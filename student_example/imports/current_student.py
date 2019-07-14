
# Student is inherited base class, must be imported
from student import Student
# CurrentStudent is inherited back in student.py

class CurrentStudent(Student):
    """ Current students -- has base Student class """

    def __init__(self, args):
        """ When a new CurrentStudent() object is created, this runs """
        Student.__init__(self, args)
        self.major = args['major']
        self.gpa = args['gpa']
        self.advisor_name = args['advisor']['name']
        self.advisor_email = args['advisor']['email']


    def __str__(self):
        """ When print(CurrentStudent) is called, this runs """
        return ("The student {} ({}) is a {} major, with GPA of {}".format(
            self.name, 
            self.id, 
            self.major, 
            self.gpa 
        ))

    def registration_appointment(self):
        """ Send a reminder to the student to register for classes """
        # TODO: 
        #   attempt to find mutual time
        #   schedule prelinary meeting - add to calendars
        #   send notifications
        print ("Sending registration appointment to:\n \
{} ({}) and \n{} ({})".format(
                self.name,
                self.email, 
                self.advisor_name,
                self.advisor_email
        ))