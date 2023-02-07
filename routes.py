from flask import Flask, render_template, request
from quizFactory import QuizFactory
from temas import Temas
from quiz import NumberResponse
from quiz import ComandoRespotas
from flask import jsonify

app = Flask(__name__)


@app.route('/quiz', methods= ['POST'])
def return_quiz():
    typeQuizStr = request.form["typeQuiz"]
    print(typeQuizStr)
    typeQuizToRetrun = Temas[typeQuizStr]
    return jsonify(QuizFactory.Quiz(typeQuizToRetrun).to_dict())

@app.route('/resultado', methods= ['POST'])
def result():
    resultado = request.form["resultado"]
    repostas = NumberResponse(resultado)
    comando = ComandoRespotas(repostas)
   
    return f"{comando.executa()}"



@app.route('/', methods= ['GET'])
def index():
    return render_template('Index.html')

app.run(port=8091, debug=True)