class Test:
    test_var = 125
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # print(self)
    
    def instance_method(self):
        print('hello instance')

    @staticmethod
    def static_method():
        print('this is static method')

    @classmethod
    def class_method(cls):
        print(f'class variable {cls.test_var}')


# Instance object
t1 = Test(a=12, b=100) # it creates class object
# t2 = Test() 

# print(t1)  t1 and self pointing to the same object
# print(t1.a, t1.b)
# t1.instance_method()
# t1.static_method()
# Test.class_method()

# class object
# Test, it represents the class object
# One class has exactly one class object but can have any number of Instance objects


"""
class object variable -> static object variable 

isinstance object variable -> __init__()
"""


class Employee:
    def __init__(self, em_id, emp_name, emp_salary):
        self.emp_id = em_id
        self.emp_name = emp_name
        self.emp_salry = emp_salary