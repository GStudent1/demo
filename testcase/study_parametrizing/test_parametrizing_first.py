import  pytest
###parametrize用于实现测试用例参数化

@pytest.mark.parametrize("x,y",[(1+1,2),(2+2,4),(3+3,6)])
def test_parametrizing_first(x,y):
    assert x==y


@pytest.mark.parametrize("x",[1,2,3])
@pytest.mark.parametrize("y",[4,5,6])
def test_parametrizing_second(x,y):
    print("x=%d,y=%d" % (x,y) )