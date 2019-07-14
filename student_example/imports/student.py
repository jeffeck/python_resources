from datetime import datetime 

# See: https://stackabuse.com/how-to-format-dates-in-python/
DATE_FORMAT = '%B %d, %Y'

class Student:
    """ Base Student object """

    def __init__(self, args):
        """ When a new Student() object is created, this runs """
        self.name = args['name']
        self.id = args['id']
        self.birthdate = args['birthdate']
        self.gender = args['gender']
        self.email = args['email']

    def __str__(self):
        """ This will run when print(Student) is called """
        return ("Name: {}\nID: {}\nBirthdate: {}\nGender: {}".format(
            self.name, 
            self.id, 
            self.birthdate, 
            self.gender
        ))

    def change_name(self, new_name):
        """ Method to change the name of a student. 
        This extends to any child classes, and may also 
        be overriden """
        # TODO: log the namechange and authorize it
        self.name = new_name

    def print_name(self):
        """ Shows how the student prefers to be addressed. 
        This is inherited by child classes, and may also 
        be overriden """
        print (self.name)


    def preferred_contact(self):
        """ Returns the student's preferred mehtod of contact """
        return {'email': 'JD-Eck@wiu.edu'}

"""
    Every import below is an extension of the base Student class.
    Putting them here allows for different types of students to be 
    imported from the single class, and not having to import each 
    class specifically, however, that can still be done. 

    from student import Student, Prospective, CurrentStudent, Alumni

"""
from prospective import Prospective
from current_student import CurrentStudent
from alumni import Alumni

