ano = int(input("Digite um ano: "))

print("-" * 30)
print(f"Ano informado: {ano}")

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Status: Ano Bissexto!")
else:
    print("Status: Ano NÃO é bissexto!")