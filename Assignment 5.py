""" Question:1 """
number = [12,5,6,7,12,8,9,4,1] #create List of number
print ("All Number in the list: ") 
total_sum = 0   # Initializing a variable to store the sum

for i in number: #loop for list
   print (i) #print number list
   total_sum = total_sum + i  # add each number to total
print(f"Sum of All Number: {total_sum}")
#printing only even number:
for i in number:
   if i % 2 == 0: #condition check
     print(f"Even Number {i} ", end="" )
"""QUESTION 2: Dictionary Basics """
students = {
   "Name": "Iqra",
   "Age":   19,
   "Course": "English Language",
   "Marks": [65, 55, 75]  #dictonary contain list
}
for key, value in students.items():  
   print(f"{key}, {value}") # Print all keys and values together:

#calculate average of the marks

total = 0   # Start total from 0
for c in students["Marks"]: 
   total = total + c  #Add each mark to total
   average_marks = total/len(students["Marks"]) #average formula
print(f"average marks: {average_marks}")

# Check if student passed or failed
if average_marks >=50: #apply condition to check pass and failed
   print("student is passed")
else:
   print("Student failed")

""" QUESTION 3: List of Dictionaries """

#list of dictionaries for employees
employees=[
  {"Name": "Fawad","Department": "Science","Salary": 45000},
  {"Name": "Junaid","Department": "Medical","Salary": 65000}, 
  {"Name": "Sami","Department": "English","Salary": 35000} 
   ]

for m in employees:  # Loop through each employee
   print(f"Name: {m["Name"]}")
   print(f"Department: {m["Department"]}")
   print(f"Salary: {m["Salary"]}\n")

# employee with the highest salary.
highest_salary = 0
highest_employees = ""
for m in employees:
 if m["Salary"] > highest_salary:
        highest_salary = m["Salary"]
        highest_employee =m["Name"]
print(f"Employe {highest_employee} with the Highest Salary: {highest_salary}")  

# Calculate total salary expense  
total_salary = 0
for m in employees:
   total_salary = total_salary + m["Salary"]
print(f"Total Salary Expense: {total_salary}")

""" QUESTION 4: While Loop with User Input """

database = [] # Create an empty list to store numbers 
num = int(input("Please Enter any Number (-1 to stop): "))
# While loop runs until user enters -1
while num != -1:
   database.append(num) # Store number in empty list
   num = int(input("Please Enter any Number (-1 to stop): ")) 
# After loop ends
print(f"Number List: {database}")
if len(database) > 0:
    print("Largest number:", max(database))
    print("Smallest number:", min(database))
else:
    print("No numbers were entered.")

""" QUESTION 5: Word Frequency Counter """

word = input("Please Enter a Sentence: ").split()
word_count = {} # Created empty dictionary to store word counts
# Count each word
for w in word: 
   if w in word_count: 
      word_count[w] += 1 # increase count
   else:
      word_count[w] = 1   # add new word with count 1
# Print word frequency clearly
print("Word Frequency:")
for w, count in word_count.items():
    print(f"{w}: {count}")
    
""" QUESTION 6: Nested Loops - Multiplication Table """
# Outer loop: rows
for i in range(1, 6):      # Row ke numbers (1,2,3,4,5)
    # Inner loop: columns
    for j in range(1, 6):  #Column ke numbers (1,2,3,4,5)
        print(i * j, end=" ")  # multiply and print on same line
    print()  # new line after each row











