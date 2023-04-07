from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = quiz_brain
        self.window = Tk()
        self.window.title("Quizimodo")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.flashcard = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.flashcard.create_text(150, 125, width=260, text=f"Question", fill=THEME_COLOR,
                                                        font=("Arial", 20,
                                                              "italic"))
        self.flashcard.grid(padx=50, pady=50, column=0, row=1, columnspan=2)
        self.right = PhotoImage(file="images/true.png")
        self.wrong = PhotoImage(file="images/false.png")
        self.right_button = Button(image=self.right, highlightthickness=0, command=self.true_button)
        self.right_button.grid(column=0, row=2, rowspan=2)
        self.wrong_button = Button(image=self.wrong, highlightthickness=0, command=self.false_button)
        self.wrong_button.grid(column=1, row=2, rowspan=2)
        self.player_score = Label(text=f"Score:{self.score.score}", bg=THEME_COLOR, fg="black", font=("Arial", 12, "italic"))
        self.player_score.grid(column=1, row=0)

        self.get_next_q()


        self.window.mainloop()

    def get_next_q(self):
        try:
            q_text = self.quiz.next_question()
            self.flashcard.itemconfig(self.question_text, text=f"{q_text}")
            self.flashcard.config(bg="white")
        except IndexError:
            self.flashcard.config(bg="white")
            self.flashcard.itemconfig(self.question_text, text=f"No more questions, restart the game or quit")

    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.player_score.config(text=f"Score:{self.score.score}/{len(self.quiz.question_list)}")
        self.give_feedback(is_right)


    def false_button(self):
        is_right = self.quiz.check_answer("false")
        self.player_score.config(text=f"Score:{self.score.score}/{len(self.quiz.question_list)}")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right and self.quiz.check_answer:
            self.flashcard.config(bg="green")
        else:
            self.flashcard.config(bg="red")
        self.window.after(1000, self.get_next_q)
