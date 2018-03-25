import collections # When we add a new variable, it determinde the place randomly.So, I imported this to sort the dict(key-value). BecauseExmp: merhaba mer erh rha... with this sort
#AYBERK SUNAL
#113200034

'''
nGramCounter Function
->To count the words which are divided with wanted number
->Parameters: String, Number
->Return: Number
->Example: rayrayroro, 4 =>  7
'''
def nGramCounter(aString, divide):
    ngram=0 #to count the amount of word
    letterList = list(aString) #to list the letters of the string
    if divide==0:
        return -1
    else:
        while (len(letterList) >= divide): #if the length of the list again bigger or equal wanted divide number
            ngram = ngram + 1 #count will increase
            letterList.pop(0) #it removes the first letter from the letter list
        return ngram


print nGramCounter('lalaland',4)


'''
nGramDict Function
->To show the divided words with iteration number
->Parameters: String ,  Number
->Return: Dictionary
->Example: 'rayrayroro',4 =>  [('rayr', 2), ('ayra', 1), ('yray', 1), ('ayro', 1), ('yror', 1), ('roro', 1)]

'''
def nGramDict(aString2, divide):
    word=[] #To store the created word with wanted number
    wordList=[] #To store the all created words
    dict=collections.OrderedDict() # To store the word and iteration number with key value
    count=0 #To count the iteration
    letterList = list(aString2) ##To list the letters of the string
    if divide==0:
        return -1
    else:
        while (len(letterList) >= divide):#If the length of the list again bigger or equal wanted divide number
            for i in range(0, divide):
                word.insert(3,letterList[i])
            str1 = ''.join(word) #To convert to a string the list
            del word[:] #To reset the list
            wordList.append(str1) #add the word to the list
            letterList.pop(0) #it removes the first letter from the letter list
        for a in wordList: #the word which will count
            for b in wordList: # the word which is comparing
                if  a==b: #iteration counter
                    count+=1
            dict[a]=count #dictionary value adder
            count = 0
        return dict

print nGramDict('rayrayroro',4)




