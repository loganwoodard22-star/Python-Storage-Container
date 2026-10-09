def countwords(sentence):
    counter=0
    inword=False
    for character in sentence:
        if character.isalpha()==True:
            if inword==False:
                counter+=1
                inword=True
            else:
                pass
        else:
            inword=False
        
    print(f"Your sentence has {counter} words")


countoperation=True
while countoperation==True:
    sentence=input("Enter a sentence to check how many word it has: ")
    countwords(sentence)
    retry=input("Would you like to test another sentence (y/n): ")
    if retry == "y":
        countoperation=True
    else:
        print("Exiting Program")
        countoperation=False
        exit    