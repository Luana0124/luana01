import os
os.system("cls|| clear")
 
contador=0
soma=0
while True:
    inserir_nota=input("digite uma nota desejada:")
    if inserir_nota=="N":
        media=soma/contador
        print ("fmedia (media:)")
        break
    else:
        contador=contador+1
        soma=contador/soma

