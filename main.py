class Student:
    def __init__(self, full_name, age, birthday, gender, courses=[]):
        self. full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = courses
    
    
    def __call__(self, course):
        self.courses.append(course)
    
    
    def __add__(self, other):
        if isinstance(other, Student):
            return self.age + other.age
        return self.age + other
    
    
    def __sub__(self, other):
        if isinstance(other, Student):
            return abs(self.age - other.age)
        return self.age - other
    
    
    def __mul__(self, other):
        if isinstance(other, Student):
            return self.age * other.age
        return self.age * other
    
    
    def __truediv__(self, other):
        if isinstance(other, Student):
            return self.age / other.age
        return self.age / other
    
    
    def __iadd__(self, other):
        if isinstance(other, int):
            self.age += other
        return self
    
    
    def __isub__(self, other):
        if isinstance(other, int):
            self.age -= other
        return self

    def __imul__(self, other):
        if isinstance(other, int):
            self.age *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, int):
            self.age /= other
        return self
    
    
    def __pow__(self, power, modulo=None):
        return self.age ** power
    
    
    def __len__(self):
        return len(self.courses)
    
    
    def __iter__(self):
        return iter(self.courses)
    
    
    def __contains__(self, item):
        return item in self.courses
    
    
    def __str__(self):
        return f"{self.full_name} ({self.age} yosh)"
    
    
    def __repr__(self):
        return f"Student({self.full_name}, {self.age}, {self.birthday}, {self.gender})"


s1 = Student("Ali Valiyev", 20, "2005-01-01", "male", ["Math"])
s2 = Student("Laylo Karimova", 22, "2003-04-12", "female", ["Biology"])

s1("English")

print(s1 + s2)      
print(s2 - s1)          
print(s1 * 2)      
print(s2 / 2)

s1 += 1
s2 *= 2
print(s1.age)       
print(s2.age)       

print(s1 ** 2)     

print(len(s1))     

for course in s1:
    print(course)

print("Math" in s1)
print("Physics" in s1)  

print(s1)          
print(repr(s2))