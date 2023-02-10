let containerQuiz = document.getElementById('containerQuiz');
let mathButton = document.getElementById('mathButton');
let historyButton = document.getElementById('historyButton');
let geographyButton = document.getElementById('geographyButton')
let worldButton = document.getElementById('worldButton')
let computingButton = document.getElementById('computingButton')
let menuContainer = document.getElementById('menu')
let menuButton = document.getElementById('menuButton')
let proxButton = document.getElementById('proxButton')
let perguntaAtual = 1;
let contador = 0;
let lista = [];
let perguntaID;
let variavel=0;
let numRespostasCertas = 0;
let selectedOptionElement = null
let quiz = null;
let result= null;
let respostaEr= null

mathButton.addEventListener('click', function(ev){
    getQuiz("Matematica")
    menuContainer.classList.remove('menu')
    menuContainer.classList.add('hide')
})

historyButton.addEventListener('click', function(ev){
    getQuiz("Historia")
    menuContainer.classList.remove('menu')
    menuContainer.classList.add('hide')                                                                     
})

geographyButton.addEventListener('click', function(ev){
    getQuiz("Geografia")
    menuContainer.classList.remove('menu')
    menuContainer.classList.add('hide')                                                                     
})

computingButton.addEventListener('click', function(ev){
    getQuiz("Informatica")
    menuContainer.classList.remove('menu')
    menuContainer.classList.add('hide')                                                                     
})

worldButton.addEventListener('click', function(ev){
    getQuiz("Mundo")
    menuContainer.classList.remove('menu')
    menuContainer.classList.add('hide')                                                                     
})

menuButton.addEventListener('click', function(ev){
    perguntaAtual = 1
    numRespostasCertas = 0;
    containerQuiz.innerHTML= ""
    menuContainer.classList.remove('hide')
    menuContainer.classList.add('menu')
    menuButton.classList.add('hide')
    proxButton.classList.add('hide')
})

proxButton.addEventListener('click', function(ev){
    perguntaAtual++
    proxButton.classList.remove('btn','btn-secondary')
    proxButton.classList.add('hide')
    if(perguntaAtual == 4){
        proxButton.classList.remove('btn','btn-secondary')
        proxButton.classList.add('hide')
    }
    if(contador > 0){
        numRespostasCertas++;
    }
    if(perguntaID != 0){
        lista.push(perguntaID)
    }
    buildQuiz()
})

function getQuiz(typeQuiz){
    var dadosQuiz = $.post('/quiz', {"typeQuiz":typeQuiz})
    dadosQuiz.done(function(Quiz){
        quiz = Quiz
        buildQuiz();
        menuButton.classList.remove('hide')
    })
}

function buildQuiz(){
    console.log(quiz)
    containerQuiz.innerHTML= ""
    contador = 0;
    variavel=0;
    menuButton.classList.add('btn','btn-secondary')
        const resultContainer = document.createElement('div');
        const titleQuiz = document.createElement('h1');
        titleQuiz.textContent = quiz.title;
        containerQuiz.appendChild(titleQuiz);
        containerQuiz.classList.add('Quiz')
        
        if(perguntaAtual == 4){
            const str2 = document.createElement('h3');
            const str =  document.createElement('h3');
            const acertos = document.createElement('h3')
            resultContainer.classList.add('resultado')
            var dadosResult = $.post('/resultado', {"resultado":numRespostasCertas})
            dadosResult.done(function(String){
                result = String;
                str.classList.add('format')
                str.textContent = result
                acertos.textContent = numRespostasCertas+'/3'
            })
            resultContainer.appendChild(str)
            resultContainer.appendChild(acertos)
            var i;
            for(i= 0 ; i<lista.length; i++){
                if(lista[i] == 1 && lista.length == 1){
                    variavel = 1
                }
                if(lista[i] == 2 && lista.length == 1){
                    variavel = 2
                }
                if(lista[i] == 3 && lista.length == 1){
                    variavel = 3
                }
                if(lista[i] == 1 && lista[i+1] == 2 && lista.length == 2){
                    variavel = 4
                }
                if(lista[i] == 2 && lista[i+1] == 3 && lista.length == 2){
                    variavel = 5
                }
                if(lista[i] == 1 && lista[i+1] == 3 && lista.length == 2){
                    variavel = 6
                }
            }

            var respostaER = $.post('/respostasErradas', {"respostasErradas":variavel})
            respostaER.done(function(String2){ 
                respostaEr = String2;
                str2.textContent = respostaEr 
                lista = []
            })
            resultContainer.appendChild(str2)
            
        }else{
            resultContainer.classList.add('hide')
        }

        quiz.perguntas.forEach(function(pergunta, indice){
            const questionContainer = document.createElement('div');
        

            if(pergunta.id != perguntaAtual){
                questionContainer.classList.add('hide')
            }else{
                questionContainer.classList.remove('hide')
                questionContainer.classList.add('pergunta')
            }


            const perguntaDescricao = document.createElement('h3');
            perguntaDescricao.textContent = pergunta.title;
            const OptionsPergunta = document.createElement('div');
            OptionsPergunta.classList.add('options');
            

            pergunta.options.forEach(function(option, indice){

                const newContainerQuestionOption = document.createElement('label')
                newContainerQuestionOption.classList.add('question-option')

                const textSpan = document.createElement('span')
                textSpan.textContent = option.text

                const radioButton = document.createElement('input')
                radioButton.id = option.id
                radioButton.setAttribute("type","radio");
                radioButton.setAttribute("name","question");
                radioButton.classList.add("hide");

                radioButton.addEventListener("change",function(e){
                    proxButton.classList.remove('hide')
                    proxButton.classList.add('btn','btn-secondary')
                    if(selectedOptionElement != null){
                        selectedOptionElement.classList.remove('container-color-option')
                    }
                    selectedOptionElement = newContainerQuestionOption
                    newContainerQuestionOption.classList.add('container-color-option')
                    if(option.id == pergunta.resposta){
                        contador = 1
                        perguntaID = 0
                    } else{
                        contador = 0;
                        perguntaID = pergunta.id
                    }
   
                })

                
                newContainerQuestionOption.appendChild(radioButton)
                newContainerQuestionOption.appendChild(textSpan)
                newContainerQuestionOption.classList.add('container-option')

                OptionsPergunta.appendChild(newContainerQuestionOption);


            })
            containerQuiz.appendChild(resultContainer)
            questionContainer.appendChild(perguntaDescricao);
            questionContainer.appendChild(OptionsPergunta);
            containerQuiz.appendChild(questionContainer);
            containerQuiz.appendChild(menuButton);
            containerQuiz.appendChild(proxButton);
            
        })
}

