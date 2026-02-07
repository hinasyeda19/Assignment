
#Alternate_element_List
fruit=input("Please enter the list of fruit and seprated by commas after fruit: ").split(',')
for i in range(len(fruit)*4):
    print(fruit[i % len(fruit)])

#Reverse_element_list:
num=input("Please enter a number list: ")
for i in num[::-1]:
    print(i)
    

#largest_number_in_the_list:
num1=input("Enter a random number list with space: ") #user input
num1=[int(n) for n in num1.split()] # convert to int list
largest = num1[0] #assume first element as largest
for i in num1:
    if i > largest:
     largest = i  # update largest
print("Largest Value is: ", largest)
  
#Rotate element of a list:
fruit = ["Banana", "Apple", "Cherry", "Grapes", "Pear"]
print(fruit)
 #first index move to the second index
fruit.pop(1)
fruit.insert(2, "Apple")
print(fruit)
#second index move to the third index
fruits = ["Banana", "Apple", "Cherry", "Grapes", "Pear"]
fruits.pop(2)
fruits.insert(3, "Cherry")
print(fruits)
#last element move to the first index
fruits.pop()
fruits.insert(0, "Pear")
print(fruits)

#user delete given word
name=input("Enter a name:  ")
delete_letter=input("Enter the letter from your name you want to delete. ")
update_name = name.replace(delete_letter,"")
print("your name is updated", update_name)


#Read a string:
month=int(input("Please Enter a Month (mm): "))
day= int(input("Please Enter a Day (dd): "))
year= int(input("Please Enter a Year (yyyy): "))
month_list = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_name = month_list[month - 1]
print(f"Date is: {month_name} {day} {year}")


#Convert character in capatalize
Sentence = "stop and smell the roses"
print(Sentence.title())  # use title function

# Matrix 
mat1= [
    [2  , 11],
    [5  ,  2],
    [8  ,  3]
     ]

mat2= [
    [7  , 12],
    [9  , 15],
    [10 , 42]
     ]
mat_sum = []

for i in range(len(mat1)):  
   temp = []  
   for j in range(len(mat1[i])):
        temp.append(mat1[i][j] + mat2[i][j])  # element-wise addition
        mat_sum.append(temp)  # append row to matrix sum


# Print matrix sum
print("Matrix Sum: ")
for k in mat_sum:
    print(k)

# print each row sum
row_number = 1
for val in mat_sum:
    print("Sum of row", row_number, "is =", sum(val))
    row_number += 1

# Matrix multiplication
mat1 = [
    [2, 11],
    [5, 2],
    [8, 3]
]

mat2 = [
    [7, 12],
    [9, 15],
    [10, 42]
]

mat3 = []
for i in range(len(mat2[0])):  # for each column in mat2
    new_row = []
    for j in range(len(mat2)):  # for each row in mat2
        new_row.append(mat2[j][i])
    mat3.append(new_row)


mat_multiply = []
for i in range(len(mat1)):  
    row = []
    for j in range(len(mat3)): 
        total = 0
        for k in range(len(mat1[0])): 
            total += mat1[i][k] * mat3[j][k]
        row.append(total)
    mat_multiply.append(row)


print("Mattrix multiplication:")
for row in mat_multiply:
    print(row)