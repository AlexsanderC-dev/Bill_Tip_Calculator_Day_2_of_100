# Calculadora simples de valor total da conta do restaurante dividido por um grupo.
# O resultado será arredondado para 2 casas decimais.
print("Bem vindo(a) a calculadora de gorjetas!\n")
valor_da_conta = float(input("\nQual o valor total da Conta? R$\n\n"))
gorjeta = int(input("\nQual a porcentagem da gorjeta que dejam pagar? 5, 10, 12, or 15?\n\n"))
qtd_pessoas = int(input("\nQuantas pessoas vão dividir a conta?\n\n"))

porcentagem_da_gorjeta = gorjeta / 100
valor_total_gorjeta = gorjeta * porcentagem_da_gorjeta
total_conta = valor_da_conta + valor_total_gorjeta
valor_por_pessoa = total_conta / qtd_pessoas
valor_final = round(valor_por_pessoa, 2)

print(f"\nCada pessoa irá pagar: R${valor_final}")
