print()
print('Digite a letra respectiva à resposta que você considera como correta.')
print()


perguntas = {
    'pergunta 1' : {
        'pergunta' : 'Quanto é 1 + 1?',
        'respostas' : {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4' },
        'resposta certa' : 'b',
    },
    'pergunta 2' : {
        'pergunta' : 'Quanto é 10 + 1?',
        'respostas' : {'a': '11', 'b': '22', 'c': '13', 'd': '6'},
        'resposta certa' : 'a',
    },
    'pergunta 3' : {
            'pergunta' : 'Quanto é 2 * 2?',
            'respostas' : {'a': '8', 'b': '22', 'c': '3', 'd': '4'},
            'resposta certa' : 'd',
        },
    'pergunta 4' : {
            'pergunta' : 'Quanto é 4 / 2?',
            'respostas' : {'a': '3', 'b': '4', 'c': '2', 'd': '0'},
            'resposta certa' : 'c',
        },
    'pergunta 5' : {
            'pergunta' : 'Quanto é 0 + 0?',
            'respostas' : {'a': '0', 'b': '2', 'c': '3', 'd': '4'},
            'resposta certa' : 'a',
        },
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'{rk} : {rv}')
    
    resposta_usuario = input('Sua resposta: ')
    print()

    if resposta_usuario == pv['resposta certa']:
        respostas_certas += 1

        
    

qnt_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qnt_perguntas * 100
print()
print(f'Você acertou {respostas_certas} respostas!')
print()
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%!')
print()

if porcentagem_acerto >= 70:
    print('Você está aprovado!')

else:
    print('Você está reprovado!')
