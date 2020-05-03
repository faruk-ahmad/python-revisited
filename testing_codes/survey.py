""" A module that defines a survey that we will use for how to test a class """

class AnnonymousSurvey():
    """ A class to represent an annonymous survey """

    def __init__(self, question):
        """ Initialize the attributes """
        self.question = question
        self.responses = []

    def show_question(self):
        """ A method to display the question """
        print(f'Q. {self.question}')

    def store_responses(self, response):
        """ A method to store the responses """
        self.responses.append(response)

    def show_responses(self):
        """ A method to display all the responses """
        print("Responses: ")
        for response in self.responses:
            print(f'- {response}')



if __name__ == '__main__':
    question = "What is your favorite language?"
    survey = AnnonymousSurvey(question)
    survey.show_question()
    
    while True:
        print("Input q to quit")
        response = input()
        if response == 'q':
            break
        survey.store_responses(response)

    print('All the reponses-')
    survey.show_responses()