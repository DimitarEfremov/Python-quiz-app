# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# The Quiz and Question classes define a particular quiz
import datetime
import random


class Quiz:
    def __init__(self):
        self.name = ''
        self.description = ''
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        self.completion_time = 0
        pass

    def print_header(self):
        print("\n\n*******************************************")
        print(f'YOUR QUIZ IS: {self.name}')
        print(f'DESCRIPTION: {self.description}')
        print(f'QUESTIONS: {len(self.questions)}')
        print(f'TOTAL POINTS: {self.total_points}')
        print("*******************************************\n")

    def print_results(self, quiz_taker):
        print("*******************************************")
        print(f'DATE: {datetime.datetime.today()}')
        print(f'TIME TO COMPLETE: {self.completion_time} NEEDED')
        print(f'{quiz_taker} total score is {self.score}!!!')
        print(f'QUESTIONS: {self.correct_count} out of {len(self.questions)} are correct')
        print(f'SCORE: {self.score} out of {self.total_points}')
        print("*******************************************\n")

    @property
    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        self.completion_time = 0

        for q in self.questions:
            q.is_correct = False

        # TODO: print the header
        self.print_header()

        # TODO: execute each question and record the result
        random.shuffle(self.questions)

        start_time = datetime.datetime.now()

        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.score += q.points
                self.correct_count += 1

        if self.correct_count != len(self.questions):
            want_to_redo = input(
                f'It seems you have answered some questions incorrect, do you want to redo? (y/n): ').lower()
            if want_to_redo[0] == 'y':
                wrong_qs = [q for q in self.questions if q.is_correct is False]

                for q in wrong_qs:
                    q.ask()
                    if q.is_correct:
                        self.score += q.points
                        self.correct_count += 1

        end_time = datetime.datetime.now()
        self.completion_time = end_time - start_time
        self.completion_time = datetime.timedelta(seconds=round(self.completion_time.total_seconds()))

        print('---------------------------------------------\n')

        return self.score, self.correct_count, self.total_points, self.completion_time
