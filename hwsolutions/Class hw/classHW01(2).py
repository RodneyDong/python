class RomanNumerals:
    letters = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
    }

    def numbers_to_roman_numeral(self,romanNum):
        for x in self.letters:
            lettersValue = self.letters.get(x) # Get the value of x from the dict above 
            if romanNum >= lettersValue: #Only runs if romanNum is greater or equal to x, else, loops back to the next x value
                divide = romanNum//lettersValue # romanNum divides by x and rounds to the smaller whole number
                if romanNum == 9: # Because 9 and 4 is IX and IV and can't be displayed in the program, set a if for this case
                    print('IX', end='') # Prints the values horizontally
                    break
                if romanNum == 4:
                    print('IV', end='')
                    break
                romanNum %= lettersValue # Changes romanNum into the remainder after divided by x
                print(x*divide, end='')

if __name__ == '__main__':
    r = RomanNumerals()
    r.numbers_to_roman_numeral(4124)