import pytest


###只运行用testdemo标记的测试，cmd运行的时候，加个-m 参数，指定参数值testdemo
###$ pytest -v -m testdemo
###$ pytest -v -m "not testdemo"

@pytest.mark.testdemo
def test_mark_first():
    print("执行test_mark_first")

def test_mark_second():
    print("不执行test_mark_second")