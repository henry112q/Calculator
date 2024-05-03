from math import *

class Main:
    def __init__(self):
        self.mathWordFunctions = ["sin","cos","tan","floor","roof","pi","e","log","perm","comb","sinh","cosh","tanh","asinh","acosh","atanh","asin","acos","atan"]
        # Define the order of operations
        self.order = [self.mathWordFunctions,["(","^"],["*","/"],["+","-"]]
        # List of invalid characters in the input
        self.invalid_syntax = ["'",'"',"£","$","&","@",":",";","#","[","]","{","}","_","¬","`","="]
        # List of valid words for mathematical functions
        self.valid_words = ["sin","cos","tan","floor","roof","pi","e","log","perm","comb","sinh","cosh","tanh","asinh","acosh","atanh","asin","acos","atan","quit","q","","r","h","help"]
        # Initialize error tracking
        self.error = False
        self.error_type = None
        # to keep the program runninf
        self.running = True
        #internal logic for conversions
        self.estimate = False
        self.raidians = False
        self.help = False
        self.input_list = []
    
    def main(self):
        while self.running:
            # Get user input
            self.input = input("--> ")
            # Validate the input
            self.init_vaildate()
            
            # Check for valid words in the input
            if any(c.isalpha() for c in self.input):
                self.word_Vaildation()
                
            self.primaryListCreation() # Ensure this is called before basicLogic
            
            self.basicLogic() # Now, input_list should be defined
            
            # If there's an error or help request, display it
            if self.help == True:
                self.Help()
            if self.error == True:
                self.throw_error()
            
    def Help(self):
        print("The list of supported functions is",self.valid_words,"\nA list of invalid inputs is",self.invalid_syntax,"\nAll bracktes must be closed and syntax must be correct with most commands being followed by brackets par Perm and Comb \nThese must first have a number directly before and after with no brackets")
        self.help = False
    
    def init_vaildate(self):
        # Check for quit command
        if self.input.lower() == "q" or self.input.lower() == "quit":
            self.running = False
        if self.input.lower() == "h" or self.input.lower() == "help":
            self.help = True
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
        # Exit if there's an error or if the program is not running or the user requires help
        if self.error == True or self.running == False or self.help == True:
            return
        if len(self.input) >= 2:
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
    
    def WordLogic(self):
        return
    
    def sublistLogic(self):
        if any(item.isalpha() for item in self.sublist):
            self.WordLogic
            return
        return
        
        
        
    def basicLogic(self):
        
        if self.error == True or self.running == False or self.help == True:
            return
        
        if all(item.isalpha() for item in self.input_list ):
            self.WordLogic()
        
        for pos in self.input_list:
            if pos == "(":
                count = 0
                location = self.input_list.index(pos)
                for posnum in range(location,len(self.input_list)):
                    if self.input_list[posnum] == ")":
                        count += 1
                        break
                    count += 1
                self.sublist = []
                for x in range(0,count):
                    self.sublist.append(self.input_list[x+location])
                for x in range(0,count):
                    self.input_list.pop(location)
                self.sublist.pop(0)
                self.sublist.pop(-1)
                print(self.sublist)
                print(self.input_list)
                self.input_list.insert(location,self.sublist)
                print(self.input_list)

            if pos in ["*", "/"]:
                location = self.input_list.index(pos)
                oprator = pos
                preNumber = self.input_list[location-1]
                # Initialize an empty list to hold the sublist
                sublist = [preNumber, oprator]
                # Iterate through the remaining elements to find the next operator or end of list
                for i in range(location+1, len(self.input_list)):
                    if self.input_list[i] in ["+", "-"]:
                        break
                    sublist.append(self.input_list[i])
                # Remove the elements from the original list
                # Collect indices to remove
                indices_to_remove = list(range(location-1, i))

                # Remove items in reverse order to avoid index shifting
                for index in sorted(indices_to_remove, reverse=True):
                    self.input_list.pop(index)
                # Insert the sublist back into the original list
                self.input_list.insert(location-1, sublist)
                print(self.input_list)
if __name__ == "__main__":
    calculator = Main()
    calculator.main()
    