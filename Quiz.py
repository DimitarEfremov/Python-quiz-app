# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# The Quiz and Question classes define a particular quiz


class Quiz:
    def __init__(self):
        self.name = ''
        self.description = ''
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        pass

    def print_header(self):
        print("\n\n*******************************************")
        print(f'YOUR QUIZ IS: {self.name}')
        print(f'DESCRIPTION: {self.description}')
        print(f'QUESTIONS: {len(self.questions)}')
        print(f'TOTAL POINTS: {self.total_points}')
        print("*******************************************\n")

    def print_results(self):
        print("*******************************************")
        print(f'Your total score is {self.total_points}!!!')
        print("*******************************************\n")

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False

        # TODO: print the header
        self.print_header()

        # TODO: execute each question and record the result
        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.score += q.points
                self.correct_count += 1

        print('---------------------------------------------\n')

        return self.score, self.correct_count, self.total_points