# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# QuizManager manages the quiz content
import os.path
import os
from os import *
import quizparser
import datetime


class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        # the most recently selected quiz
        self.the_quiz = None

        # initialize the collection of quizzes
        self.quezzes = dict()

        #: stores the results of the most recent quiz
        self.results = None

        #: the name of the person taking the quiz
        self.quiz_taker = ''

        # make sure that the quiz folder exists
        if not os.path.exists(quizfolder):
            raise FileNotFoundError('The quiz folder does not exist')
        else:
            self._build_quiz_list()

    # build the list of quizzes

    def _build_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)
        # parse the XML files in the directory
        for i, f in enumerate(dircontents):
            if f.is_file():
                parser = quizparser.QuizParser()
                self.quezzes[i + 1] = parser.parse_quiz(f)

    #  print a list of the currently installed quizzes
    def list_quizzes(self):
        for k, v in self.quezzes.items():
            print(f'{k}: {v.name}')

    # start the given quiz for the user and return the results
    def take_quiz(self, quizid, username):
        self.quiz_taker = username
        self.the_quiz = self.quezzes[quizid]
        self.results = self.the_quiz.take_quiz

    # prints the results of the most recently taken quiz
    def print_results(self):
        self.the_quiz.print_results(self.quiz_taker)

    # save the results of the most recent quiz to a file
    # the file is named using the current date as
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)
    def save_results(self):
        pass


if __name__ == "__main__":
    qm = QuizManager("Quizzes")
    qm.list_quizzes()
