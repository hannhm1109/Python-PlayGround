name = input("Enter your name ! ")
print(f"Greetings {name} Welcome to your adventure!")
start = input("Would you rather play the game or perish ?")

if start == 'play':
    print("Great! Let's play the game!")
    setting = input("Want to go to the jungle or the desert ?")
else:
    print("Lame. okay you\'re dead now ....")
    quit()


if setting == 'jungle':
    print("Welcome to the mighty Amazon reinforest.. Your guide told you to stay here for a while ..")
    response = input("But he has been gone a long time... Follow him or wait here ?")
    if response == 'follow':
        print("You follow him into the tress...")
        transport = input("You see a caneo nearby. Walk or take the caneo down road")
    elif response == 'wait':
        print("You wait another ten minutes, and he still isnt here ")
    else :
        print("Invalid response! You lose !")
        quit()

elif setting == 'desert':
    print("Welcome to the mighty Sahara Desert.. Your guide told you to stay here for a while ..")
    response = input("But he has been gone a long time... Follow him or wait here ?")
    if response == 'Follow':
        print("You follow him into the tress...")
        transport = input("You see a caneo nearby. Walk or take the caneo down road")
    elif response == 'wait':
        print("You wait another ten minutes, and he still isnt here ")
    else :
        print("Invalid response! You lose !")
        quit()

else :
    print("Invalid Response You lose.")