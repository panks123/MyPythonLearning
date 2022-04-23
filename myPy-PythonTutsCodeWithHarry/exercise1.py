#Excercise3
dict1={"abandon":"https://dictionary.cambridge.org/dictionary/english/abandon",
       "ashtonished":"https://www.merriam-webster.com/dictionary/astonished",
       "anguish":"https://www.merriam-webster.com/dictionary/anguish",
       "sorrow":"https://www.dictionary.com/browse/sorrow",
       "tickle":"https://www.dictionary.com/browse/tickle"}


inp=input("Enter a word: ")

if inp in dict1.keys():
    print("To know the meaning, visit this link : ",dict1[inp])
else:
    print("Sorry!!! This word is not in this dictionary")
