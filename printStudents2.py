"""Part II - Create a program that prints the following format
(including number of characters in each combined name):
"""
#pylint: disable=C0103
def printStudents2():
    users = {
        'Students': [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ],
        'Instructors': [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'Martin', 'last_name' : 'Puryear'}
        ]
    }

    print "Students"
    for eachstudent in users["Students"]:
        namelen = len(eachstudent["first_name"])+len(eachstudent["last_name"])
        print "1 -", eachstudent["first_name"], eachstudent["last_name"], "- ", namelen
    print "Instructors"
    for eachinstructor in users["Instructors"]:
        namelen = len(eachinstructor["first_name"])+len(eachinstructor["last_name"])
        print "1 -", eachinstructor["first_name"], eachinstructor["last_name"], "- ", namelen

printStudents2()
