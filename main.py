# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split() # a list needs to be separated by commas
for n in range(0, len(student_heights)):
  student_heights[n]  = int(student_heights[n])# to make it a number and added to a list
            #     ^ to create a list
# 🚨 Don't change the code above 👆



#Write your code below this row 👇
total_height = 0
for height in student_heights:
  total_height = total_height + height
print(total_height)

number_of_students= 0
for student in student_heights:
  number_of_students = number_of_students + 1
print(number_of_students)

average = round(total_height / number_of_students)  
print(average)






# t
# for height in student_heights:
#  total_height = total_height + height # OR total_height += heigh

# total_students = 0
# for student in student_heights:
#   total_students = total_students + 1


# average =  round(total_height / total_students)
# print(total_students)
# print(total_height)
# print (average)
   



# #alternative:
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_otal_height = 0height)
  



