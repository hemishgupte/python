class QuizApp:
    def _init_(self):
        self.__questions = [
            "What is the capital of France?",
            "Which programming language is this quiz written in?",
            "What is 2 + 2?"
        ]
        
        self.__options = [
            ["Paris", "London", "Berlin", "Madrid"],
            ["Python", "Java", "C++", "Ruby"],
            ["3", "4", "5", "6"]
        ]
        
        self.__answers = [0, 0, 1]  
        
        self.__score = 0
    
    
    def display_question(self, index):
        print(f"Q{index + 1}: {self.__questions[index]}")
        for i, option in enumerate(self.__options[index]):
            print(f"{i + 1}. {option}")
    
    
    def check_answer(self, question_index, user_answer):
        if user_answer == self.__answers[question_index]:
            return True
        else:
            return False
    
    
    def start_quiz(self):
        print("Welcome to the Python Quiz!")
        print("You will be asked multiple-choice questions. Select the number corresponding to your answer.\n")
        
        
        for index in range(len(self.__questions)):
            self.display_question(index)
            
            # Input answer from the user
            try:
                user_answer = int(input("Your answer (1-4): ")) - 1  # Adjusting for 0-based index
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")
                continue
            
            # Check if the answer is correct
            if user_answer < 0 or user_answer > 3:
                print("Invalid choice! Please choose between 1 and 4.")
                continue
            
            if self.check_answer(index, user_answer):
                print("Correct!\n")
                self.__score += 1 
            else:
                print(f"Wrong! The correct answer was: {self._options[index][self._answers[index]]}\n")
        
        
        print(f"Quiz Finished! Your final score is: {self._score}/{len(self._questions)}")



quiz_app = QuizApp()


quiz_app.start_quiz()