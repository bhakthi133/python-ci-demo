def test_add():
    from calculator import add
    n1= 5
    n2=-1
    assert add(n1,n2) == n1+n2
    assert add(10,17) == 27
    assert add(-6,-8) == -14
def test_sub():
    from calculator import sub
    n1= -2
    n2=-1
    assert sub(n1,n2) == n1-n2
    assert sub(10,17) == -7
    assert sub(-6,-8) ==2
def test_mul():
    from calculator import mul
    n1= 5
    n2=-1
    assert mul(n1,n2) == n1*n2
    assert mul(10,17) == 170
    assert mul(0,8) == 0
    assert mul(-9,-10) == 90
def test_div():
    from calculator import div
    n1= 10
    n2= 2
    if(n2==0):
        assert div(n1,n2) == "invalid divission"
    else:
        assert div(n1,n2) == n1/n2
    assert div(10,0) == "invalid division"
def test_power():
    from calculator import power
    n1= 5
    n2=-1
    assert power(n1,n2) == n1**n2
    assert power(10,0) == 1
    assert power(-6,2) == 36
def test_square():
    from calculator import square
    n1 = 5
    assert square(n1) == n1**2

