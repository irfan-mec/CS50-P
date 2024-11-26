from working import convert
import pytest

def test_valid_conversion():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Invalid separator
    with pytest.raises(ValueError):
        convert("09:60 AM to 5:00 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("13:00 PM to 9:00 AM")  # Invalid hour

def test_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"  # Midnight to noon
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"  # Noon to midnight
