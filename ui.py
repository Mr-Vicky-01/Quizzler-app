from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=500, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(250, 125, text="Testing Code", font=("Arial", 20, "italic"),
                                                     width=480)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        self.score_label = Label(text="score: 0", highlightthickness=0, fg="white", bg=THEME_COLOR,
                                 font=("arial", 18, "bold"))
        self.score_label.grid(row=1, column=2)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.correct)
        self.true_button.grid(row=3, column=1)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.wrong)
        self.false_button.grid(row=3, column=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.window.quit()

    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
