#Q.1- Write a python script to create a databse of students named Students
import pymongo
client=pymongo.MongoClient()
database=client['Students']
collection=database['student']
#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
for i in range(10):
    try:
        name = input("Enter name: ") 
        marks = int(input('Enter  Marks: '))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry')
            i=i-1
    except  ValueError as msg:
        print(msg)
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
for i in range(10):
    try:
        name = input("Enter name: ") 
        marks = int(input('Enter  Marks: '))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry')
            i=i-1
        else:
            collection.insert_one({'Name':name,'Marks':marks})  
            i=i+1
    except  ValueError as msg:
        print(msg)
#Q.4- Print the names of all the students who scored more than 80 marks.
db=collection.find({"Marks":{"$gt":80}})
for data in db:
    print(data)
