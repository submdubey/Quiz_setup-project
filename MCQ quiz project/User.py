from Super import Super

class User:
    user={}
    marks=0
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name

    def takequiz(self):
        choose = input("\n Enter the quiz you want to take either Gs or Maths:")
        level = input("\n Enter the difficulty level you want either easy or hard :")
        if choose.lower()=='Gs' or level.lower()== 'easy':
            for val in Super.GS_ques_easy:
                print(val)
                for i in range(len(Super.options[val])):
                    print(str(i+1) + ":",Super.options[val][i])
                ans=input()
                if Super.GS_ques_easy[val]==ans:
                    User.marks+=1
                    User.user[self.user_id]=User.marks

        elif choose.lower()=='Gs' or level.lower()== "hard":
            for val in Super.GS_ques_hard:
                print(val)
                for i in range(len(Super.options[val])):
                    print(str(i+1) + ":",Super.options[val][i])
                ans=input()
                if Super.GS_ques_hard[val]==ans:
                    User.marks+=2
                    User.user[self.user_id]=User.marks

        elif choose.lower() == 'Maths' or level.lower() == "easy":
            for val in Super.Maths_ques_easy:
                print(val)
                for i in range(len(Super.options[val])):
                    print(str(i+1) + ":", Super.options[val][i])
                ans = input()
                if Super.Maths_ques_easy[val] == ans:
                    User.marks +=1
                    User.user[self.user_id] = User.marks

        elif choose.lower() == 'Maths' or level.lower() == "hard":
            for val in Super.Maths_ques_hard:
                print(val)
                for i in range(len(Super.options[val])):
                    print(str(i+1) + ":", Super.options[val][i])
                ans = input()
                if Super.Maths_ques_hard[val] == ans:
                    User.marks +=2
                    User.user[self.user_id] = User.marks

    def result(self):
        print("\n****[RESULT}****\n")
        print("Easy ques having 1 marks each")
        print("Hard ques having 2 marks each")
        res= int(input('Enter your rollno.:'))

        print(self.name,'Has obtained',User.user[res],"marks")
        User.marks=0
        print('\n Right options for the questions were')
        for val in Super.GS_ques_easy.values():
            print(val)
        for val in Super.GS_ques_hard.values():
            print(val)
        for val in Super.Maths_ques_easy.values():
            print(val)
        for val in Super.Maths_ques_hard.values():
            print(val)


