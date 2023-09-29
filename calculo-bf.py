def calcular_percentual_gordura(imc, idade, sexo):
    if sexo == 1:
        bf = (1.20 * imc) + (0.23 * idade) - (10.8 * sexo) - 5.4
    elif sexo == 0:
        bf = (1.20 * imc) + (0.23 * idade) - 5.4
    else:
        return "Valor inválido para sexo. Use 0 para mulheres e 1 para homens."
    return bf

while True:
    try:
        sexo = int(input("Digite o sexo (0 para mulheres, 1 para homens): "))
        idade = int(input("Digite a idade: "))
        imc = float(input("Digite o IMC (Índice de Massa Corporal): "))

        percentual_gordura = calcular_percentual_gordura(imc, idade, sexo)

        print(f"O percentual de gordura corporal é: {percentual_gordura:.2f}%")

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos para idade e IMC.")
    
    resposta = input("Deseja calcular novamente? (S/N): ")
    if resposta.lower() != 's':
        break
