import  pytest

###跳过整个模块
###if (3 == 3):
   ### pytest.skip("跳过test_skip_third", allow_module_level=True)

###无原因跳过
@pytest.mark.skip()
def test_skip_first():
    print("未跳过test_skip_first")

###有原因跳过
@pytest.mark.skip(reason="跳过test_skip_second")
def test_skip_second():
    print("未跳过test_skip_second")



###在测试执行期间强制跳过，针对当前方法有条件的跳过某些内容
def test_skip_third():
    if(3==3):
        pytest.skip("跳过test_skip_third")
    print("未跳过test_skip_third")

###有条件的跳过某些内容
@pytest.mark.skipif(3==3,reason="跳过test_skip_fourth")
def test_skip_fourth():
    print("未跳过test_skip_fourth")

###自定义
myskip=pytest.mark.skipif(3==3,reason="跳过test_skip_fourth")
@myskip
def test_skip_fifth():
    print("未跳过test_skip_fifth")

def test_skip_sixth():
    print("未跳过test_skip_sixth")