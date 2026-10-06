company = "Tech Solutions"  # Global variable

def department():
    department_name = "Python Development"  # Enclosing variable

    def employee():
        employee_name = "Kiran"  # Local variable

        print(employee_name)       # Local
        print(department_name)     # Enclosing
        print(company)             # Global

        def project():
            project_name = "E-Commerce"  # Local to project()

            print(project_name)      # Local
            print(department_name)   # Enclosing
            print(company)           # Global

        project()

    employee()

department()