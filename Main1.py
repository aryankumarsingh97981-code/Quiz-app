# Main interface 
import json
from question_bank import Question
from tkinter import *
interface_window = Tk()
interface_window.title("QUIZ APP AND SCOREBOARD")
interface_window.config(bg= "White")
interface_window.geometry("800x600")
# ........................................................................................................

# labeling for all variable.......................................

# quiz title
quiz_title = Label(interface_window,text = "Quiz game",font =("Arial",20), fg = "red" )
quiz_title.pack(pady = 15)
# **************************************************************************************
# question
question_label = Label(interface_window,text = "",font = ("Arial",18),fg = "black")
question_label.pack(pady = 15)
# ******************************************************************************************
# score
score_label = Label(interface_window,text = "")
score_label.pack(pady = 5)
# *********************************************************************************************
# result correct/wrong
result_label = Label(interface_window,text = "")
result_label.pack(pady = 5)
# *****************************************************************************************************
# quiz ended

quiz_ended = Label(interface_window,text = "",font = ("Arial",18),fg = "black")
quiz_ended.pack(pady = 5)
# *********************************************************************************************************
# ending wish

ended_wish = Label(interface_window,text = "",font = ("Arial",20),fg ="Red")
ended_wish.pack(pady = 5)

# .........................................................................................................................
name_label = Label(interface_window,text = "Enter Name :",font = ("Arial",16))
name_label.pack(pady = 10)
# ......................................................................
get_name = Entry(interface_window,text = "",font = ("Arial",14),justify = "center",fg = "red",width = 20)
get_name.pack(pady = 5)


    


#  check answer 
current_question =[0]
score = [0]
answered = [False] # this condition is use because user not press answer button................
def check_answer(answer):
        if answered[0]:#user press the button this condition is false.................
            return
        answered[0] = True #this condition is true and it work.....................
        q = Question[current_question[0]]
        if answer==q["answer"]:
            score[0]+=1# answer is correct added the score.................
            result_label.config(text = "Correct",fg = "Green",font = ("arial", 12))
        else:
             result_label.config(text=f"Wrong!\nCorrect Answer: {q['answer']}",fg="red",
                font=("Arial",12))

        score_label.config(text = f"Your score:{score[0]}/{len(Question)}",font = ("arial",15))

# check the option....................
def option1_click():
        check_answer("A")
def option2_click():
        check_answer("B")
def option3_click():
        check_answer("C")
def option4_click():
        check_answer("D")

# ..........................................................................................................................................
# user press the button.............................

option1 = Button(interface_window,text = "",font = ("arial",14),fg = "green",
        command = option1_click         )
option1.pack(pady = 6)
option2 = Button(interface_window,text = "",font = ("arial",14),fg = "green",
        command = option2_click        )
option2.pack( pady = 6)
option3 = Button(interface_window,text = "",font = ("arial",14),fg = "green",
        command = option3_click)
option3.pack(pady = 6)
option4 = Button(interface_window,text = "",font = ("arial",14),fg = "green",
        command = option4_click         )
option4.pack(pady = 6)

# .......................................................................................................................................
# show the question and option ..............................

buttons = [option1,option2,option3,option4]#first of all the option store in list......................
def show_question():
        q = Question[current_question[0]]
        question_label.config(text =q["question"])
        for i in range(4):#then use loop .................
            buttons[i].config(text = q["option"][i])
        score_label.config(text = f"Your score:{score[0]}/{len(Question)}",font = ("arial",15))
# ........................................................................................................
# def save_score():
#     name = get_name.get()

#     with open("score.txt", "a") as f:
#         f.write(f"Name :{name}\n")
#         f.write(f"Score: {score[0]}/{len(Question)}\n")
#         f.write("________________________________\n")
        
def save_score():
    with open("score_history.json", "r") as file:
        history = json.load(file)

    history.append({
        "name": get_name.get(),
        "score": score[0]
    })

    with open("score_history.json", "w") as file:
        json.dump(history, file, indent=4)
        

# .............................................................................................................................................

def next_question():

        answered[0]= False #user press the next question button further this condition is false................
        result_label.config(text = "")
        current_question[0]+=1
        
        if current_question[0]<len(Question):
            show_question()
        else:
            save_score()
            question_label.config(text = "")
            quiz_ended.config(text="Quiz Finished")
            ended_wish.config(text = "THANK YOU")
            score_label.config(text = f"Your score:{score[0]}/{len(Question)}",font = ("arial",15))
            for button in buttons:
                button.pack_forget()

                #this use for change the question previous option is remove and new option show............
            get_name.pack_forget()
            name_label.pack_forget()
            next_button.pack_forget()

                #this use for ended the quiz next button is remove....................
            retry_button.pack(pady = 10)
        
        
        
                    
next_button = Button(interface_window,
text="Next question",bg = "green",font = ("arial",20),
command=next_question)
next_button.pack(pady = 15)

def retry_quiz():
    current_question[0] = 0
    score[0] = 0
    answered[0] = False
    question_label.config(text = "")
    result_label.config(text="")
    quiz_ended.config(text="")
    ended_wish.config(text="")
    score_label.config(text=f"Your score: {score[0]}/{len(Question)}")

    for button in buttons:
        button.pack(pady=6)
    next_button.pack(pady=15)
    retry_button.pack_forget()
    show_question()
    
    

retry_button = Button(interface_window,text="Retry Quiz",font=("Arial", 18),bg="blue",fg="white",
command=retry_quiz)
show_question()
interface_window.mainloop()




