
###模块级开始于模块始末，全局的（setup_module/teardown_module）
def setup_module():
    print("我是setup_module，模块级的，模块开始前执行")
def teardown_module():
    print("我是teardown_module，模块级的，模块结尾后执行")

###函数级只对函数用例生效（不在类中）（setup_function/teardown_function）
def setup_function():
    print("我是setup_function，函数级的，函数开始前执行")
def teardown_function():
    print("我是teardown_function，函数级的，函数结尾后执行")

def test_function():
    print("我是函数")

def add(x):
    return x+ 1

class TestMainDemo:
    ###类级只在类中前后运行一次(在类中)（setup_class/teardown_class）
    def setup_class(self):
        print("我是setup_class，类级的，类开始前执行")

    def teardown_class(self):
        print("我是teardown_class，类级的，类结尾后执行")

    ###方法级开始于方法始末（在类中）（setup_method/teardown_method）
    def setup_method(self):
        print("我是setup_method，方法级的，方法开始前执行")

    def teardown_method(self):
        print("我是teardown_method，方法级的，方法结尾后执行")


    def test_add_first(self):
        assert add(3) == 4
        print("我是方法1")

    def test_add_second(self):
        assert add(4) == 5
        print("我是方法2")

