'''
models.py - some helper data models
Alexander Patel - alexanderpatel@college.harvard.edu
January 16, 2014
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

# 
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