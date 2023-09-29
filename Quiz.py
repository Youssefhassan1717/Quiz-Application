class Quiz:
    def __init__(self):
        self.questions = {}
        self.score = 0

    def add_question(self, question, correct_answer):
        self.questions[question] = correct_answer

    def display_questions(self):
        for question in self.questions.keys():
            print(question)

    def take_quiz(self):
        print("Welcome to the Quiz!")
        for question, correct_answer in self.questions.items():
            print(question)
            user_answer = input("Your answer: ")
            if user_answer.lower() == correct_answer.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}\n")
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


class Administrator:
    def create_quiz(self):
        quiz = Quiz()
        num_questions = int(input("Enter the number of questions for the quiz: "))
        for _ in range(num_questions):
            question = input("Enter the question: ")
            correct_answer = input("Enter the correct answer: ")
            quiz.add_question(question, correct_answer)
        return quiz



if __name__ == "__main__":
    admin = Administrator()
    quiz = admin.create_quiz()
    quiz.take_quiz()
