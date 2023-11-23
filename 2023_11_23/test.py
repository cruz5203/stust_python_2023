class employee:
    emp_salary=0
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
    def assign_department(self,emp_department):
        self.emp_department=emp_department
    def print_employee_details(self):
        print(self.emp_id,self.emp_name,self.emp_salary,self.emp_department)
    def calculate_emp_salary(self,hours_worked):
        if hours_worked>50:
            self.emp_salary=self.emp_salary+(hours_worked-50)*(self.emp_salary)/50

def main():
    emp=employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    emp.calculate_emp_salary(60)
    emp.assign_department("SALES")
    emp.print_employee_details()

if __name__=="__main__":
    main()
