from tkinter import *
from tkinter import ttk
#инициализируем глобальные переменные
#Данные два массива заплняются перед игрой составителем викторины
questions = ['В каком году было крещение Руси? Укажите только год события.',
             'В каком году произошло Ледовое Побоище? Укажите только год события.',
             'В каком году была Куликовская битва? Укажите только год события.',
             'В каком году произошло объединение Польши и Литвы, появление Речи Посполитой? Укажите только год события.',
             'В каком году была Варфоломеевская ночь во Франции? Укажите только год события.'
             ]
trueAnswers = ['988',
               '1241',
               '1380',
               '1596',
               '1572'
               ]

userAnswers = []


i = 0
#Methods
def getResult():
    score = 0
    for i in range(len(questions)):
        if userAnswers[i].lower() == trueAnswers[i].lower():
            score += 1
    question['justify'] = CENTER
    analytics = score / len(questions)
    if analytics <= 0.2:
        itog = 'Плоховато! Повтори эту тему, и в следующий раз всё обязаельно получится!'
    elif 0.2 < analytics < 0.5:
        itog = 'Плоховато, попробуй ещё раз!'
    elif 0.5 <= analytics < 0.8:
        itog = 'Неплохо! Так держать!'
    elif 0.8 <= analytics < 1:
        itog = 'Очень хорошо! Молодец!'
    elif analytics == 1:
        itog = 'Это максимальное количество баллов! Молодец!'
    question['text'] = f'Поздравляем, вы прошли игру!\nВы набрали {score} из {len(questions)} очков!\n {itog}'
def getAnswer():
    global i
    global answer
    global btn
    ans = answer.get()
    userAnswers.append(ans)
    if i+1<len(questions):
        i+=1
        answer.delete(0,END)
        question['text'] = f'Вопрос {i+1}. {questions[i]}'
    else:
        answer.delete(0,END)
        answer.destroy()
        btn.destroy()
        getResult()
    print(userAnswers)

#инициализировали окно и задали его размеры
window = Tk()
window.title('Викторина по датам')
window.geometry("800x500")
window.configure(background='#ffb570')
#Заготовка

#Вопрос
question= ttk.Label(window, 
                    text=f'Вопрос {i+1}. {questions[i]}',
                    font=("Courier", 20),
                    justify=LEFT,
                    wraplength=700,
                    background='#ffb570'
                    )
question.pack(anchor=W, pady=30, padx=40)        

#Ответ
answer = ttk.Entry(window,  
                width=40, 
                justify=LEFT, 
                font=("Calibri", 20)
                )
answer.pack(anchor=W, padx=40, pady=20)

#Кнопка отправки ответа
btn = Button(text="Ответить", 
                width=10, 
                justify=CENTER,
                font=('Courier',14),
                command = getAnswer,
                activebackground='#e04724',
                bg='#e56548',
                )
btn.pack(anchor=W, pady=10, padx=40)

#отображение окна
window.mainloop()

# После редактирования в cmd нужно набрать данную команду
#pyinstaller --onefile dates.py