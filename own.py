name= input("type your name: ")
print( "welcome", name, " to this adventure!")

answer= input("you areon a dirt road, it has come to the end of your journey , choose right or left, which way would you like to choose")

if answer== "left":
    answer=input("you come to a river, you can walk around it or swim accross it")

    if answer=="swim":
        print(" you swam across and were eaten by crocodiles")
    elif answer=="walk":
         print(" you walked for miles and passed out ")
    else:
      print("not a valid option , you loose!")
    


elif answer== "right":
    answer= input(" you come to a bridge , it looks woobly , do you want to cross it or head back")
    

    if answer=="back":
        print(" you go back and loose")
    elif answer=="cross":
        answer= input(" you cross the bridge and meet a stranger. Do you talk to them")
    
        if answer=="yes":
         print("you talk to the stranger and they give you gold")

        elif answer== "no":
         print(" you got offended , you loose ")

        else:
         print(" not a valid option, you loose!")

    else:
    
       print("not a valid option , you loose!")

else:
      print("not a valid option , you loose!")

print("thank you for trying ")
  

