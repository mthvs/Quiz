from respostas import Respostas

class Pergunta:
    def __init__(self, pergunta, respostas):
        self.pergunta = pergunta
        self.respostas = respostas

def respostas_correta(RC):
    respUser= input('Escolha uma Resposta:')
    if respUser == RC:
        print('\n Parabens escolheu a resposta correta')
    else:
        print('\n Voce errou boa sorte na proxima')


Q1 = Pergunta('Quanto é 2+2?', Respostas({'a': '8','b':'4','c':'7'},'b'))
Q2 = Pergunta('Em que ano Rainha Elizabete Morreu?',Respostas({'a': '2018','b':'2019','c':'2022'},'c'))
Q3 = Pergunta('Quem foi Michael Jackson?',Respostas({'a': 'Contor','b':'Ator','c':'Escritor'},'a'))

Qlista = [Q1,Q2,Q3]
for x in Qlista:
    print(x.pergunta)
    for i in x.respostas.respostas:
        print(f'{i}.{x.respostas.respostas[i]}')
    print('\n')
    respostas_correta(x.respostas.respostasC)
    print('\n')

