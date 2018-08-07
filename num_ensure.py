#from num_ensure import numeric_ensure
"""
Takes a question and asks it until somthing that can be
converted to a integer is given by the user,
it then returns that as an integer

if a string is given as a second argument,
 that is used at first instead
"""
def integer_ensure(question, value=None):
	frustrated = False
	while True: # is broken if no error
		try:
			if frustrated:
				integer = int(input("I SAID, " + question))
				break # these are only reached if no error
				
			elif value == None:
				integer = int(input(question))
				break
				
			else:
				integer = int(value)
				break
				
		except ValueError:
			frustrated = True
	return integer
	

#from num_ensure import formula_ensure
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


#from num_ensure import float_ensure
"""
Takes a question and asks it until somthing that can be
converted to a float is given by the user,
it then returns that as a float

if a string is given as a second argument,
 that is used at first instead
"""
def float_ensure(question, value=None):
	frustrated = False
	while True: # is broken if no error
		try:
			if frustrated:
				float_num = float(input("I SAID, " + question+ " "))
				break # these are only reached if no error
				
			elif value == None:
				float_num = float(input(question + " "))
				break
				
			else:
				float_num = float(value)
				break
				
		except ValueError:
			frustrated = True
	return float_num