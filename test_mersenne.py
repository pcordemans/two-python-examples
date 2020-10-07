from mersenne import potential_MP, is_prime, is_mp

def test_is_prime():
    assert  not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)

def test_potential_mp():
    assert potential_MP(2) == 3
    assert potential_MP(3) == 7
    assert potential_MP(4) == 15

def test_mp():
    assert is_mp(2)
    assert is_mp(3)
    assert not is_mp(4) 