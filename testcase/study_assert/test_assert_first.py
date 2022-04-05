
import  pytest
class TestAssertDemo:
    ###校验正常场景
    def test_assert_first(self):
        assert 2==2
        assert not False
        assert "a" in ["a","b"]
        assert True
        assert 2!=3
        assert 2%2==0,"2不为偶数"

    ###校验异常信息
    def test_assert_second(self):
        with pytest.raises(ZeroDivisionError) as excinfo:
            1/0
        assert excinfo.type ==ZeroDivisionError
        print ("excinfo.type=%s"% excinfo.type )

        assert "division by zero" in str(excinfo.value)
        print("excinfo.value=%s " % excinfo.value)

