import re
from unittest.mock import Mock, AsyncMock
import pytest

from scrapecore.engines.toolbelt.custom import Response
from scrapecore.engines.toolbelt.convertor import ResponseFactory
from scrapecore.engines._browsers._base import SyncSession, AsyncSession
from scrapecore.engines._browsers._validators import validate_fetch, PlaywrightConfig


class TestResponseXHRFeatures:
    """Test Response class XHR filtering, querying and properties"""

    def test_xhr_properties_and_filtering(self):
        main_resp = Response(
            url="https://example.com",
            content=b"<html><body>Main Page</body></html>",
            status=200,
            reason="OK",
            cookies={},
            headers={"content-type": "text/html"},
            request_headers={},
            method="GET",
        )

        xhr1 = Response(
            url="https://example.com/api/v1/users",
            content=b'{"users": ["alice", "bob"]}',
            status=200,
            reason="OK",
            cookies={},
            headers={"content-type": "application/json"},
            request_headers={},
            method="GET",
            meta={"resource_type": "fetch", "post_data": None},
        )

        xhr2 = Response(
            url="https://example.com/api/v1/login",
            content=b'{"token": "xyz123"}',
            status=201,
            reason="Created",
            cookies={},
            headers={"content-type": "application/json"},
            request_headers={},
            method="POST",
            meta={"resource_type": "xhr", "post_data": '{"username": "admin"}'},
        )

        xhr3 = Response(
            url="https://example.com/analytics/collect",
            content=b"ok",
            status=204,
            reason="No Content",
            cookies={},
            headers={},
            request_headers={},
            method="POST",
            meta={"resource_type": "fetch", "post_data": "event=click"},
        )

        main_resp.captured_xhr = [xhr1, xhr2, xhr3]

        # Properties
        assert xhr2.post_data == '{"username": "admin"}'
        assert xhr2.request_data == '{"username": "admin"}'
        assert xhr2.resource_type == "xhr"
        assert main_resp.xhr_urls == [
            "https://example.com/api/v1/users",
            "https://example.com/api/v1/login",
            "https://example.com/analytics/collect",
        ]

        # Filter by regex string
        api_requests = main_resp.filter_xhr(r"/api/v1/")
        assert len(api_requests) == 2
        assert api_requests[0].url == "https://example.com/api/v1/users"
        assert api_requests[1].url == "https://example.com/api/v1/login"

        # Filter by compiled Pattern
        pattern = re.compile(r"/login$")
        login_requests = main_resp.filter_xhr(pattern)
        assert len(login_requests) == 1
        assert login_requests[0].url == "https://example.com/api/v1/login"

        # Filter by callable
        custom_filtered = main_resp.filter_xhr(lambda r: "analytics" in r.url)
        assert len(custom_filtered) == 1
        assert custom_filtered[0].url == "https://example.com/analytics/collect"

        # Filter by callable accepting url string
        custom_url_func = main_resp.filter_xhr(lambda url: url.endswith("users"))
        assert len(custom_url_func) == 1
        assert custom_url_func[0].url == "https://example.com/api/v1/users"

        # Filter by method
        posts = main_resp.filter_xhr(method="POST")
        assert len(posts) == 2

        # Filter by method and status
        created_post = main_resp.filter_xhr(method="POST", status=201)
        assert len(created_post) == 1
        assert created_post[0].url == "https://example.com/api/v1/login"

        # find_xhr
        found_login = main_resp.find_xhr(r"login")
        assert found_login is not None
        assert found_login.url == "https://example.com/api/v1/login"
        assert main_resp.find_xhr(r"nonexistent") is None

        # xhr_json helper
        users_json = main_resp.xhr_json(r"users")
        assert users_json == {"users": ["alice", "bob"]}

        login_json = main_resp.xhr_json(r"login")
        assert login_json == {"token": "xyz123"}

        default_val = main_resp.xhr_json(r"nonexistent", default={"fallback": True})
        assert default_val == {"fallback": True}

        # Non-JSON xhr returns default
        analytics_json = main_resp.xhr_json(r"analytics", default="NOT_JSON")
        assert analytics_json == "NOT_JSON"


