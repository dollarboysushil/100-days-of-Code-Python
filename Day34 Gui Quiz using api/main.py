import requests


parameters ={
    "amount":10,

    "type":"boolean"


}

response = requests.get("https://opentdb.com/api.php" , params=parameters)
response.raise_for_status()
data= response.json()

data = data['results']
print(data)


for question in data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    print(question_text)
    print(question_answer)