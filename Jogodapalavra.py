import os
import random 

corretas = input("Palavra secreta: ")
erros = []
print(corretas)
campos = ["_"]*len(corretas)

def verificar(erros,corretas,tentativa,campos):
	for i in range(len(corretas)):
		if tentativa == corretas[i]:
			campos[i] = tentativa
	res = corretas.count(tentativa)
	if res == 0:
		erros.append(tentativa)
	return erros,corretas,campos
	
def ganhar(campos):
	if campos.count("_") == 0:
		print("Ganhou")
		
while True:
	ganhar(campos)
	print(erros)
	print(campos)
	tentativa = input("Tentativa : ")
	erros ,corretas,campos= verificar(erros,corretas,tentativa,campos)
	os.system("clear")
	
	
	
	