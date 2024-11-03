# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# pyquiz.py -- Main starting point of the program
from quizmanager import QuizManager


class QuizApp:
    QUIZ_FOLDER = 'Quizzes'
    def __init__(self):
        self.username = ""
        self.quiz_manager = QuizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        # print the greeting at startup
        self.greeting()

        # ask the user for their name
        self.username = input("Please select your username: ")
        print(f'Welcome, {self.username}!')
        print()

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ Welcome to PyQuiz! ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu(self):
        self.menu_header()

        # get the user's selection and act on it. This loop will
        # run until the user exits the app
        selection = ""
        while True:
            selection = input('Please make a selection: ').capitalize()
            if len(selection) == 0:
                self.menu_error()
                continue

            if selection[0] == 'E':
                self.goodbye()
                break
            elif selection[0] == 'M':
                self.menu_header()
            elif selection[0] == 'L':
                print('\nAvailable quizzes are')
                self.quiz_manager.list_quizzes()
                print('---------------------\n')
            elif selection[0] == 'T':
                try:
                    quiz_number = int(input('Quiz number:'))
                    print(f'You have selected quiz number {quiz_number}')
                #     TODO start the quiz
                    self.quiz_manager.take_quiz(quiz_number,self.username)
                    self.quiz_manager.print_results()
                except:
                    self.menu_error()
            else:
                self.menu_error()

    # This is the entry point to the program
    def run(self):
        # Execute the startup routine - ask for name, print greeting, etc
        self.startup()
        # Start the main program menu and run until the user exits
        self.menu()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
