#Q1.
student = {
    "name": "Sadia",
    "age" : 21,
    "course" : "Python Programming",
    "city" : "Karachi"
} 

# Q2. adding and update 
car = {
    "brand": "toyota",
    "model": "corrolla",
    "year": 2019
}
car["color"] = "white"  #adding color in car dictonary
car["year"] = 2022 #updating car dictonary
#Q3.
person ={
    "name": "Ali",
     "age": 22,
     "city": "Karachi"
}
print(person["name"]) # print name
for i in person.keys(): #printing keys using loop.
    print(i)
for i in person.values(): #printing values using loop.
    print(i)
#Q4.frequency
number = [1,2,2,3,3,3,4,4,4,4]
frequency = {} 
for i in number:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)
#Q5. word counter
word = input("Please Enter a sentence: ").split()
frequency = {}
for i in word:
    i = i.lower()
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)
#Q6. Student marks and average:
marks = {
    "math": 80,
    "English": 70,
    "pyhsics" : 90
}

totalmarks = sum(marks.values())
print(f"Total_marks: {totalmarks}")
average_marks = totalmarks/len(marks)
print(f"Average_marks: {average_marks}")
#Q7. Highest Scoring student
students = {
    "Ali": 85,
    "Sara": 90,
    "Ahmed": 78,
    "Zara": 95
 }
highest_score = 0
highest_student = ""

for students, score in students.items():
#Checking if current student's score is higher than the highest_score
    if score > highest_score:
# Update highest_score and highest_student
        highest_score = score
        highest_student = students
print(f"Highest Scoring Student: {highest_student}")
print(f"Marks: {highest_score}")
#Q8. Merge dictonaries:
dict1={
    "a":1,
    "b":2
}
dict2={   
    "c":3,
    "d":4,
}
dict1.update(dict2)
print(dict1)
#Q9 mini project- contact book add 3 conatct serach name ,print phone,or contact not found
contact1={
    "name": "dua",
    "Phone": +923215678
    }
contact2={
    "name": "ali",
    "Phone": +923672739
    }
contact3={
    "name": "zARA",
    "Phone": +922179732
    }
contact_book = [contact1, contact2, contact3] # Create contact book as a list
search_name= input("Enter Name of contact: ").lower() # Ask user for contact to search
found=False # Initialize found flag
for i in contact_book:
    if search_name == i["name"].lower():
        print(f"Phone_Number: {i["Phone"]}")
        found = True
        break  # stop loop once found
if found == False: # If not found after the loop
        print("Contact not Found")
