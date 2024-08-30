import os
os.system("cls||clear")



for i in range(3):
    nota=float(input("digite sua nota":))
    while True:
        if nota<0 or nota>10:
            print("nota incoreta:")
            break
        else:
            break
    soma=nota+soma
    media=soma/3
print(soma,media)

if media>=7:
   print(" aprovado")
   if media>=5:
       print("reprovado")
