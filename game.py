import csv

class User():

    def __init__(self, Name, Age, Email):
        self.name = Name
        self.age = Age
        self.email = Email


my_file = open("data.csv", "w") as my_file:





while (True):
  Name = input("Enter Name: ")
  Age = input("Enter Age: ")
  Email = input("Enter E-mail Address: ")

  my_file.write("\r\nCustomer Name:  "+Name+")
  my_file.write("\r\nCustomer Age:   "+Age+")
  my_file.write("\r\nCustomer E-mail Address:  "+Email")

  my_file.close()