class TestResponseFactoryXHR:
    """Test ResponseFactory correctly parses XHR responses and requests"""

    def test_sync_playwright_xhr_conversion(self):
        # Mock main response and page
        mock_response = Mock()
        mock_response.url = "https://example.com"
        mock_response.status = 200
        mock_response.status_text = "OK"
        mock_response.headers = {"content-type": "text/html"}
        mock_response.all_headers = Mock(return_value={"content-type": "text/html"})
        mock_response.body = Mock(return_value=b"<html><body>Test</body></html>")
        mock_response.request.all_headers = Mock(return_value={})
        mock_response.request.redirected_from = None
        mock_response.request.method = "GET"
        mock_response.request.resource_type = "document"
        mock_response.request.post_data = None

        mock_page = Mock()
        mock_page.url = "https://example.com"
        mock_page.content = Mock(return_value="<html><body>Test</body></html>")
        mock_page.context.cookies = Mock(return_value=[])

        # Mock captured XHR
        mock_xhr = Mock()
        mock_xhr.url = "https://example.com/api/data"
        mock_xhr.status = 200
        mock_xhr.status_text = "OK"
        mock_xhr.headers = {"content-type": "application/json"}
        mock_xhr.all_headers = Mock(return_value={"content-type": "application/json"})
        mock_xhr.body = Mock(return_value=b'{"success": true}')
        mock_xhr.request.all_headers = Mock(return_value={"authorization": "Bearer 123"})
        mock_xhr.request.redirected_from = None
        mock_xhr.request.method = "POST"
        mock_xhr.request.resource_type = "xhr"
        mock_xhr.request.post_data = '{"query": "test"}'

        response = ResponseFactory.from_playwright_response(
            mock_page,
            mock_response,
            mock_response,
            {"adaptive": False},
            captured_xhr=[mock_xhr],
        )

        assert response.status == 200
        assert len(response.captured_xhr) == 1
        captured = response.captured_xhr[0]
        assert captured.url == "https://example.com/api/data"
        assert captured.method == "POST"
        assert captured.resource_type == "xhr"
        assert captured.post_data == '{"query": "test"}'
        assert captured.json() == {"success": True}

    @pytest.mark.asyncio
    async def test_async_playwright_xhr_conversion(self):
        mock_response = Mock()
        mock_response.url = "https://example.com"
        mock_response.status = 200
        mock_response.status_text = "OK"
        mock_response.headers = {"content-type": "text/html"}
        mock_response.all_headers = AsyncMock(return_value={"content-type": "text/html"})
        mock_response.body = AsyncMock(return_value=b"<html><body>Test</body></html>")
        mock_response.request.all_headers = AsyncMock(return_value={})
        mock_response.request.redirected_from = None
        mock_response.request.method = "GET"
        mock_response.request.resource_type = "document"
        mock_response.request.post_data = None

        mock_page = Mock()
        mock_page.url = "https://example.com"
        mock_page.content = AsyncMock(return_value="<html><body>Test</body></html>")
        mock_page.context.cookies = AsyncMock(return_value=[])

        mock_xhr = Mock()
        mock_xhr.url = "https://example.com/api/async-data"
        mock_xhr.status = 200
        mock_xhr.status_text = "OK"
        mock_xhr.headers = {"content-type": "application/json"}
        mock_xhr.all_headers = AsyncMock(return_value={"content-type": "application/json"})
        mock_xhr.body = AsyncMock(return_value=b'{"async": true}')
        mock_xhr.request.all_headers = AsyncMock(return_value={})
        mock_xhr.request.redirected_from = None
        mock_xhr.request.method = "GET"
        mock_xhr.request.resource_type = "fetch"
        mock_xhr.request.post_data = None

        response = await ResponseFactory.from_async_playwright_response(
            mock_page,
            mock_response,
            mock_response,
            {"adaptive": False},
            captured_xhr=[mock_xhr],
        )

        assert response.status == 200
        assert len(response.captured_xhr) == 1
        captured = response.captured_xhr[0]
        assert captured.url == "https://example.com/api/async-data"
        assert captured.method == "GET"
        assert captured.resource_type == "fetch"
        assert captured.json() == {"async": True}


class TestBrowserResponseHandler:
    """Test sync and async browser response handlers with xhr_pattern options"""

    def test_sync_handler_patterns(self):
        page_info = Mock()
        page_info.page.main_frame = Mock()
        resp_container = [None]

        # 1. True: captures all xhr/fetch
        captured = []
        handler_all = SyncSession._create_response_handler(page_info, resp_container, True, captured)

        resp_xhr = Mock()
        resp_xhr.request.resource_type = "xhr"
        resp_xhr.url = "https://example.com/api/data"

        resp_image = Mock()
        resp_image.request.resource_type = "image"
        resp_image.url = "https://example.com/img.png"

        handler_all(resp_xhr)
        handler_all(resp_image)
        assert len(captured) == 1
        assert captured[0] == resp_xhr

        # 2. String regex pattern
        captured_regex = []
        handler_regex = SyncSession._create_response_handler(page_info, resp_container, r"/users/\d+", captured_regex)
        resp_users = Mock()
        resp_users.request.resource_type = "fetch"
        resp_users.url = "https://example.com/users/42"

        resp_posts = Mock()
        resp_posts.request.resource_type = "fetch"
        resp_posts.url = "https://example.com/posts/abc"

        handler_regex(resp_users)
        handler_regex(resp_posts)
        assert len(captured_regex) == 1
        assert captured_regex[0] == resp_users

        # 3. Callable filter
        captured_fn = []
        handler_fn = SyncSession._create_response_handler(page_info, resp_container, lambda r: "important" in r.url, captured_fn)
        resp_imp = Mock()
        resp_imp.request.resource_type = "xhr"
        resp_imp.url = "https://example.com/important-api"

        resp_norm = Mock()
        resp_norm.request.resource_type = "xhr"
        resp_norm.url = "https://example.com/normal-api"

        handler_fn(resp_imp)
        handler_fn(resp_norm)
        assert len(captured_fn) == 1
        assert captured_fn[0] == resp_imp

    @pytest.mark.asyncio
    async def test_async_handler_patterns(self):
        page_info = Mock()
        page_info.page.main_frame = Mock()
        resp_container = [None]
        captured = []
        handler_all = AsyncSession._create_response_handler(page_info, resp_container, True, captured)

        resp_xhr = Mock()
        resp_xhr.request.resource_type = "fetch"
        resp_xhr.url = "https://example.com/api/async-data"

        await handler_all(resp_xhr)
        assert len(captured) == 1
        assert captured[0] == resp_xhr


class TestValidationAndConfig:
    """Test validation of capture_xhr configuration and parameters"""

    def test_config_and_fetch_validation(self):
        config_true = PlaywrightConfig(capture_xhr=True)
        assert config_true.capture_xhr is True

        config_pattern = PlaywrightConfig(capture_xhr=r"/api/.*")
        assert config_pattern.capture_xhr == r"/api/.*"

        fn = lambda url: True
        config_fn = PlaywrightConfig(capture_xhr=fn)
        assert config_fn.capture_xhr == fn

        # validate_fetch override
        session_mock = Mock()
        session_mock._config = config_true
        params = validate_fetch({"capture_xhr": True}, session=session_mock, model=PlaywrightConfig)
        assert params.capture_xhr is True
