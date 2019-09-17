# Unnar Sigurðsson



# Movement function
def movement(a_str):

    return a_str


# Movement_input function
def movement_input():
    a_str = str(input("Direction: "))
    return a_str


# Tiles
def tiletraveller(blabla):
    #Tiles   
    a = "nN"
    b = "nN"
    c = "nN"
    d = "nNsSeE"
    e = "sSwW"
    f = "nNsS"
    g = "sSeE"
    h = "aAwW"
    i = "sSwW"

    if a.count(blabla) >= 1:
        return blabla
    else:
        print("Vitlaust")

    return 0


# ef a_str er n, þá má fara áfram, en þá þarf ég að halda utan um 
# Avalible Tiles
a_str = "n"

a_input = movement_input()
print(a_input)

print(tiletraveller(a_input))

#print(movement(a_str))






