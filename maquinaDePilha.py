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
    files = open(sys.argv[1], "r")
    #files = open("test.txt", "r")
except:
    sys.exit("ERROR: Wrong or missing file")

stack = files.read().split()
values = []

for i in range(0,len(stack)):
	if(stack[i].upper() == "PUSH"):
		values.append(float(stack[i+1]))
	elif (stack[i].upper() == "SUM"):
		try:
			add()
		except:
			print("The stack is empty.")
	elif (stack[i].upper() == "MULT"):
		try:
			mult()
		except:
			print("The stack is empty.")
	elif (stack[i].upper() == "DIV"):
		try:
			div()
		except:
			print("The stack is empty.")
	elif (stack[i].upper() == "SUB"):
		try:
			sub()
		except:
			print("The stack is empty.")
	elif (stack[i].upper() == "PRINT"):
		print(values.pop())
		break
	else:
		try:
			if(stack[i-1].upper() == "PUSH"):
				continue
			else:
				print("\""+stack[i]+"\" "+"is undefined.")	
				break
		except:
			print("\""+stack[i]+"\""+"is undefined.")	
			break

files.close()




