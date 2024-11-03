# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# The Quiz and Question classes define a particular quiz


class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ''
        self.question_text = ''
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while True:
            print(f"(T)rue or (F)alse: {self.question_text}")
            response = input("? ")

            if len(response) == 0:
                print('Not a valid response, please try again')
                continue

            if response.lower()[0] not in ('t', 'f'):
                print('Not a valid response, please try again')
                continue

            if response.lower()[0] == self.correct_answer:
                self.is_correct = True
            break


class QuestioncMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while True:
            print(self.question_text)
            for answer in self.answers:
                print(f'{answer.name}: {answer.text}')

            response = input("? ")

            if len(response) == 0:
                print('Not a valid response, please try again')
                continue

            if response.lower()[0] == self.correct_answer:
                self.is_correct = True

            break


class Answer:
    def __init__(self):
        self.text = ''
        self.name = ''
