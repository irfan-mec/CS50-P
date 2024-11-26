from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("hello, um, world") == 1

def test_multiple_um():
    assert count("um um") == 2
    assert count("Um, um, um.") == 3
    assert count("Um... um? Um!") == 3

def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("hello world") == 0