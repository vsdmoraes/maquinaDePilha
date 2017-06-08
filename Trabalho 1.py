#!/usr/bin/python
import sys

def add():
	count = float(values.pop())
	count = count + float(values.pop())
	values.append(count)
def mult():
	count = float(values.pop())
	count = count * float(values.pop())
	values.append(count)
def div():
	count = float(values.pop())
	count = count / float(values.pop())
	values.append(count)
def sub():
	count = float(values.pop())
	count = count - float(values.pop())
	values.append(count)
	
try:
    #files = open(sys.argv[1], "r")
    files = open("test.txt", "r")
except:
    sys.exit("ERROR: Wrong or missing file")

stack = files.read().split()
values = []

for i in range(0,len(stack)):
	if(stack[i] == "PUSH"):
		values.append(float(stack[i+1]))
	elif (stack[i] == "ADD"):
		add()
	elif (stack[i] == "MULT"):
		mult()
	elif (stack[i] == "DIV"):
		div()
	elif (stack[i] == "SUB"):
		sub()
	elif (stack[i] == "PRINT"):
		save = values.pop()
		values.append(save)
		print(save)
	else:
		try:
			if(stack[i-1] == "PUSH"):
				continue
		except:
			print(stack[i],"is undefined.")	
			break

files.close()




