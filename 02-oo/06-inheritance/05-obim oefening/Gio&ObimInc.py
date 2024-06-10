from abc import ABC,abstractmethod


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job 
        
    def get_name(self):
        return self.name
    
    def get_job(self):
        return self.job
    
class Job(ABC):
    def __init__(self, jobtitle, sickdays, salary):
        self.jobtitle = jobtitle
        self.sickdays = sickdays 
        self.salary = salary
        
    def get_jobtitle(self):
        return self.jobtitle
    
    def get_salary(self):
        return self.salary
    
    def raise_salary(self, bedrag):
        self.salary += bedrag 
    
    @abstractmethod 
    def calculate_salary(self, hours_work_per_day): 
        pass
    
class Developer(Job):
    def __init__(self, jobtitle, sickdays, salary):
        super().__init__(jobtitle, sickdays, salary)
    
    def calculate_salary(self, hours_work_per_day):
        self.salary = (hours_work_per_day * 5 * 75) 
        return self.salary 
    
class Analyst(Job):
    def __init__(self, jobtitle, sickdays, salary):
        super().__init__(jobtitle, sickdays, salary)
    
    def calculate_salary(self, hours_work_per_day):
        self.salary = (hours_work_per_day * 5 * 70)
        return self.salary

class Architect(Job):
    def __init__(self, jobtitle, sickdays, salary):
        super().__init__(jobtitle, sickdays, salary)
        
    def calculate_salary(self, hours_work_per_day):
        self.salary = (hours_work_per_day * 5 * 112.5)
        return self.salary
    
class Entreprise_Architect(Job):
    def __init__(self, jobtitle, sickdays, salary, bedrijfswagen):
        super().__init__(jobtitle, sickdays, salary)
        self.bedrijfswagen = bedrijfswagen
    
    def calculate_salary(self, hours_work_per_day):
        self.salary = (hours_work_per_day * 5 * 70)
        return self.salary
    
    def get_bedrijfswagen(self):
        return self.bedrijfswagen
    
class Bedrijfswagen:
    def __init__(self, naam, waarde):
        self.naam = naam
        self.waarde = waarde
        
    def get_naam(self):
        return self.naam
    

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, person):
        self.employees.append(person)
    
    def to_string(self):
        print(f"Company name: {self.name}")
        print(f"Team members: ")
        for person in self.employees:
            job = person.get_job()
            if job:
                if job.get_jobtitle() == "Entreprise Architect":
                    print(f"{person.get_name()}, {job.get_jobtitle()}, € {job.get_salary()}, {job.get_bedrijfswagen().get_naam()} " )
                else:
                    print(f"{person.get_name()}, {job.get_jobtitle()}, € {job.get_salary()} " )
            else:
                print(f"{person.get_name()}, null, O")
            
company = Company("Gio&Obim.inc")

bmw_x5 = Bedrijfswagen("BMW X5", 85000)

technical_software_engineer = Developer("Technical Software Engineer", 32, 0)
technical_software_engineer.calculate_salary(8)
business_analyst = Analyst("Business Analyst", 30, 0)
business_analyst.calculate_salary(8)
software_architect = Architect("Software Architect", 20, 0)
software_architect.calculate_salary(8)
entreprise_architect = Entreprise_Architect("Entreprise Architect", 15, 0, bmw_x5)
entreprise_architect.calculate_salary(10)

thomas = Person("Thomas", technical_software_engineer)
brent = Person("Brent", business_analyst)
hanni = Person("Hanni")
kaat = Person("Kaat", software_architect)
nelle = Person("Nelle", entreprise_architect)

company.add_employee(hanni)
company.add_employee(thomas)
company.add_employee(brent)
company.add_employee(kaat)
company.add_employee(nelle)

company.to_string()  