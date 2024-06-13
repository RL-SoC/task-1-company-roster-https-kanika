"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            age= int(input("Age"))
            ID = int(input("ID:"))
            city = input("City:")
            branchcodes = input("Branch(es):")
            # How will you conver this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes = list(map(int, branchcodes.split(",")))
            position= input("Position: ")
            salary =int(input("Salary: "))
            # Create a new Engineer with given details.
            engineer = Engineer(name, age, ID, city, branchcodes, position, salary) # Change this

            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson
            # Then add them to the roster
            name = input("Name:")
            age= input("Age")
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            branchcodes = list(map(int, branchcodes.split(",")))
            position= input("Position: ")
            salary = int(input("Salary: "))

            salesman= Salesman(name,age,ID,city,branchcodes,position,salary)

            sales_roster.append(salesman)
            

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            employee_roster = engineer_roster + sales_roster
            for employee in employee_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names =[]
                ## ???? what comes here??
                # print(f"Branches: " + ???? )
                branches=found_employee.branches
                for branch_code in branches:
                    branch_names.append(branchmap[branch_code].get("name"))
                    
                    
                print(f"Branches: {branch_names}")
                print(f"Position: {found_employee.position}")
                print(f"Salary: {found_employee.salary}")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("ID: "))
            new_code=int(input("New code: "))
            found_employee=None
            employee_roster= engineer_roster + sales_roster
            for employee in employee_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            if found_employee is None:
                print("No such employee")
            res=found_employee.migrate_branch(new_code)
            if res:
                print("Branch changed(for engineer)/added(for salesman) successfully!")
            else:
                print("If engineer, only works for those who have single branch; If salesman, incorrect branch code")
            
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            position=str(input("Enter position to promote: "))
            found_employee=None
            employee_roster= engineer_roster + sales_roster
            for employee in employee_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            if found_employee is None:
                print("No such employee")
            res=found_employee.promote(position)
            if res:
                print("Employee promoted successfully!")
            else:
                print("Invalid position")            
            # promote employee to next position

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            increment=float(input("Enter increment: "))
            found_employee=None
            employee_roster= engineer_roster + sales_roster
            for employee in employee_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            if found_employee is None:
                print("No such employee")
            found_employee.increment(increment)
            print("Incremented successfully")
            # Increment salary of employee.
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            found_employee=None
            for employee in sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            if found_employee is None:
                print("No such employee")
            print(f"Superior: {found_employee.find_superior()}")
            # Print superior of the sales employee.
        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            found_employee=None
            for employee in sales_roster:
                if employee.ID == ID_E:
                    found_employee = employee
                    break
            if found_employee is None:
                print("No such employee")
            res=found_employee.add_superior(ID_S)
            if res:
                print("Superior added successfully")
            else:
                print("Given ID cannot be superior for the selected employee")
            # Add superior of a sales employee

        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






