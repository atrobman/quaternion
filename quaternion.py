from math import cos, sin, exp, log, atan2

class Quaternion:

	def __init__(self, a=0, b=0, c=0, d=0):
		"""Q(a,b,c,d) = a + bi + cj + dk"""
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def mul(self, comp):
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
		na = self.a * comp.a - self.b * comp.b - self.c * comp.c - self.d - comp.d
		nb = self.a * comp.b + self.b * comp.a + self.c * comp.d - self.d * comp.c
		nc = self.a * comp.c - self.b * comp.d + self.c * comp.a + self.d * comp.b
		nd = self.a * comp.d + self.b * comp.c - self.c * comp.b + self.d * comp.a

		return Quaternion(na, nb, nc, nd)

	def add(self, comp):
		na = self.a + comp.a
		nb = self.b + comp.b
		nc = self.c + comp.c
		nd = self.d + comp.d

		return Quaternion(na, nb, nc, nd)

	def sub(self, comp):
		na = self.a - comp.a
		nb = self.b - comp.b
		nc = self.c - comp.c
		nd = self.d - comp.d

		return Quaternion(na, nb, nc, nd)

	def div(self, comp):
		# if (comp.a ** 2 + comp.b ** 2) != 0:
		# 	na = (self.a * comp.a + self.b * comp.b) / (comp.a ** 2 + comp.b ** 2)
		# 	nb = (self.b * comp.a - self.a * comp.b) / (comp.a ** 2 + comp.b ** 2)

		# 	return Complex(na, nb)
		# else:
		# 	raise ZeroDivisionError("division by zero")

	def pow(self, comp):

		# if self.a == 0 and self.b == 0 and comp.a == 0 and comp.b == 0:
		# 	raise ArithmeticError("indefinite power")

		# elif self.a == 0 and self.b == 0:
		# 	return Complex(0, 0)

		# elif self.a == 1 and self.b == 0:
		# 	return Complex(1, 0)

		# elif comp.a == 0 and comp.b == 0:
		# 	return Complex(1, 0)

		# elif comp.a == 1 and comp.b == 0:
		# 	return Complex(self.a, self.b)

		# else:
		# 	mult1 = (self.a ** 2 + self.b ** 2) ** (comp.a / 2) * exp(-comp.b * atan2(self.b, self.a))
		# 	real_mult = cos(comp.a * atan2(self.b, self.a) + .5 * comp.b * log(self.a**2 + self.b**2))
		# 	imag_mult = sin(comp.a * atan2(self.b, self.a) + .5 * comp.b * log(self.a**2 + self.b**2))

		# 	na = mult1 * real_mult
		# 	nb = mult1 * imag_mult

		# 	return Complex(na, nb)

	def __str__(self):

		# msg = ""
		# if self.a != 0:
		# 	msg += f"{self.a} "

		# if self.b != 0:
		# 	if self.b > 0 and self.a != 0:
		# 		msg += f"+ {self.b}*i"
		# 	elif self.b < 0 and self.a != 0:
		# 		msg += f"- {self.b*-1}*i"
		# 	elif self.b > 0 and self.a == 0:
		# 		msg += f"{self.b}*i"
		# 	elif self.b < 0 and self.a == 0:
		# 		msg += f"{self.b}*i"

		# elif msg == "":
		# 		msg = "0"

		# return msg