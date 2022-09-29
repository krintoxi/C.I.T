

class Printer():
	def __init__(self, verbosity, color):
		self.verbosity = verbosity
		self.color = color

		self.colors = {
			1: 'yellow',
			2: 'cyan',
			3: 'blue',
			4: 'red',
			5: 'white'
		}

	def print(self, msg, verbosity_level=0, line_ending='\n'):
		if verbosity_level <= self.verbosity:

			if verbosity_level in self.colors:
				color =  self.colors[verbosity_level]
			else:
				color = 'normal'

			print(self.color.format(msg, color, bold=False), end=line_ending)


