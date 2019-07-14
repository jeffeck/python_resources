
from student import Student

class Alumni(Student):
    """ Alumni -- has Student base class """

    def __init__(self, args):
        """ When a new Alumni() object is created, this runs """
        # Set the base attributes
        Student.__init__(self, args)

        # TODO: refactor to handle >1 degrees
        # Extract the degree dictionary
        degree = args['degrees']
        # Set degree attributes
        self.program = degree['program']
        self.degree = degree['degree']
        self.conferred_date = degree['conferred_date']
        self.alumni_email = args['alumni_email']


    def __str__(self):
        """ This runs when print(Alumni) is called """
        return ("The Degree {}\nwas conferred to {}\non {}.".format(
            self.program + " " + self.degree, 
            self.name,
            self.conferred_date,
        ))

    def base_str(self):
        """ Gets the str(Student) object """
        return super().__str__()


    def preferred_contact(self):
        """ Returns the alumni preferred contact.
        This will override the base Student preferred contact.
        """
        return {'email': 'jd-eck@alumni.wiu.edu'}
        
    
    def send_survey(self, emails=None, message=None):
        """ Sends the alumni survey """
        # get email
        email = self.preferred_contact()['email`']
        # get survey

        # send survey
        print ('Sending survey to alumni at {}'.format(
            email
        ))


