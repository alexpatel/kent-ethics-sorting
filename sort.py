#!/usr/bin/python

'''
sort.py 
Alexander Patel - alexanderpatel@college.harvard.edu
January 13, 2014
'''

import csv, sys
from models import Student, Seminar

## configuration variables

# optimal seminar size 
opt_size = 15

# maximum seminar size
max_size = 20

# percentage weight for age
# e.g. age_distro = 10 --> seniors are 10% more likely to receive 
# first choice than juniors, juniors 10% more likely than sophomores, etc.
age_distro = 0

## build students from csv file specified by command line argument
def read_students():
	students = []
	f = open(sys.argv[1], 'rb') 
	try:
		read = csv.reader(f)
		for row in read:
			name = row[0].split().replace(',', '')
			grade = row[1]
			advisor = row[2]
			choices = row[3:]
			student = Student(name[1], name[0], grade, advisor, choices)
			students.append(student)
	finally:
		f.close()
		return students

## build seminars from csv file specified by command line argument
## no idea how this data is being collected - default to numerical identifies (e.g. 0 - 50)
def read_seminars():
	seminars = []

