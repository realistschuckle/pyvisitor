from __future__ import print_function
import sys
import os

# Put the path to the visitor module on the search path
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if not path in sys.path:
  sys.path.insert(1, path)

import visitor

class Person(object):
	def __init__(self, name):
		self.name = name
		self.deps = []

	def add_dependent(self, dep):	
		self.deps.append(dep);

	def accept(self, visitor):
		visitor.visit(self)


class Pet(object):
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

	def accept(self, visitor):
		visitor.visit(self)


class DescendantsVisitor(object):
	def __init__(self):
		self.level = 0

	@visitor.on('member')
	def visit(self, member):
		pass

	@visitor.when(Person)
	def visit(self, member):
		self.write_padding()
		print('-', member.name)
		self.level += 1
		for dep in member.deps:
			dep.accept(self)
		self.level -= 1

	@visitor.when(Pet)
	def visit(self, member):
		self.write_padding()
		print('-', member.name, 'a', member.breed)

	def write_padding(self):
		for i in range(self.level):
			sys.stdout.write('  ')