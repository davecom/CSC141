import pytest
from employee import Employee

@pytest.fixture
def employee():
    return Employee("John", "Smith", 60000)

def test_give_default_raise(employee):
    old_salary = employee.salary
    employee.give_raise()
    new_salary = employee.salary
    assert new_salary == (old_salary + 5000)

def test_give_custom_raise(employee):
    old_salary = employee.salary
    employee.give_raise(10000)
    new_salary = employee.salary
    assert new_salary == (old_salary + 10000)