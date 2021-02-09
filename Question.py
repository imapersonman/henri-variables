class Question:
    def __init__(self, msg: str, answer):
        self.msg = msg
        self.answer = answer
    
    def __repr__(self):
        return self.msg
    
    def check_answer(self, possible_answer):
        return self.answer(possible_answer)
