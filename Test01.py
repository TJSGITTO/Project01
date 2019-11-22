#populate a list of students
student_names = ["Mark","Katarina","Jessica","Connor","Ian","Natalie", "Brad","Amy","Sarah","Kelly"]
Building_materials = ["Studs", "Sheetrock", "Fastners", "Doors", "Lights"]

#Adding a name to the list

#student_names.append("Homer")

#Printing the list using for loop
#x=0
#for name in student_names:
#    print (student_names [x])
#    x+=1

#Printing the list using a for loop
#for name in student_names:
#    print("student_name is {0}".format(name))

#Printing the list using format statement

#x = 0
#for materials in Building_materials:
#   print("The building material is {0}".format(materials))

#Printing the list using for loop and the Range statement   

#x=0
#for index in range(8):
#    print("The name of the", x, "student is ",student_names[x])
#    x += 1

#Using For and Break statement
#for m in Building_materials:
#    if m == "Sheetrock":
#        print ("Found it at")
#        break
#    print (m)

# Using Dictionaries
Student = {
    "First_Name": "Nick",
    "Last_Name": "Sudelski", 
    "Student_ID": 5422
}

try:
    Family_Name = Student["Name"]
except KeyError:
    print("Error found in last name")
except TypeError:
    print("this is a good code!")  
except:
    print("Unknown Error")
