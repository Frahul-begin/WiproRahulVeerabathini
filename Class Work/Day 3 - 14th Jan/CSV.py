import csv

with open("student.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID","Name","Age"])
    writer.writerow(["996","Rahul","25"])
    writer.writerow(["997","Rohit","27"])
    writer.writerow(["998","Roshan","28"])