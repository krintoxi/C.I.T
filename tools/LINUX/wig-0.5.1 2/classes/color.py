import os


class Color(object):
	def __init__(self):
		self.colors = {
			'red': '31',
			'green': '32',
			'yellow': '33',
			'blue': '34',
			'magenta': '35',
			'cyan': '36',
			'normal': None
		}

	def format(self, string, color, bold):
		attr = []
		code = self.colors[color]

		# bail if OS is windows
		# note: cygwin show be detected as 'posix'
		if os.name == 'nt':
			return string

		if not code == None:
			attr = [code]

		if bold: 
			attr.append('1')
		
		return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
