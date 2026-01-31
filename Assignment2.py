print("Python Basic Conditinal Statements.")
#Input from user in data type through variable.
Salary = float(input("what is your salary: " )) 
Years_of_Service =float(input("Enter your years of service: "))
if Years_of_Service > 5:     #Condition check
    bonus = Salary* (5/100)  #calculate bonus
    print("You are eligible for bonus") 
    print(f"Bonus Amount:{bonus}") 
else:
    print("You are not eligible for bonus")
#Age-Checker For Vote
age =int(input("what is your age: "))
if age > 17:
    print("You are eligible for Vote.")
else:
    print("you are not eligible for vote.")
#Even/odd Number Check
num =int(input("Enter your number: "))    #number from user
if num % 2 == 0:
  print("Given number is Even")
else:
    print("Given number is odd")
# check Division by 7
Num = int(input("Enter Your Number: "))
if Num % 7 ==0:
    print(f"{Num} is Divisible by 7")
else:
    print(f"{Num} is Not divisible by 7")
   # mulitiply by 5
num=int(input("Enter Number: "))
if num * 5:
    print("Hell0")
else:
    print("bye")
    #Display Last digit of Number
Num1 =int(input("Enter your Number: "))
digit = Num1 % 10
print(f"The Last digit of {Num1} is {digit}")
#Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
length=float(input("Enter the length of a rectangle: "))
breadth=float(input("Enter the breadth of a rectangle: "))
if length == breadth:
    print("It is square")
else:
    print("It is rectangle")
#Take two int values from user and print greatest among them.
value1=int(input("Enter First Value: "))
value2=int(input("Enter Second Value: "))
if value1 > value2:
    print(f"The Greatest Number is {value1}")
else:
    print(f"The Greatest number is {value2}")
  #shop discount 10%
quantity = int(input("How many quantity do you require: "))
unit_price = 100
cost_quantity = quantity * unit_price #cost without discount
if quantity > 1000:  #Discount Condition
    discount = (cost_quantity*10)/100  
    total_cost = cost_quantity - discount #cost with discount
    print("you will get 10% Discount")
    print(f"your total cost to pay is {total_cost}") #final amount
else:
     print("sorry you will not get any discount")
#School Grade system
English=float(input("What's your English Marks: "))
Math=float(input("What's your Math Marks:"))
Science=float(input("What's your Science Marks:"))
Total_marks= 300
Obtained_marks = English + Math + Science
Percentage = (Obtained_marks/Total_marks)*100
print(f"Your percentage is {Percentage}")
if Percentage < 25:
    print("Your grade is F")
elif Percentage >= 25 and  Percentage < 45:
  print("Your grade is E")
elif Percentage >= 45 and Percentage < 50:
    print("Your grade is D")
elif Percentage >= 50 and Percentage < 60:
    print("Your grade is C")
elif Percentage >= 60 and Percentage < 80:
    print("Your grade is B")
else: # <80 Percentage
    print("Your grade is A")
#class Attendance
classes_held=int(input("Number of classes held: "))
classes_attended=int(input("Number of classes Attended: "))
medical_cause=input("Do you have medical cause? Y/N: ")
class_percentage = (classes_attended/classes_held)*100
if class_percentage >= 75 or medical_cause.upper == "Y":
    print("student is allowed t0 sit in exam")
else:
    print("Student is not allowed to sit in exam")
#Leap Year
year=int(input("Enter a year: "))
if year % 4 == 0 and year % 400 == 0:
    print("it is a leap Year") 
else:
    print("it is not a leap Year")
#Place of service
age=int(input("Enter your age: "))
gender=(input("What's your Gender? M/F:  ")).upper()
Marital_Status=(input("Are you Married? Y/N:")).upper()
if gender == "F":
    print("She will work only in Urban Areas.")
elif gender =="M" and 20 <= age <= 40:
    print("He may work anywhere")
elif gender == "M" and 40 < age <= 60:
    print("He will work only in urban areas.")
else:
    print("Error")
#Calculate Electricity Bill
unit=float(input("Enter the number of units consumed: "))
bill=0          #initializa amount of bill
if unit <= 100: #condition for 100 unit no charge
    bill=0 
elif unit <= 300: #condition for 200 unit charge Rs 5 per unit
    bill = (unit - 100)*5
else:
    bill=(unit-200)*10
#condition for 300 unit charge Rs 10 per unit
print(f"Your total Bill is {bill}")
#younger and oldest check
age1=int(input("Enter age of first person: "))
age2=int(input("Enter age of Second person: "))
age3=int(input("Enter age of third person: "))
#finding oldest and youngest using max() and min()
oldest = max(age1, age2, age3)
youngest = min(age1, age2, age3)
#result
print(f"the oldest age is{oldest}")
print(f"the youngest age is {youngest}")

