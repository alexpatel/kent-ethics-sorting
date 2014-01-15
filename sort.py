#!/usr/bin/python

'''
sort.py 
Alexander Patel - alexanderpatel@college.harvard.edu
January 13, 2014
'''

import random, sys, csv

'''
config vars for testing
'''
num_sems = 40
num_students = 500
num_runs = 1000
num_ranks = 5 # number of seminars ranked by each student
sem_size = 15

'''
some data models
'''
# each student has name, grade, advisor, and a set of ranked seminars
class Student:
	def __init__(self, first, last, grade, advisor, choices):
		self.first = first
		self.last = last
		self.grade = grade
		self.advisor = advisor
		self.choices = choices

	def __str__(self):
		return "{0}, {1}, Grade: {2}".format(self.first, self.last, self.grade)

	def choices(self):
		return self.choices

	def assign(self, seminar):
		self.seminar = seminar
		seminar.add_student(self)

	def set_assigned_rank(self, assigned_rank):
		self.assigned_rank = assigned_rank

# each seminar has 
class Seminar:
	def __init__(self, title, cap=None):
		self.title = title
		# size capacity of seminar
		self.cap = cap
		self.students = []

	def __str__(self):
		return self.title

	def students(self):
		return self.students

	def add_student(self, student):
		self.students[len(self.students):] = student

	def is_full(self):
		return len(self.students) == self.cap if self.cap else len(self.students) == sem_size

	def get_age_distro(self):
		age_sum = 0
		for student in self.students:
			age_sum += student.grade - 8 # so that ages are 1, 2, 3, 
		return abs(float(age_sum - len(self.students)) /len(self.students))

# object to store stats for any given sample Run
class Run():
	def __init__(self, seed, seminars, students):
		self.seminars = seminars
		self.students = students
		self.seed = seed

	# average rank assigned
	def get_choice_distro(self):
		rank_sum = 0
		for student in self.students:
			rank_sum += student.assigned_rank # should replace with lambda
		return float(rank_sum) / len(self.students)

	# average age distribution
	# returns: % diff. between run's age distribution and optimal age distribution (equal)
	def get_age_distro(self):
		distro_sum = 0
		for seminar in self.seminars:
			distro_sum += seminar.get_age_distro()
		return float(distro_sum) / len(self.seminars)

'''
sort students into seminars	
return: run (run with optimal age and choice distribution)
'''
def sort(students, seminars):
	runs = []
	for i in range(num_runs):
		# create unique rand seed
		random.seed (i) 
		random.shuffle(students)
		# assign students to seminars
		for student in students:
			rank = 1
			seminar = student.choices[rank]
			# assign student to highest ranked seminar with an open seat
			while seminar.is_full():
				rank += 1
				# short end of the stick
				if rank > num_ranks:
					seminar = seminars[random.randint(len(seminars))]
					rank = -1
				else:
					seminar = student.choices[rank]
			# assign student to seminar
			student.assign(seminar)
			student.set_assigned_rank(rank)
		run = Run(i, seminars, students) # pass by value, so passing updated seminars and students should be o.k.
		# add run to set of runs
		runs[len(runs):] = run

	# figure out optimal run
	best_run = None
	best_choice_distro = sys.maxint
	best_age_distro = sys.maxint

	for run in runs:
		choice_distro = run.get_choice_distro() 
		age_distro = run.get_age_distro()
		if  age_distro < best_age_distro and choice_distro < best_choice_distro:
			best_age_distro = age_distro
			best_choice_distro = choice_distro
			best_run = run

	return best_run

'''
create sample student body
'''
def sample_students(seminars):
	students = []
	for i in range(num_students):
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
seminars = [Seminar(str(i)) for i in range(num_sems)] 
# create clean copy of seminar
sems_cp = seminars[:]
students = sample_students(sems_cp)
sort(students, sems_cp)

'''
build students from csv file specified by command line argument
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
