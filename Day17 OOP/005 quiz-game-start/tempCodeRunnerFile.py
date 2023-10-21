from question_model import Question
from data import question_data



question_bank = []

for question in Question:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text , question_bank)
    question_bank.append(question_bank)
    
    
    
print(question_bank)