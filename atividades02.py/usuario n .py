import os
os.system("cls|| clear")
 
contador=0
soma=0
while True:
    inserir_nota=input("digite uma nota desejada:")
    contador+=1
    soma+inserir_nota
    resposta=input(" deseja inserir mais nota?:")
    if resposta=="N":
     break
    media=soma/contador
    print(f"Media(media)")



