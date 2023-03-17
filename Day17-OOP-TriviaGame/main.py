from question_model import Question
from data import question_data
from quiz_brain import Brain


question_bank = []

for q in question_data:
    question = q["question"]
    answer = q["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)


quiz = Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()