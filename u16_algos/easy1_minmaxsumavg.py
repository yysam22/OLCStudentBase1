
# Write a program to find the largest and smallest numbers in 
# a list using 
# 1a. max()
# 1b. min()
# 1c. without using max()
# 1d. without using min()
# 1e. find the sum of all the numbers
# 1f. find the count of items in the list
# 1g. find the average of all the numbers
# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
#          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
#          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
#          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# ####################################################
# # Answer for Question 1a here
# maxnum = max(list1)
# print(f"The biggest number is {maxnum}")

# ####################################################
# # Answer for Question 1b here
# minnum = min(list1)
# print(f"The smallest number is {minnum}")

# ####################################################
# # Answer for Question 1c here
# maxnum2 = list1[0]
# for i in list1:
#     if i > maxnum2:
#         maxnum2 = i
# print(f"The biggest number is {maxnum2}")

# ####################################################
# # Answer for Question 1d here
# minnum2 = list1[0]
# for i in list1:
#     if i < minnum2:
#         minnum2 = i
# print(f"The smallest number is {minnum2}")

# ####################################################
# # 1e. find the sum of all the numbers
# sumnum = 0
# for i in list1:
#     sumnum = sumnum + i

# print(f"The sum of all the numbers is {sumnum}")

# ####################################################
# # 1f. find the count of items in the list
# print(len(list1))

# count = 0
# for i in list1:
#     count = count + 1

# print(f"The count of all the numbers is {count}")

# ####################################################
# # 1g. find the average of all the numbers
# average = sumnum / count # OR
# average = sumnum / len(list1)

# print(f"The average of all the numbers is {average}")

######################################################
# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
#####################################################
swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 32.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# Answer for Question 2 here

fasttime= swim_times[0]
slowtime= swim_times[0]
count=1

fastindex = 0
slowindex = 0

# for time in swim_times:
#     if time<fasttime:
#         fasttime=time
#         # count=count+1
#         fastindex = count
#     if time > slowtime:
#         slowtime=time
#         # count=count+1
#         slowindex = count
    
#     count += 1

# print(f"The fastest timing is {fasttime},lane{fastindex}")
# print(f"The slowest timing is {slowtime},lane{slowindex}")
    





########################################################
# Question 3:
# The student council organised a charity fundraising event. 
# The amount collected from each class is stored in the dictionary below. 
# Identify the class that raised the highest and lowest amounts. 
# Print out the class names and their respective contribution amounts.
########################################################
donations = {
    'Class 1A': 320, 'Class 1B': 480, 'Class 1C': 290, 'Class 1D': 375,
    'Class 1G': 450, 'Class 1H': 530, 'Class 2C': 470, 'Class 3D': 310,
    'Class 4E': 415, 'Class 5F': 390
}
# Answer for Question 3 here
# highest=0
# lowest=9999

# highclass=""
# lowclass=""

# for thisclass,amount in donations.items():
#     if amount>highest:
#         highest=amount
#         highclass=thisclass
#     if amount< lowest:
#         lowest=amount
#         lowclass=thisclass
    

# print(f"The highest donation is {highest} donated by {highclass}")
# print(f"The lowest donation is {lowest} donated by {lowclass}")

#################################################################
# Question 4: 
# A bookstore keeps track of their sales figures each day 
# for the month of June. The sales for the 30 days are provided 
# in the list below. Find the days with the highest and lowest sales. 
# Assume that the first item in the list corresponds to Day 1.

# Find the total sales figure for the month
# Find the average sales rounded to 2 decimal points
#################################################################
daily_sales = [120, 98, 135, 105, 150, 112, 80, 130, 95, 110, 
               102, 85, 140, 99, 123, 145, 78, 90, 136, 145, 
               132, 108, 75, 88, 142, 115, 97, 121, 89, 100]
# Answer for Question 4 here
sumnum=0
for m in daily_sales:
    sumnum=sumnum+m
print(f{sumnum})





##################################################################
# Question 5: 
# Hourly temperature measurements (°C) for a specific day are given below. 
# Write Python code to determine the highest and lowest temperatures, 
# along with the corresponding hour of measurement. 
# (First measurement at index 0 corresponds to midnight, 
#  and each subsequent value is measured hourly.)

# Find the average temperature for this day.
##################################################################
hourly_temperatures = [26.4, 25.9, 25.1, 24.6, 24.2, 23.8, 24.5, 25.6, 
                       27.3, 29.0, 30.5, 31.2, 32.0, 33.1, 32.8, 31.6,
                       30.8, 29.4, 28.1, 27.5, 27.0, 26.8, 26.0, 25.7]
# Answer for Question 5 here




#################################################################
# Question 6:
# A mathematics teacher recorded the final exam scores (out of 100) of 
# students in the dictionary below. 
# Write Python code to identify the student 
# with the highest and lowest exam scores, and print their names and scores.

# Find the average score rounded to 2 decimal points
# Create a dictionary called failed_students
# add the names and score of students who failed (<50) into this dictionary.
# loop through the failed_students and print out the names and scores like below
# "Esther scored 9 and failed. Go to the Principal's Office."
#################################################################
exam_scores = {
    'Ali': 88, 'Benny': 75, 'Chloe': 92, 'Diana': 85,
    'Ethan': 78, 'Farid': 81, 'Grace': 66, 'Haziq': 94,
    'Ivy': 71, 'Jun': 88, 'Ullas':45, 'Josephine':98,
    'Sor Lang': 23, 'Jimmy': 5, 'Borui': 78, 'Esther': 9}
# Answer for Question 6 here
