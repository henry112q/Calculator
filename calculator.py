from math import *
# take an input and split it down so that we can check each fuction
# be able to throw an error if invalid syntax without the program quiting
class Main:
    def __init__(self):
        self.order = [["(","^"],["*","/"],["+","-"]]
        self.invalid_syntax = ["'",'"',"£","$","&","@",":",";","#","[","]","{","}","_","¬","`","="]
        self.valid_words = ["sin","cos","tan","floor","roof","pi","e","log","perm","comb","sinh","cosh","tanh","asinh","acosh","atanh","asin","acos","atan","quit"]
        self.error = False
        self.error_type = None
        self.running = True
        self.estimate = False
        
    def main(self):
        
        while self.running:
            
            self.input = input("--> ")
            self.init_vaildate()
            
            if self.error == True:
                self.throw_error()
                
    def init_vaildate(self):
        
        if self.input.lower() == "q" or self.input.lower() == "quit":
            self.running = False
            
        for char in self.input:
            
            if char in self.invalid_syntax:
                self.error = True
                self.error_type = "Syntax Error"
                break
                
            if char == "(":
                bracketsClose = False
                for x in range (
                                self.input.rfind("("),
                                len(self.input)):
                    
                    if self.input[x] == ")":
                        bracketsClose = True
                        break
                    
                if bracketsClose == False:
                    self.error = True
                    self.error_type = "Syntax Error"
                    break
        if any(c.isalpha() and c.lower() not in ["q"] for c in self.input):
            self.word_Vaildation()
        
        
    def word_Vaildation(self):
        
        word = ""
        
        for x in range(len(self.input)):
            
            if self.input[x].isalpha():
                word += self.input[x]
                
            else:
                if word.lower() in self.valid_words:
                    word = ""
                    
                else:
                    self.error = True
                    self.error_type = "Syntax Error"
                    break
                
        if word.lower() not in self.valid_words:
            self.error = True
            self.error_type = "Syntax Error"
                            
            
    
    def throw_error(self):
        print(self.error_type)
        self.error = False
        self.error_type = None

if __name__ == "__main__":
    calculator = Main()
    calculator.main()
