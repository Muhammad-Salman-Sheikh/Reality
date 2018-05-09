import sys


def Interpreter(program , stream):
	'''
	Initial values for both integral and string results
	'''
	intValue = 0
	strValue = ''
	'''
	Checking for empty program and input is not given
	and outputting the FizzBuzz program ahh good ol' fizzbuzz !
	'''
	if program == '' and len(stream) == 0 :
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
	input is given but program is empty 
	then just print the output
	'''
	elif program == '' and len(stream) > 1 :
		strValue = stream
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
			alternate input given in program
			'''
		if i == 'L' and len(program) == 1 :
			inSt = int(stream)
			strValue = 'true' if inSt % 4 == 0 and (not inSt % 100 == 0 or inSt % 400 == 0) else 'false'
		elif i == 'L' and len(program) > 1 :
			inSt = int(program[1:])
			strValue = 'true' if inSt % 4 == 0 and (not inSt % 100 == 0 or inSt % 400 == 0) else 'false'

	return strValue if not strValue == '' else intValue if not intValue == 0 else program


program = open(sys.argv[1]).read()

print(Interpreter(program,sys.stdin.read()))

#print(Interpreter('',input()))
# ^ if you want you can do that too
