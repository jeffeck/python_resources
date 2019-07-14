from datetime import datetime 

# Local project imports
from student import Student, Prospective, CurrentStudent, Alumni
# from prospective import Prospective
# from current_student import CurrentStudent
# from alumni import Alumni

# See: https://stackabuse.com/how-to-format-dates-in-python/
DATE_FORMAT = '%B %d, %Y'


# Set the attributes of the student
my_attributes = {
    # Student attributes
    "id": '902073705',
    "name": "Jeff Eck",
    "birthdate": datetime(1985, 4, 5).strftime(DATE_FORMAT),
    "gender": 'male',
    "email": "JD-Eck@wiu.edu",

    # Prospective attributes
    "school": 'Ashford University',
    "load_date": datetime(2013, 6, 1).strftime(DATE_FORMAT),

    # Alumni attributes
    "degrees": {
        "program": "MS",
        "degree": "ASDA",
        "conferred_date": datetime(2019, 5, 10).strftime(DATE_FORMAT)
    },
    "alumni_email": "JD-Eck@alumni.wiu.edu",

    # Current attributes
    "major": "Applied Statistics & Decision Analytics", 
    "gpa": 4.0,
    "advisor": {
        "name": "Kasing Man",
        "email": "K-Man@wiu.edu"
    }
}




### Create different objects
me = Student(my_attributes)
me_prospective = Prospective(my_attributes)
me_current = CurrentStudent(my_attributes)
me_alumni = Alumni(my_attributes)




# me.change_name("Jeck Eff")
# print ('Student name changed to: ', me.name)

# me_prospective.contact('email')
# me_prospective.change_name('J Eck')
# print ('Prosp name: ', me_prospective.name)

me_current.registration_appointment()
# me_current.change_name('Student Jeff D. Eck')
# print ('Current name: ', me_current.name)

me_alumni.send_survey()
# me_alumni.change_name('Master Jeffrey D. Eck')
# print('Alumni name: ', me_alumni.name)
# print('Alumni email: ', me_alumni.preferred_contact())