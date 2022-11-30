from temas import Temas

class QuizFactory():

    def Quiz(tipo, perguntas, respostas):
        if tipo == Temas.Geografia:
            return 