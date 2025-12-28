from datetime import datetime
class Developer:
    LIMIT = 3
    def __init__(self, name , age):
        self.name = name
        self.age = age
        self.skills = []

    def __str__(self):
        result = (f"Class name is : {self.__class__.__name__}\nName of the Developer : {self.name}\nAge : {self.age}\nNumber of skills : {len(self.skills)}")
        return result
    
    def add_skill(self, skill):
        if len(self.skills) < Developer.LIMIT:
            self.skills.append(skill)
            print(f"{skill} added successfully")
        else:
            print(f"You cannot add more than {Developer.LIMIT} skills !")

    def show_skills(self):
        print(f"The skills of {self.name} are as follows : ")
        for skill in self.skills:
            print(skill,end="\n")

    @classmethod
    def set_limit(cls, new_limit):
        Developer.LIMIT = new_limit


    @classmethod
    def from_birthyear(cls, name, birthyear):
        year = Developer.birthyeartoage(birthyear)
        return cls(name, year-birthyear)
    
    @staticmethod
    def birthyeartoage(brithyear):
        year = datetime.today().year
        return year


print("This information belongs to first developer : ")
d1 = Developer("Sathvik", 23)
d1.add_skill("Python")
d1.add_skill("Java")
d1.add_skill("C++")
Developer.set_limit(4) 
d1.add_skill("Full Stack")
print(d1)
d1.show_skills()

print("The information belongs to second developer : ")
d2 = Developer.from_birthyear("Nandeesha", 1967)
d2.add_skill("Communication")
d2.add_skill("Team Lead")
print(d2)