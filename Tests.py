from math import *

class Main:
    def __init__(self):
        self.mathWordFunctions = ["sin","cos","tan","floor","roof","pi","e","log","perm","comb","sinh","cosh","tanh","asinh","acosh","atanh","asin","acos","atan"]
        # Define the order of operations
        self.order = [self.mathWordFunctions,["(","^"],["*","/"],["+","-"]]
        # List of invalid characters in the input
        self.invalid_syntax = ["'",'"',"£","$","&","@",":",";","#","[","]","{","}","_","¬","`","="]
        # List of valid words for mathematical functions
        self.valid_words = ["sin","cos","tan","floor","roof","pi","e","log","perm","comb","sinh","cosh","tanh","asinh","acosh","atanh","asin","acos","atan","quit","q","","r"]
        # Initialize error tracking
        self.error = False
        self.error_type = None
        # to keep the program runninf
        self.running = True
        #internal logic for conversions
        self.estimate = False
        self.raidians = False

    def main(self):
        while self.running:
            # Get user input
            self.input = input("--> ")
            # Validate the input
            self.init_vaildate()
            
            self.primaryListCreation()
            # If there's an error, display it
            if self.error == True:
                self.throw_error()

    def init_vaildate(self):
        # Check for quit command
        if self.input.lower() == "q" or self.input.lower() == "quit":
            self.running = False
        # Check for invalid characters
        for char in self.input:
            if char in self.invalid_syntax:
                self.error = True
                self.error_type = "Syntax Error"
                break
            # Check for unmatched parentheses
            if char == "(":
                bracketsClose = False
                # Iterate from the last occurrence of "(" to the end of the input
                for x in range(self.input.rfind("("), len(self.input)):
                    # If a closing parenthesis is found, set bracketsClose to True and break the loop
                    if self.input[x] == ")":
                        bracketsClose = True
                        break
                # If no closing parenthesis is found, set an error
                if bracketsClose == False:
                    self.error = True
                    self.error_type = "Syntax Error"
                    break
        # Check for valid words in the input
        if any(c.isalpha() for c in self.input):
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

    def primaryListCreation(self):
        # Exit if there's an error or if the program is not running
        if self.error == True or self.running == False:
            return
        # Check if the last two characters are "~" to indicate radians are used
        #checks whether radians are used or not
        if self.input[-2] or self.input[-1] == "~":
            self.estimate = True
        
        # Check if the last character is "r" to indicate radians are used
        if self.input[-2] or self.input[-1] == "r":
            self.raidians = True

        # Initialize an empty list to store the processed input
        self.input_list = []
        inputString = ""
        # Iterate through each character in the input
        for char in self.input:
            if char == " ":
                pass
            # If the character is alphabetic and inputString is not empty, check if inputString is numeric
            elif char.isalpha() and inputString != "":
                if inputString.isalpha() == False:
                    self.input_list.append(inputString)
                    inputString = char
                else:
                    inputString += char
            # If the character is numeric and inputString is not empty, check if inputString is numeric
            elif char.isnumeric() and inputString != "":
                if inputString.isnumeric() == False:
                    self.input_list.append(inputString)
                    inputString = char
                else:
                    inputString += char
            # If the character is alphabetic, append it to inputString
            elif char.isalpha():
                inputString += char
            elif char.isnumeric():
                inputString += char
            # If inputString is not empty, append it to input_list and reset inputString
            elif inputString != "":
                self.input_list.append(inputString)
                inputString = ""
                self.input_list.append(char)
            else:
                self.input_list.append(char)
        # If inputString is not empty after the loop, append it to input_list
        if inputString != "":
            self.input_list.append(inputString)

        self.basicLogic()
        
    def basicLogic(self):
        if all(item.isalpha for item in self.input_list ):
            print("Letters")
            return
            
if __name__ == "__main__":
    calculator = Main()
    calculator.main()
