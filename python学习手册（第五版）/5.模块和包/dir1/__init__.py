print('dir1 init')
x = 1

def test():
    from . import dir2
    print(dir2.y)