import os 
os.system("cls|| clear")

QUANTIDADE_NUMEROS=3
lista_pares_positivos={}

#entrada.
print("/n===solicintado dados===")
for i in range(QUANTIDADE_NUMEROS):
    while True:
        numero=input(f"digite o {i+1}numero:")
        
        # verificando se o numero è par e positivo.
        if numero%2==0 and numero>0:
            lista_pares_positivos.append(numero)
            break
        else:
            print("numero invalido./ntente novamente./n/n")

            # saida.
            print("/n===exibindo resultado===")
            for i, numero in enumerate(reversed)(lista_pares_positivos)):
              print(f"{len(lista_pares_positivos)}")
