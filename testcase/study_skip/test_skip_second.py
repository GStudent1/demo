###在test_skip_first.py里定义的myskip，可以跨模块使用
from study_fixture import  myskip

@myskip
def test_skip_seventh():
    print("未跳过test_skip_seventh")

def test_skip_eighth():
    print("未跳过test_skip_eighth")