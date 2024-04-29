class Main:
    def __init__(self):
        # Define the order of operations
        self.order = [["(","^"],["*","/"],["+","-"]]
        # List of invalid characters in the input
        self.invalid_syntax = ["'",'"',"£","$","&","@",":",";","#","[","]","{","}","_","¬","`","="]
        # List of valid words for mathematical functions
        self.valid_words = ["sin","cos","tan","floor","roof","pi","e","log","perm","comb","sinh","cosh","tanh","asinh","acosh","atanh","asin","acos","atan","quit","q",""]
        # Initialize error tracking
        self.error = False
        self.error_type = None
        self.running = True
        self.estimate = False

    def main(self):
        while self.running:
            # Get user input
            self.input = input("--> ")
    
    def inputlistformer(self):
        self.inputlist = []
if __name__ == "__main__":
    main = Main
    main.main()