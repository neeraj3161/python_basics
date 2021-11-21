from survey_class import AnonymousSurvey

# asking the question
question='What language did you first learn to speak??'
# creating a instance
my_survey=AnonymousSurvey(question)
# storing the question
my_survey.question=question
# showing the question
my_survey.show_question()
print('press q to quit')

# to get multiple input of answers we are stating the while loop

while True:
    response=input("Enter your response : ")
    if response=='q':
        break
    my_survey.store_response(response)
print('Thank you for your response!!')
my_survey.show_results()


