"""
Type definitions for type checking purposes.
"""

from collections.abc import (
    AsyncIterable,
    AsyncIterator,
    Callable,
    Iterable,
    Iterator,
    Mapping,
    Sequence,
)
from http.cookiejar import CookieJar
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    Optional,
    Union,
)

if TYPE_CHECKING:  # pragma: no cover
    from ._auth import Auth
    from ._config import Proxy, Timeout
    from ._models import Cookies, Headers, Request
    from ._urls import URL, QueryParams


PrimitiveData = Optional[str | int | float | bool]

URLTypes = Union["URL", str]

QueryParamTypes = Union[
    "QueryParams",
    Mapping[str, PrimitiveData | Sequence[PrimitiveData]],
    list[tuple[str, PrimitiveData]],
    tuple[tuple[str, PrimitiveData], ...],
    str,
    bytes,
]

HeaderTypes = Union[
    "Headers",
    Mapping[str, str],
    Mapping[bytes, bytes],
    Sequence[tuple[str, str]],
    Sequence[tuple[bytes, bytes]],
]

CookieTypes = Union["Cookies", CookieJar, dict[str, str], list[tuple[str, str]]]

TimeoutTypes = Union[
    float | None,
    tuple[float | None, float | None, float | None, float | None],
    "Timeout",
]
ProxyTypes = Union["URL", str, "Proxy"]
CertTypes = Union[str, tuple[str, str], tuple[str, str, str]]

AuthTypes = Union[
    tuple[str | bytes, str | bytes],
    Callable[["Request"], "Request"],
    "Auth",
]

RequestContent = Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]
ResponseContent = Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]
ResponseExtensions = Mapping[str, Any]

RequestData = Mapping[str, Any]

FileContent = Union[IO[bytes], bytes, str]
FileTypes = Union[
    # file (or bytes)
    FileContent,
    # (filename, file (or bytes))
    tuple[str | None, FileContent],
    # (filename, file (or bytes), content_type)
    tuple[str | None, FileContent, str | None],
    # (filename, file (or bytes), content_type, headers)
    tuple[str | None, FileContent, str | None, Mapping[str, str]],
]
RequestFiles = Union[Mapping[str, FileTypes], Sequence[tuple[str, FileTypes]]]

RequestExtensions = Mapping[str, Any]

__all__ = ["AsyncByteStream", "SyncByteStream"]


class SyncByteStream:
    def __iter__(self) -> Iterator[bytes]:
        raise NotImplementedError(
            "The '__iter__' method must be implemented."
        )  # pragma: no cover
        yield b""  # pragma: no cover

    def close(self) -> None:
        """
        Subclasses can override this method to release any network resources
        after a request/response cycle is complete.
        """


class AsyncByteStream:
    async def __aiter__(self) -> AsyncIterator[bytes]:
        raise NotImplementedError(
            "The '__aiter__' method must be implemented."
        )  # pragma: no cover
        yield b""  # pragma: no cover

    async def aclose(self) -> None:
        pass
