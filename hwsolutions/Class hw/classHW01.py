class romanNumerals:
    letters = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
    }
    def numbersToRomanNumeral (self,a): # a is the number received
        ans = '' # ans is the empty string of letters
        while a > 0:
            if a == 9: # Nine and Four are special numbers in roman numerals
                ans += 'IX'
                break
            if a == 4:
                ans += 'IV'
                break
            for x in self.letters:
                y = self.letters.get(x)
                if a >= y:
                    ans += x
                    a = a-y
                    break
        return ans
    def romanNumeralToNumbers (self,a): # a is the Roman Numeral received
        ans = 0

        while len(a) > 0:
            for x in a:
                for y in self.letters:
                    z = self.letters.get(y)
                    if x == y:
                        ans += z
                        a = a.replace(x,'')
                        break
        return ans
if __name__ == '__main__':
    r = romanNumerals()
    number = 343
    romanNumeral = 'DCLXXVI'
    ans1 = r.numbersToRomanNumeral(number)
    ans2 = r.romanNumeralToNumbers(romanNumeral)
    print(number, '==>',ans1)
    print(romanNumeral, '==>',ans2)