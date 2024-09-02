import os
os.system("cll|| clear")
soma=0
media=0
a=3

for i in range(a):
    nota=float(input(f"digite sua nota:"))
    while True:
        if nota<0 or nota>10:
            print("nota incoreta:")
            break
        else:
            break
    soma=nota+soma
    media=soma/a
print(soma,media)

if media>=7:
   print(" aprovado")
   if media>=5:
       print("reprovado")


