import os 
os. system("cls||clear")

def nota_media(k):
    if k >7:
        print("aprovado:")  
    else:
        print("reprovado:")

def media(nota1, nota2):
        soma = nota1 + nota2
        resultado= soma / 2
        return resultado
# entrada.
nota1=(float(input("digite uma nota:")))
nota2=( float(input("digite a segunda nota:")))


#saida.
print("/n===resutado.")
nota_final = media(nota1, nota2)
print(f"media = {nota_final}")
nota_media(nota_final)