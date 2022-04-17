"我是顶层的注释"
def func(args):
    "我是方法注释"
    pass

class spam:
    "我是类注释"
    def method(self):
        "我是类里面的方法的注释"
        print(self.__doc__)
        print(self.method.__doc__)