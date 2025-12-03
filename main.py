# Data Cleanup

students = {}

with open("students_raw.csv", "r") as file:
  lines = file.readlines()
  for data in lines [1:]:
    name , grade = data.strip().split(",")
    grade = grade.strip()
    grade = grade.replace(" ", "")
    if not all(part.isalpha () for part in name.split ()):
      continue 

    try:
      grade = round (float(grade),2)
      if 0 <= grade <= 100 and name not in students :
        students [name] = float(grade)
      elif name in students:
        if grade > students[name]:
          students [name] = float(grade)
        else:
          continue 

    except:
      continue 

# Analysis

students_avg = 0

for grade in students.values():
 students_avg += grade

students_num = len(students)

students_avg = round(students_avg / students_num , 2)


high_grade = 0
top_student = ""
low_grade = 999
lowest_student = ""

for name , grade in students.items():
 if grade > high_grade:
  high_grade = grade
  top_student = name
 elif grade < low_grade:
  low_grade = grade
  lowest_student = name


passed = 0
failed = 0

for grade in students.values():
 if grade >= 60 :
  passed += 1
 else:
  failed += 1

# Write a new csv file 

with open("students_clean.csv", "w") as file:
 file.write("name,grade\n")
 for name , grade in students.items():
  file.write(f"{name},{grade}\n")

# Report

with open("report.txt" , "w") as file:
  file.write(f"Students Report\n...............\nTotal clean students : {students_num}\nAverage grade: {students_avg}\n\nTop students: {top_student} with {high_grade}\nLowest students: {lowest_student} with {low_grade}\n\nPassed: {passed} students\nFailed: {failed} students")
