#!/usr/bin/python
import sys  #Biblioteca do sistema


# Funcoes

def add():
	count = float(values.pop())            # Tira da Pilha
	count = count + float(values.pop())    # Tira da pilha outro / Já somando
	values.append(count)                   # Bota na pilha o resultado
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
	

# Abre Arquivo

try:
    files = open(sys.argv[1], "r")       # Por linha de comando
    #files = open("test.txt", "r")       # Direto do código
except:
    sys.exit("ERROR: Wrong or missing file")      # Se der erro ao abrir

stack = files.read().split()               # Le o arquivo
values = []                                # Inicia uma pilha só com valores

for i in range(0,len(stack)):
	if(stack[i].upper() == "PUSH"):            # Verifica se é push
		values.append(float(stack[i+1]))       # Se for, bota o valor que vem a seguir na pilha
	elif (stack[i].upper() == "SUM"):          # Verifica se é soma
		try:
			add()                              # Se não ocorrer nenhum erro ele chama a função soma
		except:
			print("The stack is empty.")       # Se não ele joga o erro na tela.
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
			if(stack[i-1].upper() == "PUSH"):    # Ajuste caso leia um numero
				continue
			else:
				print("\""+stack[i]+"\" "+"is undefined.")	    # Caso leia algo fora dos comandos esperados
				break
		except:
			print("\""+stack[i]+"\""+"is undefined.")	
			break

files.close()




