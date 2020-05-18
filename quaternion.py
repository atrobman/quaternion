from math import floor, sqrt, cos, sin, acos
from math import exp as math_exp
from math import log as math_ln

class Quaternion:

	def __init__(self, a=0, b=0, c=0, d=0):
		"""Q(a,b,c,d) = a + bi + cj + dk"""
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def mul(self, comp):

		if type(comp) is Quaternion:
			""" Distributing [a1+b1*i+c1*j+d1*k] * [a2+b2*i+c2*j+d2*k] =
				a1*a2 + a1*b2*i + a1*c2*j + a1*d2*k +
				b1*a2*i + b1*b2*i^2 + b1*c2*i*j + b1*d2*i*k +
				c1*a2*j + c1*b2*j*i + c1*c2*j^2 + c1*d2*j*k +
				d1*a2*k + d1*b2*k*i + d1*b2*j*k + d1*d2*k^2 =

				a1*a2 - b1*b2 - c1*c2 - d1*d2 +
			(a1*b2 + b1*a2 + c1*d2 - d1*c2) * i +
			(a1*c2 - b1*d2 + c1*a2 + d1*b2) * j +
			(a1*d2 + b1*c2 - c1*b2 + d1*a2) * k
			"""
			na = self.a * comp.a - self.b * comp.b - self.c * comp.c - self.d * comp.d
			nb = self.a * comp.b + self.b * comp.a + self.c * comp.d - self.d * comp.c
			nc = self.a * comp.c - self.b * comp.d + self.c * comp.a + self.d * comp.b
			nd = self.a * comp.d + self.b * comp.c - self.c * comp.b + self.d * comp.a

			return Quaternion(na, nb, nc, nd)
		
		elif type(comp) is int or type(comp) is float:
			return Quaternion(self.a * comp, self.b * comp, self.c * comp, self.d * comp)
		
		else:
			raise TypeError(f'Expected type={type(self)} but recieved type={type(comp)}')

	def add(self, comp):

		if type(comp) is Quaternion:
			na = self.a + comp.a
			nb = self.b + comp.b
			nc = self.c + comp.c
			nd = self.d + comp.d

			return Quaternion(na, nb, nc, nd)
		
		elif type(comp) is int or type(comp) is float:
			return Quaternion(self.a + comp, self.b, self.c, self.d)
		
		else:
			raise TypeError(f'Expected type={type(self)} but recieved type={type(comp)}')

	def sub(self, comp):

		if type(comp) is Quaternion:
			na = self.a - comp.a
			nb = self.b - comp.b
			nc = self.c - comp.c
			nd = self.d - comp.d

			return Quaternion(na, nb, nc, nd)

		elif type(comp) is int or type(comp) is float:
			return Quaternion(self.a - comp, self.b, self.c, self.d)
		
		else:
			raise TypeError(f'Expected type={type(self)} but recieved type={type(comp)}')

	def div(self, comp):

		if type(comp) is Quaternion:
			"""Source: https://www.mathworks.com/help/aerotbx/ug/quatdivide.html"""

			denom = comp.a ** 2 + comp.b ** 2 + comp.c ** 2 + comp.d ** 2

			if denom != 0:
				na = (comp.a * self.a + comp.b * self.b + comp.c * self.c + comp.d * self.d) / denom
				nb = (comp.a * self.b - comp.b * self.a - comp.c * self.d + comp.d * self.c) / denom
				nc = (comp.a * self.c + comp.b * self.d - comp.c * self.a - comp.d * self.b) / denom
				nd = (comp.a * self.d - comp.b * self.c + comp.c * self.b - comp.d * self.a) / denom

				return Quaternion(na, nb, nc, nd)
			else:
				raise ZeroDivisionError("division by zero")
		
		elif type(comp) is int or type(comp) is float:

			if comp != 0:
				return Quaternion(self.a / comp, self.b / comp, self.c / comp, self.d / comp)
			else:
				raise ZeroDivisionError("division by zero")
		
		else:
			raise TypeError(f'Expected type={type(self)} but recieved type={type(comp)}')

	
	def norm(self):
		return sqrt( self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2 )
	
	def conj(self):
		return Quaternion(self.a, -1*self.b, -1*self.c, -1*self.d)
	
	def unit(self):
		return self / self.norm()
	
	def inverse(self):
		return self.conj() / (self.norm() ** 2)

	def exp(self):
		v = Quaternion(0, self.b, self.c, self.d)

		norm_v = v.norm()
		unit_v = v.unit()

		rhs = unit_v * sin(norm_v) + cos(norm_v)

		return  rhs * math_exp(self.a)

	def ln(self):
		v = Quaternion(0, self.b, self.c, self.d)

		return v.unit() * acos(self.a / self.norm()) + math_ln(self.norm())

	def __mul__(self, comp):
		return self.mul(comp)
	
	def __add__(self, comp):
		return self.add(comp)

	def __sub__(self, comp):
		return self.sub(comp)

	def __truediv__(self, comp):
		return self.div(comp)
	
	def __floordiv__(self, comp):
		newQ = self.div(comp)

		newQ.a = floor(newQ.a)
		newQ.b = floor(newQ.b)
		newQ.c = floor(newQ.c)
		newQ.d = floor(newQ.d)

		return newQ

	def __str__(self):
		msg = ""
		if self.a != 0:
			msg += f"{self.a}"
		
		if self.b != 0:
			if msg == "":
				msg += f"{self.b}*i"
			else:
				
				if self.b > 0:
					msg += f" + {self.b}*i"
				else:
					msg += f" - {self.b*-1}*i"

		if self.c != 0:
			if msg == "":
				msg += f"{self.c}*j"
			else:
				
				if self.c > 0:
					msg += f" + {self.c}*j"
				else:
					msg += f" - {self.c*-1}*j"
		
		if self.d != 0:
			if msg == "":
				msg += f"{self.d}*k"
			else:
				
				if self.d > 0:
					msg += f" + {self.d}*k"
				else:
					msg += f" - {self.d*-1}*k"
		
		elif msg == "":
			msg = "0"
		
		return msg

	def __repr__(self):
		return f"Quaternion({self.a}, {self.b}, {self.c}, {self.d})"

	def __bool__(self):
		return (self.a != 0) or (self.b != 0) or (self.c != 0) or (self.d != 0)