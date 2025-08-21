class question_bank:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_questions(self):
        return self.questions

    def clear_questions(self):
        self.questions.clear()

def main():
    qb = question_bank()

    while True:
        question = input("Enter a question (or type 'quit' to stop): ")
        if question.lower() == "quit":
            break
        qb.add_question(question)

    print("\nYour Question Bank:")
    for i, q in enumerate(qb.get_questions(), 1):
        print(f"{i}. {q}")

if __name__ == "__main__":
    main()