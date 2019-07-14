from datetime import datetime 

# Student is inherited base class, must be imported
from student import Student 
# The Prospective class is inherited back into student.py


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


    def contact(self, method):
        """ Initiate a contact with the prospect """
        # TODO: Log the contact
        print ('Contacting {} at {} by {}'.format(
            self.name,
            datetime.now(), 
            method
        ))