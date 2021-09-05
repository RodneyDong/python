sentence =  'I am so happy to learn Python which makes me happy, my parents happy, and also interested in Python Python Python Python Python.'

def convertToWords(a):
    words = a.split()
    for x in words: # Deletes punctuation marks
        newString = ''
        for y in x:
            z = y.isalpha()
            if z == True:
                newString += y
        words[words.index(x)] = newString
    return words
    # Receives a string and convert to list with only words

def removeMultipleWords(a):
    b = set(a)
    c = list(b)
    return c
    # receives a list of words and delete all words that are the same

def tupleList (a,b): # Receives a non-repetitive word list and a repetitve word list
    list1 = []
    for x in a:
        count = 0
        for y in b:
            if x == y:
                count += 1
            singleTuple = (x,count)
            if count > 0:
                list1.append(singleTuple)
    return list1
# Counts the number of repetitive words and returns it as a tuple list
def listToDict (a):
    b = dict(a)
    return b

if __name__ == '__main__':
    # sentenceWords = convertToWords(sentence)
    # singleWords = removeMultipleWords(sentenceWords)
    # tupleList = tupleList(singleWords, sentenceWords)
    # finalResult = listToDict(tupleList)
    # print(finalResult)
    x = sentence.split()
    d = {}
    for i in x:
        if i.endswith(',') or i.endswith('.'):
            i=i[:len(i)-1]
        if i in d:
            d[i] = d.get(i)+1 # get the exsiting value and add 1, put it back
        else:
            d[i] = 1 # create key-value pair and give default value 1.
    print(d)