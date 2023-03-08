# importing the question class into our project.
from questions import Question

# this is an array that is to have the questions and also the answers.
question_prompts = [
    "What colors are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colors are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colors are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
    "The combination of the Sun's light is called?\n(a) Spectrum\n(b) Rainbow\n(c) White Light\n\n",
    "What is the color of Water?\n(a) Transparent\n(b) Colourless\n(c) White\n\n",
    "Do Snakes have legs?\n(a) Yes\n(b) No\n(c) Sometimes\n\n"
]

# An array to hold the questions in this quiz
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b")
]


def ask_question(question_ask):
    score = 0
    answers_given = []
    for question in question_ask:
        print()
        answer = input(question.prompt)
        answers_given.append(answer)
        if answer == question.answer:
            score += 1

    print("You got", str(score) + "/" + str(len(question_ask)), "questions correct.\nYour answers were", answers_given)


ask_question(questions)
