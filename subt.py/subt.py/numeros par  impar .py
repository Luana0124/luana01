import os 
os.system(" clls||clear")

#processamento.
def verficar_numero(numero):
    if numero%2==0:
        print("par.")    
    else:

        print("impar.")
 #Entrada de dados.
print("===solicitando dados===")
numero=int(input("digite um numero:"))

#saida.
verficar_numero(numero)