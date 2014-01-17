'''
read.py 
Alexander Patel - alexanderpatel@college.harvard.edu
January 13, 2014
'''

import sys, csv
from models import Student, Seminar

'''
build student body from csv file specified by command line argument
'''
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

'''
build set of seminars from csv file 
'''
def read_seminars(): pass