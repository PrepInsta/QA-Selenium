

def add(x):
    return x+1

def test_add():
    assert add(3)==4
    print("running a test")

def test_add_fail():
    assert add(3)==5

