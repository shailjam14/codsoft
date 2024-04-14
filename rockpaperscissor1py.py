import random
class game:
    def __init__(self, user_choice,computer_choice):
        self.user_choice=user_choice
        self.computer_choice=computer_choice
    def rps(self):

        if (self.user_choice==self.computer_choice):
            print("draw")
        elif ((self.user_choice-self.computer_choice)%3==1):
            print("you win!")
        else:
            print("you lose!")
        
       
g=game(int(input()),random.randint(0,2))
print(g.rps())
print(g.computer_choice)
print(g.user_choice)