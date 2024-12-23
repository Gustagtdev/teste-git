'''Faça um programa que realize a média de 2 notas de 3 estudantes e faça os requisitos de aprovação,
recuperação e reprovação.
Este projeto possui o intuito em aprimorar minhas habilidades com a ferramenta Git.'''
aluno1= "Igor"
aluno2= "João"
aluno3= "Rafaela"
aluno4="Gustavo"
nota1_aluno1= float(input(f'Digite a 1° nota de {aluno1}:'))
nota2_aluno1= float(input(f'Digite a 2° nota de {aluno1}: '))
media= (nota1_aluno1+nota2_aluno1) / (2)
print(media)

nota1_aluno2= float(input(f'Digite a 1° nota de {aluno2}:'))
nota2_aluno2= float(input(f'Digite a 2° nota de {aluno2}: '))
media2= (nota1_aluno2+nota2_aluno2) / (2)
print(media2)

nota1_aluno3= float(input(f'Digite a 1° nota de {aluno3}:'))
nota2_aluno3= float(input(f'Digite a 2° nota de {aluno3}: '))
media3= (nota1_aluno3+nota2_aluno3) / (2)
print(media3)
nota1_aluno4= float(input(f'Digite a 1° nota de {aluno4}:'))
nota2_aluno4= float(input(f'Digite a 2° nota de {aluno4}: '))
media4= (nota1_aluno4+nota2_aluno4) / (2)
print(media4)

if media >= 6.0:
    print(f"{aluno1} está aprovado")
elif 6.0 > media > 4.0:
    print(f"{aluno1} está de recuperação")
elif media < 4.0:
    print(f"{aluno1} está reprovado")

if media2 >= 6.0:
    print(f"{aluno2} está aprovado")
elif 6.0 > media2 > 4.0:
    print(f"{aluno2} está de recuperação")
elif media2 < 4.0:
    print(f"{aluno2} está reprovado")

if media3 >= 6.0:
    print(f"{aluno3} está aprovado")
elif 6.0 > media3 > 4.0:
    print(f"{aluno3} está de recuperação")
elif media < 4.0:
    print(f"{aluno3} está reprovado")

if media4 >= 6.0:
    print(f"{aluno4} está aprovado")
elif 6.0 > media4 > 4.0:
    print(f"{aluno4} está de recuperação")
elif media < 4.0:
    print(f"{aluno4} está reprovado")
