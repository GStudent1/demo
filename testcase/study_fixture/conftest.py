import pytest

###参数：scope="function", params=None, autouse=False, ids=None, name=None
###scope 有四个级别参数 "function" (默认), "class", "module" or "session".

###scope="function"
###@pytest.fixture()如果不写参数，默认就是scope="function"，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例运行之后运行。
###scope="class"
###fixture为class级别的时候，如果一个class里面有多个用例，都调用了此fixture，那么此fixture只在该class里所有用例开始前执行一次
###scope="module"
###fixture为module级别时，在当前.py脚本里面所有用例开始前只执行一次
###scope="session"
###fixture为session级别是可以跨.py模块调用的,也就是当我们有多个.py文件的用例时候，如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里

@pytest.fixture()
def sub():
    print("我是yield前执行的")
    yield
    print("我是yield后执行的")