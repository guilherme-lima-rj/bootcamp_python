# Instruções:
# O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Digite seu nome: ")

# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.
salario_usuario = float(input("Digite seu salário: "))

# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, 
# que também pode ser um número decimal.
bonus_usuario = float(input("Digite seu percentual de bônus recebido: "))

# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
CONSTANTE_BONUS = 1000

valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: 
# "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome_usuario} o seu valor bônus foi de {valor_bonus}.")

# Exemplo de Saída:
# Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:

# Olá Luciano, o seu bônus foi de 8500
