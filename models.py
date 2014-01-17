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
		seminar.add_student(self) # update seminar object, as well

	def set_assigned_rank(self, assigned_rank):
		self.assigned_rank = assigned_rank

# Seminar class representation
# to do: cap, age restriction
class Seminar:
	def __init__(self, title):
		self.title = title
		self.students = []

	def __str__(self):
		return self.title

	def add_student(self, student):
		self.students[len(self.students):] = student

	def is_full(self, sem_size):
		return len(self.students) == self.cap if self.cap else len(self.students) == sem_size

	# determines age distribution of seminar
	# 
	def get_age_distro(self):
		# figure out how many students per grade ought to be in seminar
		size = len(self.students)  # we'll round the size up to be divisible by four
		while size % 4 != 0:
			size += 1
		opt_score = 0 
		# let's assign each grade a number (1 - 4) 
		# we then figure out the optimal score for a seminar of this size (with an even grade distribution)
		for i in range(4):
			opt_score += i * size / 4 # 

		# now we determine the score of this particular seminar
		score = 0
		for student in self.students:
			if student.grade == 9: score += 1  # python switch statements?
			if student.grade == 10: score += 2 
			if student.grade == 11: score += 3 
			if student.grade == 12: score += 4 

		# return percent difference between seminar's age score and optimal score
		return float(abs( opt_score - score )) / opt_score

	# how did the students in this seminar rank this seminar in their choices?
	def get_avg_rank(self):
		rank_sum = 0
		for student in self.students:
			rank_sum += student.assigned_rank
		return float(rank_sum) / len(self.students)

# object to store stats for any given sample Run
class Run:
	def __init__(self, seed, seminars, students):
		self.seminars = seminars
		self.students = students
		self.seed = seed

	# average rank assigned
	# the closer to 1, the better
	def get_avg_rank(self):
		rank_sum = 0
		for seminar in self.seminars:
			rank_sum += seminar.get_avg_rank()
		return float(rank_sum) / len(self.seminars)

	# average age distribution
	# returns: % diff. between run's age distribution and optimal age distribution (equal)
	# the closer to 0, the better
	def get_age_distro(self):
		distro_sum = 0
		for seminar in self.seminars:
			distro_sum += seminar.get_age_distro()
		return float(distro_sum) / len(self.seminars)

	# heuristic for figuring out how good a given run is
	# the lower, the better
	def get_score(self):
		return self.get_age_distro() / self.get_avg_rank()
