import json
from temas import Temas
from integer import Integer
from collections.abc import Iterator, Iterable


with open("historyQuestion.json", encoding='utf-8') as Qh:
    history = json.load(Qh)

with open("mathQuestion.json", encoding='utf-8') as Qm:
    math = json.load(Qm)

with open("geographyQuestion.json", encoding='utf-8') as Qg:
    geography = json.load(Qg)

with open("computingQuestion.json", encoding='utf-8') as Qc:
    computing = json.load(Qc)

with open("worldQuestion.json", encoding='utf-8') as Qw:
    world = json.load(Qw)

class Comando():
    def executa(self):
        pass

class NumberResponse():
    def __init__(self,numRespotasCertas):
        self.numRespotasCertas = numRespotasCertas
        pass

    def responderUsuario(self):
        if self.numRespotasCertas == "0":
            return "Voce Falhou, tenta mais na proxima"
        elif self.numRespotasCertas == "1":
            return "Acertou apenas uma, se esforce mais na proxima"
        elif self.numRespotasCertas == "2":
            return "Parabens voce quase acertou tudo"
        elif self.numRespotasCertas == "3":
            return "Parabens, acertou todas as Questoes"   

class ComandoRespotas(Comando):
    def __init__(self,numRespotasCertas) :
        self._numRespotasCertas = numRespotasCertas

    def executa(self):
       return self._numRespotasCertas.responderUsuario()

class QuestionIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, question: Iterable,
            reverse: bool = False) -> None:
        self._question = question
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._question[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

class QuestionIterable(Iterable):
    def __init__(self) -> None:
        self._question = []

    def __iter__(self) -> QuestionIterator:
        return QuestionIterator(self._question)

    def get_reverse(self) -> QuestionIterator:
        return QuestionIterator(self._question, True)

    def add_item(self, item):
        self._question.append(item)

class Pergunta():
    def __init__(self,id, title,resposta):
        self.id = id
        self.title = title
        self.options = []
        self.resposta = resposta


    def define_options(self,respostas):
        self.options = respostas

    def to_dict(self):
        return {'id': self.id , 'title': self.title ,'options': self.Options_to_dict(), 'resposta': self.resposta}

    def Options_to_dict(self):
        List_options = []
        for option in self.options:
            List_options.append(option.to_dict())
        return List_options

    def __str__(self):
        return f'{self.id} {self.title}'

class Option():
    def __init__(self,id,text):
        self.id = id
        self.text = text

    def __str__(self):
        return f'{self.id} {self.text}'

    def to_dict(self):
        return {'id': self.id, 'text': self.text}

class Quiz():
    def __init__ (self,id,title,perguntas):
        self.id = id
        self.title = title
        self.perguntas = perguntas


    def to_dict(self):
        return {'id': self.id ,'title':self.title, 'perguntas': self.perguntas_to_dict()}

    def perguntas_to_dict(self):
        List_perguntas = []
        for pergunta in self.perguntas:
            List_perguntas.append(pergunta.to_dict())
        return List_perguntas

class ContentStorage():     
    def ReturnContentSpecifiedArq (paran):
        if paran == Temas.Matematica:
            readerfileMath = ReaderfileMath()
            readerfileMath.ler()
            return readerfileMath.iterator()
        elif paran == Temas.Historia: 
            readerfileHistory = ReaderfileHistory()
            readerfileHistory.ler()
            return readerfileHistory.iterator()
        elif paran == Temas.Geografia: 
            readerfileGeography = ReaderfileGeography()
            readerfileGeography.ler()
            return readerfileGeography.iterator()
        elif paran == Temas.Informatica: 
            readerfileComputing = ReaderfileComputing()
            readerfileComputing.ler()
            return readerfileComputing.iterator()
        elif paran == Temas.Mundo: 
            readerfileWorld = ReaderfileWorld()
            readerfileWorld.ler()
            return readerfileWorld.iterator()

class ReaderfileQuiz(): 
    def __init__(self):
        self.question = []
        self.contentFile = None,
        pass

    def ler(self):
        list_perguntas = []
        for i in self.contentFile['perguntas']:
            pergunta = Pergunta(i['id'], i['question'], i['answer_id'])
            list_options = []
            for x in i['options']:
                option = Option(x['id'], x['text'])
                list_options.append(option)
            pergunta.define_options(list_options)
            list_perguntas.append(pergunta)
        self.Instanse_question(list_perguntas)

    def Instanse_question(self, elements: list[str]) -> QuestionIterable():
        self.question =  QuestionIterable()
        for element in elements:
            self.question.add_item(element)
        return self.question

    def iterator(self):
        list=[]
        for e in self.question.get_reverse():
            list.append(e)
        return list
    
#Padrao Sigleton usado para seja possivel receber apenas uma vez o contudo presente no json.
class ReaderfileMath(ReaderfileQuiz):
    _instanse = None
    def __init__(self):
        super().__init__()
        self.contentFile = math
    
    def __new__(cls):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls)
        return  cls._instanse

class ReaderfileHistory(ReaderfileQuiz):
    _instanse = None
    def __init__(self):
        super().__init__()
        self.contentFile = history
    
    def __new__(cls):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls)
        return  cls._instanse

class ReaderfileComputing(ReaderfileQuiz):
    _instanse = None
    def __init__(self):
        super().__init__()
        self.contentFile = computing
    
    def __new__(cls):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls)
        return  cls._instanse

class ReaderfileGeography(ReaderfileQuiz):
    _instanse = None
    def __init__(self):
        super().__init__()
        self.contentFile = geography
    
    def __new__(cls):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls)
        return  cls._instanse

class ReaderfileWorld(ReaderfileQuiz):
    _instanse = None
    def __init__(self):
        super().__init__()
        self.contentFile = world
    
    def __new__(cls):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls)
        return  cls._instanse
        
def QuizTeste(Ruser,RQuiz):
    if Ruser == RQuiz:
        print("\nParabens Voce Acertou\n")
    else:
        print("\nvoce errou\n")

def teste(self):
        for i in self.perguntas:
            print(f"\n{i}")
            for x in i.options:
                print(f"{x.id} . {x.text}")
            print("\n")
            resposta = input("qual a resposta correta? R: ")
            QuizTeste(Integer(resposta), i.resposta)


historia = Quiz(history['id'],history['title'],ContentStorage.ReturnContentSpecifiedArq(Temas.Historia))
matematica = Quiz(math['id'], math['title'], ContentStorage.ReturnContentSpecifiedArq(Temas.Matematica))
geografia = Quiz(geography['id'],geography['title'], ContentStorage.ReturnContentSpecifiedArq(Temas.Geografia))
informatica = Quiz(computing['id'],computing['title'], ContentStorage.ReturnContentSpecifiedArq(Temas.Informatica))
mundo = Quiz(world['id'],world['title'], ContentStorage.ReturnContentSpecifiedArq(Temas.Mundo))

 

