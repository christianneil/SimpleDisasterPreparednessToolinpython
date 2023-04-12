#DISASTER PREPAREDNESS TOOLKIT
# Ask the user for their name, location, and the type of disaster they are preparing for
name = input("What is your name? ")
location = input("Where are you located? ")
disaster = input("What kind of disaster are you preparing for (earthquake, typhoon, or flood)? ")
print()

# Print out a message  with information and advice specific to the disaster they're preparing for
if disaster == "earthquake":
    print(f"Hello {name}, based on your location in {location}, it appears you are at risk of experiencing an earthquake. It is important to take the following precautions to ensure your safety:\n")
    print("-Secure your furniture and other objects to prevent them from falling or toppling over")
    print("-Identify safe spots in each room, such as under a sturdy table or against an interior wall, where you can take cover.")
    print()

elif disaster == "typhoon":
    print(f"Hello {name}, based on your location in {location}, it appears you are at risk of experiencing a typhoon. To keep yourself safe during this type of disaster, please consider the following precautions:")
    print("-Stay tuned to local news and weather reports for updates on the storm's progress.")
    print("- Stay indoors and away from windows during the storm.")
    print("-If you lose power, turn off major appliances and unplug smaller electronics to protect them from power surges when power is restored.")
    print("-If you must evacuate, follow the instructions of local authorities and take your emergency kit with you.")
    print()
elif disaster == "flood":
    print(f"Hello {name}, based on your location in {location}, it appears you are at risk of experiencing a flood. To stay safe during this type of disaster, please take the following precautions:")
    print("-Elevate important belongings and documents to protect them from flood damage")
    print("-Know the safest routes to higher ground and have a plan for evacuation")
    print("-Monitor the weather and stay informed through local news and weather reports")
    print()
# If the user's response is not one of the specified options, the code then reminds them to always be prepared for any type of disaster
else:
    print(f"Hello {name}, you are located in {location}. It's important to be prepared for any kind of disaster that may occur.")
    print()
# Define a dictionary of essential items with default values set to False
essentials = {
    "Water bottles (at least 500ml each)": False,
    "Long-lasting snacks": False,
    "Small battery-powered radio": False,
    "Flashlight": False,
    "Extra batteries": False,
    "Whistle": False,
    "First aid kit": False,
    "Dust masks": False,
    "Emergency Cash": False,
    "Copies of important documents (birth certificates,  etc.)": False,
    "Updated map of the area": False,
}
#for loop is used to iterate to over each item in the dictionary.Asking them  with a y/n question
for item in essentials:
    response = input(f"Do you have {item}? (y/n) ")
    #if the user responds with  y , the corresponding value in the "essentials" dictionary is set to "True",indicating nga the user has that item
    if response.lower() == "y":
        essentials[item] = True
    #if the user responds with n, the value remains "False"

#this  displays a list of items that the user still needs to acquire for their kit.
#this if statement check if any of the values in the "essential" dictionary are equal to "False"
if False in essentials.values():
    print("Based on your responses, you still need to acquire the following items:")
    #the for loop  iterates over the "essential" dictionary with the items with a value of "False" and prints it
    for item, value in essentials.items():
        if not value:#if the value is "False" this statement will run
            print(f"- {item}") 
            
#else, meaning if there are no "False" values in the "essential" dictionary ,then the  program prints a congratulating message to the user for being well-prepared for potential disaster         
else:
    print("Congratulations! Based on your responses, it appears you are well-prepared for potential disasters.")
                                      