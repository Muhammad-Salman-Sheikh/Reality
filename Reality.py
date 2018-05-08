import sys


def Interpreter(program , stream):
	'''
	Initial values for both integral and string results
	'''
	intValue = 0
	strValue = ''
	'''
	Checking for empty program
	and outputting the FizzBuzz program ahh good ol' fizzbuzz !
	'''
	if program == '':
		a = ''
		for i in range(1,100):
			if i % 3 == 0 and i % 5 == 0:
				a += 'FizzBuzz '
			elif i % 3 == 0:
				a += 'Fizz '
			elif i % 5 == 0:
				a += 'Buzz '
			else :
				a += '' + str(i) + ' '
		strValue = '\n'.join(a.split(" "))
		return strValue
		'''
		Checking if it is 1 byte program and is a space
		then going forward with our plan to be masters and write hello world 
		'''
	elif program == ' ':
		strValue = 'Hello, World!'
		return strValue
		'''
		Otherwise lets just do boring (note : sarcasm) stuff
		'''
	for i in program :
		'''
		Primality test ! (number via stdinput)
		and 
		Primality test (no input)
		'''
		if i == 'P' and len(program) == 1 :
			inSt = int(stream)
			strValue = 'true' if not (inSt < 2 or any(inSt % x == 0 for x in range(2, int(inSt ** 0.5) + 1))) else 'false'
		elif i == 'P' and len(program) > 1 :
			inSt = int(program[1:])
			strValue = 'true' if not (inSt < 2 or any(inSt % x == 0 for x in range(2, int(inSt ** 0.5) + 1))) else 'false'			
			'''
			Collatz conjecture (number via stdinput)
			'''
		if i == 'C' :
			inSt = int(stream)
			counter = 0
			while inSt > 1 :
				if inSt % 2 == 0 :
					inSt /= 2
				else :
					inSt = inSt * 3 + 1
				counter += 1
			intValue = counter
		for j in ['+' , '-' , '*' , '/' , '%'] :
			if i == j and len(program) == 1 :
				inSt = stream.split(',')
				intValue = eval(inSt[0] + str(i) + inSt[1])
			if i == j and len(program) > 1 : 
				inSt = stream.split(j)
				intValue = eval(inSt[0] + str(j) + inSt[1])
			'''
			checking for leap year (input via stdinput)
			'''
		if i == 'L' and len(program) == 1 :
			inSt = int(stream)
			strValue = 'true' if inSt % 4 == 0 and (not inSt % 100 == 0 or inSt % 400 == 0) else 'false'
		elif i == 'L' and len(program) > 1 :
			inSt = int(program[1:])
			strValue = 'true' if inSt % 4 == 0 and (not inSt % 100 == 0 or inSt % 400 == 0) else 'false'

	return strValue if not strValue == '' else intValue
	'''
	prog = sys.argv[1]
	if prog.endswith('.txt'):
	    prog = open(prog).read()
	
	print(Interpreter(prog,sys,sys.stdin.read()))
	'''

print(Interpreter('',input()))
