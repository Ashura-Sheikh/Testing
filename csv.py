import csv

with open('bored.csv', 'w', newline='') as f:
    fieldnames = ['column1' ,'column2', 'column3', 'column4']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)

    thewriter.writeheader()
    thewriter.writerow({'column1': "First Name",'column2': "Last Name",'column3': "D.O.B"})
