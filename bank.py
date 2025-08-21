class question_bank:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_questions(self):
        return self.questions

    def clear_questions(self):
        self.questions.clear()