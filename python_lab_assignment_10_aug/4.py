#  Write a Python function employee_salary(*args, **kwargs) where *args contains employee salaries and **kwargs contains employee names with their salaries. Calculate the average salary, highest salary, lowest salary, and identify employees earning above the average salary.  
def employee_salary(*args, **kwargs):
    # Calculate average salary
    average_salary = sum(args) / len(args) if args else 0
    
    # Find highest and lowest salaries
    highest_salary = max(args) if args else 0
    lowest_salary = min(args) if args else 0
    
    # Identify employees earning above the average salary
    above_average_employees = [name for name, salary in kwargs.items() if salary > average_salary]
    
    # Display results
    print("Average Salary:", average_salary)
    print("Highest Salary:", highest_salary)
    print("Lowest Salary:", lowest_salary)
    print("Employees earning above average:", above_average_employees)
