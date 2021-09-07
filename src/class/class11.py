class Dog:
    tricks = [] # attribute scope: class level attribute

    def __init__(self, name):
        self.name = name

    def addTrick (self, trick):
        self.tricks.append(trick)
    
if __name__ == '__main__':
    fido = Dog('fido')
    fido.addTrick('roll over')

    print(f'fido can: {fido.tricks}')

    buddy = Dog('buddy')
    buddy.addTrick('play dead')

    print(f'fido can: {buddy.tricks}') # both fido and buddy share the same class level attribute: tricks