# Lista de treinos
treinos = ["A (Quadríceps)", "B (Glúteos e Posterior de coxa)", "C (Costas e Peito)", "D (Bíceps, Tríceps e Ombro)"]

# Pedir ao usuário os dias da semana que ele gostaria de ir à academia
dias_semana = input("Informe os dias da semana que você gostaria de ir à academia (separados por vírgula): ").split(",")

# Organizar os treinos com base nos dias da semana
treinos_organizados = []

# Variável para controlar o tipo de treino (superior ou inferior)
tipo_treino = "superior"  # Começa com treino superior

for dia in dias_semana:
    treino = None
    for t in treinos:
        if (tipo_treino == "superior" and (t.startswith("C") or t.startswith("D"))) or \
           (tipo_treino == "inferior" and (t.startswith("A") or t.startswith("B"))):
            treino = t
            treinos.remove(t)  # Remove o treino da lista de treinos disponíveis
            break
    
    if treino is None:
        print("Não é possível organizar os treinos com as restrições fornecidas.")
        break

    treinos_organizados.append((dia.strip(), treino))
    tipo_treino = "inferior" if tipo_treino == "superior" else "superior"

# Se ainda houver dias de semana sobrando e treinos disponíveis, repita o primeiro treino
while len(treinos_organizados) < len(dias_semana) and treinos:
    treinos_organizados.append((dias_semana[len(treinos_organizados)].strip(), treinos[0]))

# Imprimir os treinos organizados
if treinos_organizados:
    print("\nTreinos organizados:")
    for dia, treino in treinos_organizados:
        print(f"{dia}: Treino {treino}")
