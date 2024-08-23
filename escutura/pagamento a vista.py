import os
os.system("cll|| clear")

#declaracando dados.
desconto=0
preco_final=0
preco_final=0

print("solicitando dados para o usuario")      
 preco_produto=int(input("digite o valor do produto:")
print("1-pagamento a vista")
print("2-pagamento a prazo")
opcao=int(input("informar a opcão desejada:"))
match(opcao):
    case1:
    desconto=preco_produto*0.18
    preco_final=preco_produto-desconto
    print("f/npreco do produto:R$ (preco_produto)")
    print("f/n forma de pagamento: a vista")
    print("f/nvalor do descontoR$(desconto)")
    print("ftotal a pagar:R$(preco_final)")
     
     case2:
     parcelas=int(input("/n digite a quantidade de parcelas:"))
     pre