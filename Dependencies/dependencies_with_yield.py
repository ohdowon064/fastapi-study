# @contextlib.contextmanager: __enter__, __exit__ 없이 컨텍스트 매니저 구현가능
# __enter__ == try, __exit__ == finally

"""
from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)

>>> with managed_resource(timeout=3600) as resource:
...     # Resource is released at the end of this block,
...     # even if code in the block raises an exception

class ManagerResource:
    def __init__(self, timeout=3600, *args, **kwargs):
        self.timeout = timeout
        self.resource = acquire_resource(*args, **kwargs)

    def __enter__(self):
        return self.resource

    def __exit__(self, teyp, value, traceback):
        release_resouce(self.resource)

>>> with ManagerResource(timeout=3600) as resource:
...     # do something
"""

async def get_db():
    db = "DBSession()"
    try:
        yield db
    finally:
        db.close() # response 후 실행

async def get_db():
    with "DBSession()" as db:
        yield db

# exit(finally) 코드는 응답을 이미 보낸 후 실행되므로 HTTPException 발생 불가 (yield 전에는 가능)
# 이미 응답을 보낸 시점에 400을 다시 보낼 수 없다.
# DB rollback, 로깅, 트랙킹 시스템 등은 가능 => 응답을 보낸 후 background 작업 실행 가능하다는 뜻

