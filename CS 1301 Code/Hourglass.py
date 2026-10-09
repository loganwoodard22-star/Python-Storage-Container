size=int(input("Please enter the size you want your hour glass to be (>=5): "))
border=input("Please enter border character: ")
fill=input("Please enter fill character: ")

#Prevents faulty outputs
while size < 5:
    print("Please enter a number greater than or equal to five")
    size=int(input("Please enter the size you want your hour glass to be (>=5): "))

#Actually starts the code when the proper inputs have been entered
if size >= 5:
    #This part draws the first part of the hourglass
    for i in range(1,size+1):
        for j in range(1,i+1):
            print(border,end="")
        print("")
        for k in range(1,size-1,-1):
            print(border,fill,end="")
#I cant figure it out I have tried all I could think of