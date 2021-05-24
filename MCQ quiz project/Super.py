class Super:
    GS_ques_easy = {}
    GS_ques_hard = {}
    Maths_ques_easy = {}
    Maths_ques_hard = {}
    options = {}
    super_user = {}

    def __init__(self,s_id,s_name):
        self.s_id = s_id
        self.s_name = s_name
        print('Hey',s_name,"You can set the Quiz")

    def setQuestion(self):
        while True:
            quiz = input("Do you want to set quiz on some other topic ?(yes/no)")
            if (quiz.lower()=='yes'):
                topic = input("Enter the topic which you want to set on quiz (GS/Maths):")
                difficulty = input("\n Enter the difficulty level of quiz either easy or hard :")

                if topic.lower()=='GS' or difficulty.lower()=='easy':
                    No_of_ques = int(input("\n How many ques you want to set on quiz :"))
                    for val in range(No_of_ques):
                        question = input("\n Enter the question:")
                        option = input("\n Enter your options seperated by space: ").split()
                        Super.options[question]=option
                        answer=input("\n Enter the answer")
                        Super.GS_ques_easy[question]=answer
                elif topic.lower()=='GS' or difficulty.lower()=="hard":
                    No_of_ques = int(input("\n How many ques you want to set on quiz :"))
                    for val in range(No_of_ques):
                        question = input("\n Enter the question:")
                        option = input("\n Enter your options seperated by space: ").split()
                        Super.options[question] =option
                        answer = input("\n Enter the answer")
                        Super.GS_ques_hard[question] =answer

                elif topic.lower()=='Maths' or difficulty.lower()== 'easy':
                    No_of_ques = int(input("\n How many ques you want to set on quiz"))
                    for val in range(No_of_ques):
                        question = input("\n Enter the question:")
                        option = input("\n Enter your options seperated by space: ").split()
                        Super.options[question]=option
                        answer=input("\n Enter the answer")
                        Super.Maths_ques_easy[question]=answer

                elif topic.lower() == 'Maths' or difficulty.lower() == 'hard':
                    No_of_ques = int(input("\n How many ques you want to set on quiz"))
                    for val in range(No_of_ques):
                        question = input("\n Enter the question:")
                        option = input("\n Enter your options seperated by space: ").split()
                        Super.options[question] =option
                        answer = input("\n Enter the answer")
                        Super.Maths_ques_hard[question] = answer

            else:
                break

    def addQuestion(self):
        while True:
            add_ques = input("Do you want to add question ? (yes/no):")
            if add_ques.lower()=="yes":
                topic=input("Enter the topic where you want your ques to be added (GS/Maths):")
                difficulty=input("\n Enter the difficulty level of the ques either easy or hard :")

                if topic.lower()=='Gs' or difficulty.lower()=='easy':
                    question=input("\n Enter your question:")
                    option=input("\n Enter your option seperated by space :").split()
                    Super.options[question]=option
                    answer = input("\n Enter the answer")
                    Super.GS_ques_easy[question]=answer

                elif topic.lower()=='Gs' or difficulty.lower()=='hard':
                    question=input("\n Enter your question:")
                    option=input("\n Enter your option seperated by space :").split()
                    Super.options[question]=option
                    answer = input("\n Enter the answer")
                    Super.GS_ques_hard[question]=answer

                elif topic.lower()=='Maths' or difficulty.lower()=='easy':
                    question = input("\n Enter your question:")
                    option = input("\n Enter your option seperated by space :").split()
                    Super.options[question]=option
                    answer = input("\n Enter the answer")
                    Super.Maths_ques_easy[question]=answer

                elif topic.lower() =='Maths' or difficulty.lower()== 'hard':
                    question = input("\n Enter your question:")
                    option = input("\n Enter your option seperated by space :").split()
                    Super.options[question]=option
                    answer = input("\n Enter the answer")
                    Super.Maths_ques_hard[question] = answer
            else:
                break




