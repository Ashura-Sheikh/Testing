#import csv

class User():

    def __init__(self, Name, Age, Email):
        self.name = Name
        self.age = Age
        self.email = Email


my_file = open("Data1.txt", "w")





while (True):
  Name = input("Enter Name: ")
  Age = input("Enter Age: ")
  Email = input("Enter E-mail Address: ")

  my_file.write[Name]
  my_file.write[Age]
  my_file.write[Email]

  my_file.close()
