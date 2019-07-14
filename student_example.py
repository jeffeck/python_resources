from datetime import datetime 

# See: https://stackabuse.com/how-to-format-dates-in-python/
DATE_FORMAT = '%B %d, %Y'

class Student:
    """ Student object """

    def __init__(self, args):
        """ When a new Student() object is created, this runs """
        self.name = args['name']
        self.id = args['id']
        self.birthdate = args['birthdate']
        self.gender = args['gender']

    def __str__(self):
        """ This will run when print(Student) is called """
        return ("Name: {}\nID: {}\nBirthdate: {}\nGender: {}".format(
            self.name, 
            self.id, 
            self.birthdate, 
            self.gender
        ))


class Prospective(Student):
    """ Prospective Student -- has Student base class """

    def __init__(self, args):
        """ When a new Prospective() object is created, this runs """
        # The base class needs to run the __init__ method to set variables of base 
        Student.__init__(self, args)

        # Assign Prospective specific variables
        self.school = args['school'] 
        self.load_date = args['load_date']


    def __str__(self):
        """ When print(Prospective) is called, this runs. 
            If __str__ is not defined, the base class Student()'s __str__ function 
                will run """ 
        return ("Student: {}\nID: {}\nSchool: {}\nLoad Date: {}".format(
            self.name,
            self.id, 
            self.school, 
            self.load_date 
        ))


class CurrentStudent(Student):
    """ Current students -- has base Student class """

    def __init__(self, args):
        """ When a new CurrentStudent() object is created, this runs """
        Student.__init__(self, args)
        self.major = args['major']
        self.gpa = args['gpa']

    def __str__(self):
        """ When print(CurrentStudent) is called, this runs """
        return ("The student {} ({}) is a {} major, with GPA of {}".format(
            self.name, 
            self.id, 
            self.major, 
            self.gpa 
        ))


class Alumni(Student):
    """ Alumni -- has Student base class """

    def __init__(self, args):
        """ When a new Alumni() object is created, this runs """
        # Set the base attributes
        Student.__init__(self, args)

        # Extract the degree dictionary
        degree = args['degrees']
        # Set degree attributes
        self.program = degree['program']
        self.degree = degree['degree']
        self.conferred_date = degree['conferred_date']


    def __str__(self):
        """ This runs when print(Alumni) is called """
        return ("The Degree {}\nwas conferred to {}\non {}.".format(
            self.program + " " + self.degree, 
            self.name,
            self.conferred_date,
        ))

    def base_str(self):
        return super().__str__()


# Set the attributes of the student
my_attributes = {
    # Student attributes
    "id": '902073705',
    "name": "Jeff Eck",
    "birthdate": datetime(1985, 4, 5).strftime(DATE_FORMAT),
    "gender": 'male',

    # Prospective attributes
    "school": 'Ashford University',
    "load_date": datetime(2013, 6, 1).strftime(DATE_FORMAT),

    # Alumni attributes
    "degrees": {
        "program": "MS",
        "degree": "ASDA",
        "conferred_date": datetime(2019, 5, 10).strftime(DATE_FORMAT)
    },

    # Current attributes
    "major": "Applied Statistics & Decision Analytics", 
    "gpa": 4.0
}




### Create different objects
# me = Student(my_attributes)
# me = Prospective(my_attributes)
# me = CurrentStudent(my_attributes)
me = Alumni(my_attributes)


# print ('me: ', type(me))
print ('student: ', me.base_str())
print ('alumni: ', str(me))


### Print (__str__) objects
# print('Student: \n', str(me), '\n' * 2)
# print('Prospect: ', me.name, me.school, me.load_date)
# print('Current: ', me.name, me.major, me.gpa)
# print('Alumni: \n', str(me), '\n' * 2)

# my_name = me.name 
my_name = 'Jeff'

def greet(greeting, name):
    print ("{}, {}".format(greeting, name))

# greet("Hello", my_name)
# greet("Goodbye", "Bob")
# greet(my_name, my_name)

















































##### Software specifications ####
# Create related student objects: Prospective, Current, Alumni
# Each object should receive attributes and create a new instance
# Each object needs one method
##################################


""" Desired results:
{
    student {
        "id": "902073705",
        "name": "Jeff Eck",
        "birthdate": 1985/04/05,
        "gender": "male",
        "prospective": {
            "school": "Ashford University",
            "load_date": 2013/05/01
        },
        "current": {
            "major": "ASDA",
            "gpa": 4.0
        },
        "alumni": {
            {
                "conferred_date": 2019/05/10,
                "program": "MS",
                "degree": "ASDA"
            },
            {
                "conferred_date": 2018/12/19,
                "program": "PBC",
                "degree": "Business Analytics"
            },
            {
                "conferred_date": 2017/07/31,
                "program": "MS",
                "degree": "Computer Science"
            }
        }
    }
}


"""