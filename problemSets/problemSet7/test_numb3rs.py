from numb3rs import validate

def test_valid_addresses():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_addresses():
    assert validate("275.3.6.28") == False  # Out of range
    assert validate("192.168.1") == False   # Incomplete
    assert validate("192.168.1.256") == False  # 256 is out of range
    assert validate("192.168.1.-1") == False   # Negative number
    assert validate("192.168.1.1.1") == False  # Too many parts
    assert validate("abc.def.ghi.jkl") == False  # Not numbers
