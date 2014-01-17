#!/usr/bin/python

'''
sort.py 
Alexander Patel - alexanderpatel@college.harvard.edu
January 13, 2014
'''

import random, sys, csv
from models import Student, Seminar, Run
from read import read_students, read_seminars

'''
config vars for testing
'''
NUM_SEMS = 40
NUM_STUDENTS = 500
NUM_RUNS = 1000
NUM_RANKS = 5 # number of seminars ranked by each student
SEM_SIZE = 15


'''
sort students into seminars	
returns optimal run (i.e. sorted seminars and students)
'''
def sort(students, seminars):
	runs = []
	for i in range(NUM_RUNS):
		# create unique rand seed and shuffle student assignment order
		random.seed (i) 
		random.shuffle(students)
		# assign students to seminars
		for student in students:
			rank = 1
			seminar = student.choices[rank]
			# assign student to highest ranked seminar with an open seat
			while seminar.is_full(SEM_SIZE):
				rank += 1
				# short end of the stick - assign to random seminar
				if rank > NUM_RANKS:
					rank = -1
					seminar = seminars[random.randint(len(seminars))]
				else:
					seminar = student.choices[rank]
			# assign student to seminar
			student.assign(seminar)
			student.set_assigned_rank(rank)
		run = Run(i, seminars, students) # pass by value, so passing updated seminars and students should be o.k.
		# add run to set of runs
		runs[len(runs):] = run

	return best_run(runs)

'''
given a set of test traversals (runs), figure out the best way of traversing student graph
'''
def best_run(runs):
	best_run = None
	best_score = sys.maxint # arbitrary - just a big number
	for run in runs:
		if run.get_score() < best_score:
			best_score = run.get_score()
			best_run = run
	return best_run

'''
create sample student body
'''
def sample_students(seminars):
	students = []
	for i in range(NUM_STUDENTS):
		 # shuffle seminars to simulate ranking
		random.shuffle(seminars)
		# construct student 'i i' with random seminar ranks
		student = Student(str(i), str(i), random.randint(1,4), 'a', seminars) 
		# add student to student body
		students[len(students):] = student 
	return students

''' 
test the algo with some sample data
'''
# create seminars
seminars = [Seminar(str(i)) for i in range(NUM_SEMS)] 
# create clean copy of seminar
sems_cp = seminars[:]
students = sample_students(sems_cp)
sort(students, sems_cp)