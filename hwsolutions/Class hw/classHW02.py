class Upper:

    def get_String():
        sentence = input("Please enter a string: ")
        return sentence

    def print_String(sentence):
        a = upper(sentence)
        print(a)

if __name__ == '__main__':
    u = Upper()
    sentence = u.get_String()
    u.print_String(sentence)