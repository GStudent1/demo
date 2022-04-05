import pytest


def test_demo_fifth(sub):
    print("test_demo_fifth")

class TestFixtureDemoSecond:
    def test_demo_third(self):
        print("test_demo_third")
    def test_demo_fourth(self,sub):
        print("test_demo_fourth")