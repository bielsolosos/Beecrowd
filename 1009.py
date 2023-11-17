vendedor = input()
fixo = float(input())
vendas = float(input())

vendas = (fixo + ((vendas*15)/100))

print("TOTAL = R$ {:.2f}".format(vendas))