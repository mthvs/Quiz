from temas import Temas
from quiz import historia, matematica, geografia, informatica, mundo

#Padrao factory usado para separar os temas para que seja retornado apenas o tema escolhido pelo usuário
class QuizFactory():

    def Quiz(tipo):
        if tipo == Temas.Historia:
            print('estou em historia')
            return historia
        elif tipo == Temas.Matematica:
            print('estou matematica')
            return matematica
        elif tipo == Temas.Geografia:
            return geografia
        elif tipo == Temas.Informatica:
            return informatica
        elif tipo == Temas.Mundo:
            return mundo
