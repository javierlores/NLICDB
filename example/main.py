__author__ = "Javier Lores"

import sys
sys.path.append("../src")
from generate import Generator
sys.path.append("../../concourse/concourse-driver-python/")
from concourse import Concourse
import csv


def create_db():
    # Create the database connection
    db = Concourse.connect()

    # The database will be populated with a list of employees
    # Each employee record will contain the following information
    # ID, Name, Dept, Gender, Country, Salary, Age, Spouse
    # The employee information is located in employees.csv
    with open('employees.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            id, name, dept, gender, country, salary, age, spouse = row

            db.add("name", name, record=int(id))
            db.add("dept", dept, record=int(id))
            db.add("gender", gender, record=int(id))
            db.add("country", country, record=int(id))
            db.add("salary", int(salary), record=int(id))
            db.add("age", int(age), record=int(id))
            db.add("spouse", spouse, record=int(id))

    return db
 

# Create the example database
db = create_db()

# Create our query generator
generator = Generator()

while True:
   # Accept a command input
   command_input = input("\nEnter a natural language question or command: ")

   # Create the concourse generation command
   command = generator.generate(command_input)

   # Ensure a valid command
   if not command:
       print ("Sorry, I did not understand that. Please try again")
   else:
       # SPECIAL CASE:
       # The find command uses kwargs so we need a ** to unpack
       if command[0] == 'find':
           result = getattr(db, command[0])(**command[1])
       else:
           result = getattr(db, command[0])(*command[1])

       # Print the results
       print ("Answer: ", end="")
       print (result)



