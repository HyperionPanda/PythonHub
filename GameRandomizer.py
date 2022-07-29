import random

def GameRandomizer():
    gamelist = list()
    inputs = str(input("Put in a new game, or put exit: "))
    
    while True:
        gamelist.append(inputs)
        inputs = str(input("Put in a new game, or put exit: "))
        if inputs == "exit":
            break

    numberlist = list()
    
    while True:
        
        number = len(gamelist)
        testnumber = random.randrange(0, number)
        numberlist.append(testnumber)
        
        for num in numberlist:
            
            if numberlist.count(num) == 50:
                print(gamelist)
                print()
                print(numberlist)
                return print(gamelist[num])
          

            
        
        








GameRandomizer()
