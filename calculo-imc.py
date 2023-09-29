def calculo_imc(massa, altura):
    imc = float(massa) / (float(altura) * float(altura))
    return imc

def get_status(imc):
    if 0 < imc < 17:
        return "Muito abaixo do peso"
    elif imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.99:
        return "Peso normal"
    elif imc < 29.99:
        return "Acima do peso"
    elif imc < 34.99:
        return "Obesidade I"
    elif imc < 39.99:
        return "Obesidade II (severa)"
    else:
        return "Obesidade III (mórbida)"

massa = input("Massa (em quilos): ")
altura = input("Altura (em metros): ")

imc = calculo_imc(massa, altura)
status = get_status(imc)

print(f"\nSeu IMC é de {imc:.2f}.")
print(f"Situação: {status}.\n")
input("Pressione qualquer tecla para finalizar.")