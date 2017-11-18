answers = {
		"привет": "И тебе привет!",
		"как дела": "Лучше всех",
		"пока": "Увидимся"
	}

def get_answer(question, answers=answers):
	#question = input("Something: ")
	question = question.lower()
	return answers.get(question)

question1 = input("Something: ")
result = get_answer(question1, answers)
print(result)        