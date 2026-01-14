import xml.etree.ElementTree as ET

tree = ET.parse("student.xml")
root = tree.getroot()

for student in root.findall("student"):
    id = student.find("id").text
    name = student.find("name").text
    marks = student.find("marks").text
    print(id, name, marks)

root = ET.Element("employe")
emp1 = ET.SubElement(root, "emp")
ET.SubElement(emp1, "Id").text = "101"
ET.SubElement(emp1, "Name").text = "Rahul"
ET.SubElement(emp1, "Salary").text = "38000"

emp2 = ET.SubElement(root, "emp")
ET.SubElement(emp2, "Id").text = "102"
ET.SubElement(emp2, "Name").text = "Ravi"
ET.SubElement(emp2, "Salary").text = "25000"

tree = ET.ElementTree(root)
tree.write("employe.xml")
print("xml file written Successfully")