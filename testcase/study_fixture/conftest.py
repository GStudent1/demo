import pytest
###参数：scope="function", params=None, autouse=False, ids=None, name=None
###scope 有四个级别参数 "function" (默认), "class", "module" or "session".
@pytest.fixture()
def sub():
    print("我是yield前执行的")
    yield
    print("我是yield后执行的")