class QuestionMachine:
    def __init__(self, questions):
        self.questions = questions
        self.current_index = 0
    
    def ask(self):
        if self.current_index >= len(self.questions):
            return "You're done! Congratulations!"
        return self.questions[self.current_index]
    
    def answer(self, answer):
        if self.current_index >= len(self.questions):
            print("No more questions!")
        question = self.questions[self.current_index]
        response_prefix = "Question: {}\nAnswer: {}\n".format(self.questions[self.current_index], answer)
        if (question.check_answer(answer)):
            self.current_index += 1
            print("{}Correct!".format(response_prefix))
            print("\nNext Question: {}".format(self.ask()))
        else:
            print("{}Incorrect.  Try again.".format(response_prefix))