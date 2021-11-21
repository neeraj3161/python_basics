class AnonymousSurvey:
    "collect anonymous answers to a survey questions"
    def __init__(self,question):
        "store and question and prepare for respose"
        self.question=question
        self.response=[]
    def show_question(self):
        "show the survey question"
        print(self.question)
    def store_response(self,new_response):
        "store a single response to the survey"
        self.response.append(new_response)
    def show_results(self):
        'show the final results altogether'
        print("Anonymous responses are mentioned below")
        for response in self.response:
            print('response : '+str(response))

