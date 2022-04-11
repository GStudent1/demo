import pytest


@pytest.fixture()
def login_x(request):
    x = request.param
    return x

@pytest.fixture()
def login_y(request):
    y = request.param
    return y

test_data_x = [1+1,1+2,1+4]
test_data_y = [2,3,4]


@pytest.mark.parametrize("login_x",test_data_x,indirect=True)
@pytest.mark.parametrize("login_y",test_data_y,indirect=True)
def test_login(login_x,login_y):
    a=login_x
    b=login_y
    if a==b:
        print("a=%s,b=%s" % (a,b))
        return True
    else:
        print("a=%s,b=%s" % (a, b))
        return False
