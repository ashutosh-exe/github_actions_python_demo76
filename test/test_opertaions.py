from src.math_operations import add, subtract

def test_add():
    assert add(2,5)==5
    assert add(-1,1)==0
    assert add(0,0)==0
    
def test_subtract():
    assert subtract(5,3)==2
    assert subtract(0,0)==0
    assert subtract(-1,-1)==0
    