from temas import Temas
from quiz import Quiz,history,math,geography,world,computing,ContentStorage

#Padrao factory usado para separar os temas para que seja retornado apenas o tema escolhido pelo usuário
class QuizFactory():

    def Quiz(tipo):
        if tipo == Temas.Historia:
            return Quiz(history['id'],history['title'],ContentStorage.ReturnContentSpecifiedArq(tipo))
        elif tipo == Temas.Matematica:
            return Quiz(math['id'],math['title'],ContentStorage.ReturnContentSpecifiedArq(tipo))
        elif tipo == Temas.Geografia:
            return Quiz(geography['id'],geography['title'],ContentStorage.ReturnContentSpecifiedArq(tipo))
        elif tipo == Temas.Informatica:
            return Quiz(computing['id'],computing['title'],ContentStorage.ReturnContentSpecifiedArq(tipo))
        elif tipo == Temas.Mundo:
            return Quiz(world['id'],world['title'],ContentStorage.ReturnContentSpecifiedArq(tipo))
