#from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import requests

request = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')
requested_questions = request.json()["results"]

question_bank = []

for question in requested_questions:
    new_question = Question(requested_questions[len(question_bank)]["question"],
                            requested_questions[len(question_bank)]["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")