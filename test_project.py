import pytest
from project import check_age, check_grades, check_nationality

def main():
    test_check_age()
    test_check_grades()
    test_check_nationality()

def test_check_age():
    assert check_age(25) == "✓ Age requirement satisfied"
    assert check_age(26) == "✗ You are above the maximum age requirement"

def test_check_grades():
    assert check_grades(79.97) == "✗ Your score is below the required percentage"
    assert check_grades(85.50) == "✓ Grade requirement satisfied"
    assert check_grades(95) == "✓ Excellent, you are well above the required percentage"

def test_check_nationality():
    assert check_nationality("india") == "✓ You can apply through both Embassy and University track"
    assert check_nationality("China") == "✓ You can only apply through university track"
    assert check_nationality("South Korea") == "✗ Korean citizens cannot apply for this scholarship."

if __name__ == "__main__":
    main()
