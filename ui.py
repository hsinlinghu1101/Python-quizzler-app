THEME_COLOR = "#375362"

from quiz_brain import QuizBrain
from tkinter import *


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.scores = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.scores.grid(row=0, column=1)
        self.canvans = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvans.create_text(150, 125, width=280, text="Hey", font=("Arial", 20, "italic"))
        self.canvans.grid(row=1, column=0, columnspan=2, pady=50)
        true = PhotoImage(file="./images/true.png")
        false = PhotoImage(file="./images/false.png")
        self.correct = Button(image=true, highlightthickness=0, command=self.selected_true_button)
        self.correct.grid(row=2, column=0)
        self.wrong = Button(image=false, highlightthickness=0, command=self.selected_false_button)
        self.wrong.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvans.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.scores.config(text=f"Score: {self.quiz.score}")
            self.canvans.itemconfig(self.q_text, text=question)
        else:
            self.wrong.config(state="disabled")
            self.correct.config(state="disabled")
            self.canvans.itemconfig(self.q_text, text="You've reached the end of the quiz.")

    def selected_true_button(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def selected_false_button(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
          self.canvans.config(bg="green")
        else:
          self.canvans.config(bg="red")
        self.window.after(1000, self.get_next_question)
