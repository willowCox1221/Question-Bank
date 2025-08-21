class question_bank:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_questions(self):
        return self.questions

    def clear_questions(self):
        self.questions.clear()


def clear_question_bank(qb):
    while True:
        action = input("Do you want to clear the question bank? (yes/no): ")
        if action.lower() == "yes":
            qb.clear_questions()
            print("Question bank cleared.")
            break
        elif action.lower() == "no":
            print("Question bank not cleared.")
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")


def add_questions(qb):
    while True:
        question = input("Enter a question or type quit to stop: ")
        if question.lower() == "quit":
            break
        qb.add_question(question)

    print("\nYour Question Bank:")
    for i, q in enumerate(qb.get_questions(), 1):
        print(f"{i}. {q}")


def view_questions(qb):
    questions = qb.get_questions()
    if questions:
        print("Current questions in the bank:")
        for i, q in enumerate(questions, 1):
            print(f"{i}. {q}")
    else:
        print("No questions in the bank.")


def main():
    qb = question_bank()  # ONE shared bank
    while True:
        action = input("Do you want to add a question, view questions, clear the bank, or exit? (add/view/clear/exit): ")
        if action.lower() == "add":
            add_questions(qb)
        elif action.lower() == "view":
            view_questions(qb)
        elif action.lower() == "clear":
            clear_question_bank(qb)
        elif action.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main()