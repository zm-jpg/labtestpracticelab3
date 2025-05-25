import employee_info as emp

def test_get_employees_by_age_range():
    result=emp.get_employees_by_age_range(25, 36)
    expected=[{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert(result==expected)

def test_calculate_average_salary():
    result=emp.calculate_average_salary()
    expected=60166.67
    assert(result==expected)

def test_get_employees_by_dept():
    result=emp.get_employees_by_dept("Marketing")
    expected=[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(result==expected)


