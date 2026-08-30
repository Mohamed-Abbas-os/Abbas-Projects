questions=('How many elements are in the periodric table ?',
           'Which animal lays largest egg ? ',
           'What is the most abundant gas in the Earth atmosphere ?',
           'How many bones are in the human body ?',
           'Which is the hotest planet in the solar system ?')
options=(('A.116','B.117','C.118','D.119'),
         ('A.crocodile','B.hen','C.pigeon','D.ostrich'),
         ('A.nitrogen','B.oxygen','C.hydrogen','D.carbon-di-oxide'),
         ('A.205','B.206','C.208','D209'),
         ('A.mercury','B.venus','C.earth','D.jupiter'))
answers=['C','D','A','B','B']
guesses=[]
score=0
question_num=0
for question in questions:
    print('-------------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input('Enter (A,B,C,D):').upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print('CORRECT!')
    else:
        print('INCORRECT')
        print(f'correct answer is {answers[question_num]}')
    question_num+=1
print(f'your score is {score}/5')