from hello import add

def test_add():
    assert 8 ==add(5,3)    #The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
    ##if condition returns False, AssertionError is raised:
     #assert x == "goodbye", "x should be 'hello'"