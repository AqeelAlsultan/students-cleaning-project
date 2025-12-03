Students Cleaning Project

This is a small learning project created to practice Python basics and simple data cleaning.

This project reads a CSV file with student names and grades, cleans the data, and creates a clean CSV file and a text report.
It is a simple example of data cleaning and basic data analysis using Python.


---

Project Overview

The program does the following:

Reads raw student data from students_raw.csv

Cleans the data (removes invalid rows)

Converts grades to numbers

Fixes extra spaces

Removes invalid names

Keeps the highest grade if a name appears more than once

Calculates basic statistics

Saves a clean CSV file

Writes a text report with the results



---

Files

File	Description

students_raw.csv	Raw input data
main.py	Main Python script
students_clean.csv	Clean output data (generated)
report.txt	Final analysis report (generated)
README.md	Project description



---

How to Run

1. Install Python 3


2. Place all files in the same folder


3. Run this command:



python main.py

After running the script:

students_clean.csv will contain the cleaned data

report.txt will contain the analysis report



---

Data Cleaning Rules

The script removes or fixes the following:

Names with numbers or invalid characters

Grades that are not numbers

Grades outside the range 0 to 100

Extra spaces in the grade field

Duplicate names (keeps only the highest grade)



---

Analysis Performed

The program calculates:

Number of clean students

Average grade

Highest grade and student name

Lowest grade and student name

Number of passed students

Number of failed students



---

Learning Purpose

This project was created to practice:

Reading files

Writing files

Using dictionaries

Loops and nested loops

Error handling (try / except)

Data cleaning

Basic statistics


It is a simple introduction to data preprocessing, which is an important step in machine learning.


---

Possible Future Improvements

Use pandas instead of manual loops

Add charts or graphs

Organize the code into functions

Build a menu-based program



---

Author

Aqeel Alsultan
