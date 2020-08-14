from types import CodeType, FrameType, TracebackType, coroutine
from typing import Any, Coroutine, Iterator, Optional, Type, TypeVar, Union

_T_co = TypeVar("_T_co", covariant=True)
_V_co = TypeVar("_V_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

class AsyncBase:
    def __init__(self, file: str, loop: Any, executor: Any) -> None: ...
    async def __aiter__(self) -> Iterator[str]: ...
    async def __anext__(self) -> str: ...

class _ContextManager(Coroutine[_V_co, _T_co, _T_contra]):
    def __init__(self, __coro: Coroutine[_V_co, _T_co, _T_contra]) -> None: ...
    def send(self, __value: _T_contra) -> _T_co: ...
    def throw(
        self, __typ: Type[BaseException], __val: Union[BaseException, object] = ..., tb: Optional[TracebackType] = ...,
    ) -> _T_co: ...
    def close(self) -> None: ...
    @property
    def gi_frame(self) -> FrameType: ...
    @property
    def gi_running(self) -> bool: ...
    @property
    def gi_code(self) -> CodeType: ...
    def __next__(self) -> _T_co: ...
    @coroutine
    def __iter__(self) -> Iterator[Coroutine[_V_co, _T_co, _T_contra]]: ...
    def __await__(self) -> None: ...
    async def __anext__(self) -> Coroutine[_V_co, _T_co, _T_contra]: ...
    async def __aenter__(self) -> Coroutine[_V_co, _T_co, _T_contra]: ...
    async def __aexit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType],
    ) -> None: ...

class AiofilesContextManager(_ContextManager):
    async def __aexit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType],
    ) -> None: ...

