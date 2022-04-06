import pytest


@pytest.fixture()
def login(request):
    x = request.param["x"]
    y = request.param["y"]
    if x==y:
        return True
    else:
        return False

test_data = [{"x":1+1,"y":2},{"x":1+2,"y":3},{"x":1+4,"y":4}]

@pytest.mark.parametrize("login",test_data,indirect=True)
def test_login(login):
    a=login
    print("a=%s"%a)


