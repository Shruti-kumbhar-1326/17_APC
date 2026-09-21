class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name =", self.name)
        print("Age =", self.age)


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_doctor(self):
        print("Specialization =", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def display_patient(self):
        print("Disease =", self.disease)


class Surgeon(Doctor):
    def surgery(self):
        print("Surgeon performs surgery")


class MedicalResearcher(Doctor, Patient):
    def research(self):
        print("Medical researcher performs research")


# Create objects
s = Surgeon("Dr. Rahul", 40, "General Surgery")

m = MedicalResearcher("Dr. Amit", 35, "Medical Research")


print("Surgeon Details:")
s.display_person()
s.display_doctor()
s.surgery()

print("\nMedical Researcher Details:")
m.display_person()
m.research()