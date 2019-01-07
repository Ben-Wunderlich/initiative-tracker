#from input_ensure.inp_ensure import is_int
"""
takes a n item and returns true if it can be converted to an integer
"""
def is_int(num):
	try:
		int(num)
		return True
	except ValueError:
		return False
		

#from input_ensure.inp_ensure import integer_ensure
"""
Takes a question and asks it until somthing that can be
converted to an integer is given by the user,
it then returns that as an integer

if a string is given as a second argument,
that is used at first instead and is returned if it can 
be converted to an integer

min and max values place addition restrictions on the
number that will be returned
"""
def integer_ensure(question, value=None, min=None, max=None):
	frustrated = False
	inpt = value
	if inpt is None:
		inpt = "placeholder"
	while not is_int(inpt):
		try:
			if frustrated:
				inpt = int(input("I SAID "+question))
			elif value != None:#frustrated starts off as false so this will always run 1st time
				inpt = int(value)
			else:#runs 1st time if no value is given
				inpt = int(input(question))

			if min != None and inpt < min:#if less than min value
				inpt = "too small"
				print("Error 2301, value must be bigger than or equal to {}".format(min))
			if max != None and inpt > max:#if more than max value
				inpt = "too big"
				print("Error 2301, value must be smaller than or equal to {}".format(max))
		except ValueError:
			frustrated = True
	return inpt
			
			



#from input_ensure.inp_ensure import integer_ensure
"""
Takes a question and asks it until somthing that can be
evaluated is given by the user,
it then returns that as a number,

if a string is given as a second argument,
 that is used at first instead
"""
def formula_ensure(question, value=None):
	frustrated = False
	while True:# is broken if no error
		try:
			if frustrated:
				final = eval(input("I SAID " + question + " "))
				break# these are only reached if no error
				
			elif value == None:
				final = eval(input(question + " "))
				break
			
			else:
				final = eval(value)
				break
				
		except NameError:
			frustrated = True
		except SyntaxError:
			frustrated = True
	
	return final


#from input_ensure.inp_ensure import is_int
"""
takes a n item and returns true if it can be converted to a float
"""
def is_float(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

#from input_ensure.inp_ensure import float_ensure
"""
Takes a question and asks it until somthing that can be
converted to a float is given by the user,
it then returns that as an integer

if a string is given as a second argument,
that is used at first instead and is returned if it can 
be converted to an integer

min and max values place addition restrictions on the
number that will be returned
"""
def float_ensure(question, value=None, min=None, max=None):
	frustrated = False
	inpt = value
	if inpt is None:
		inpt = "placeholder"
	while not is_float(inpt):
		try:
			if frustrated:
				inpt = float(input("I SAID "+question))
			elif value != None:#frustrated starts off as false so this will always run 1st time
				inpt = float(value)
			else:#runs 1st time if no value is given
				inpt = float(input(question))

			if min != None and inpt < min:#if less than min value
				inpt = "too small"
				print("Error 2301, value must be bigger than or equal to {}".format(min))
			if max != None and inpt > max:#if more than max value
				inpt = "too big"
				print("Error 2301, value must be smaller than or equal to {}".format(max))
		except ValueError:
			frustrated = True
	return inpt