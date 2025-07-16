from .__version__ import __description__, __title__, __version__
from ._api import *
from ._auth import *
from ._client import *
from ._config import *
from ._content import *
from ._exceptions import *
from ._models import *
from ._status_codes import *
from ._transports import *
from ._types import *
from ._urls import *

try:
    from ._main import main
except ImportError:  # pragma: no cover

    def main() -> None:  # type: ignore
        import sys

        print(
            "The httpx command line client could not run because the required "
            "dependencies were not installed.\nMake sure you've installed "
            "everything with: pip install 'httpx[cli]'"
        )
        sys.exit(1)


__all__ = [
    "URL",
    "USE_CLIENT_DEFAULT",
    "ASGITransport",
    "AsyncBaseTransport",
    "AsyncByteStream",
    "AsyncClient",
    "AsyncHTTPTransport",
    "Auth",
    "BaseTransport",
    "BasicAuth",
    "ByteStream",
    "Client",
    "CloseError",
    "ConnectError",
    "ConnectTimeout",
    "CookieConflict",
    "Cookies",
    "DecodingError",
    "DigestAuth",
    "HTTPError",
    "HTTPStatusError",
    "HTTPTransport",
    "Headers",
    "InvalidURL",
    "Limits",
    "LocalProtocolError",
    "MockTransport",
    "NetRCAuth",
    "NetworkError",
    "PoolTimeout",
    "ProtocolError",
    "Proxy",
    "ProxyError",
    "QueryParams",
    "ReadError",
    "ReadTimeout",
    "RemoteProtocolError",
    "Request",
    "RequestError",
    "RequestNotRead",
    "Response",
    "ResponseNotRead",
    "StreamClosed",
    "StreamConsumed",
    "StreamError",
    "SyncByteStream",
    "Timeout",
    "TimeoutException",
    "TooManyRedirects",
    "TransportError",
    "UnsupportedProtocol",
    "WSGITransport",
    "WriteError",
    "WriteTimeout",
    "__description__",
    "__title__",
    "__version__",
    "codes",
    "create_ssl_context",
    "delete",
    "get",
    "head",
    "main",
    "options",
    "patch",
    "post",
    "put",
    "request",
    "stream",
]


__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        setattr(__locals[__name], "__module__", "httpx")  # noqa
