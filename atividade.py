import os
os.system("cls|| clear")

def inflacionar(preco_preduto):
    if preco_produto<100:
        return (preco_produto*0.1)+ preco_produto
    else:
        return preco_produto*1.2
    
#entrada.
preco_produto=float(input("digite o preco de um produto:"))
# processamento. 
preco_produto=inflacionar(preco_produto)
#saida.
print("/n===resultado===")
print(f"preço infacionado:"){preco_inflacionado:.2f}