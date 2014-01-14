'''
models.py
Alexander Patel - alexanderpatel@college.harvard.edu
January 13, 2014
'''
class Student:
	def __init__(self, first, last, grade, advisor, *choices):
		self.first = first
		self.last = last
		self.grade = grade
		self.advisor = advisor
		self.choices = [choice for choice in choices]

	def __str__(self):
		return "{0}, {1}, Grade: {2}".format(self.first, self.last, self.grade)

class Seminar:
	def __init__(self, title, cap=None, restriction=None):
		self.title = title
		# size capacity of seminar
		self.cap = cap
		self.restriction = restriction
		self.students = []

	def __str__(self):
		return self.title