import random
class Password_generator:
    def __init__(self,number,symbol,letter):
        self.letter=letter
        self.symbol=symbol
        self.number=number
    
        return None
    def password(self):
        n_letter=int(input("letter\n"))
        n_symbol=int(input("symbol\n"))
        n_number=int(input("number\n"))
        password_list=[]
        for i in range(1,n_letter+1):
            char=random.choice(self.letter)
            password_list+=char
        for i in range(1,n_symbol+1):
            char=random.choice(self.symbol)
            password_list+=char
        for i in range(1,n_number+1):
            char=random.choice(self.number)
            password_list+=char
        random.shuffle(password_list)
        return "".join(password_list)

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','r','s','t','w','x','y','z']
symbol=['!',"@",'#',"$","%","^","&","*",('(',')'),'?','/']
number=['1','2','3','4','5','6','7','8','9','0']

p=Password_generator(letter,symbol,number)
print(p.password())    
