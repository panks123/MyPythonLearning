# else with for loop

for item in ["roti","sabzi","chawal"]:
    print(item)

else:                                    # if the for loop executes completely then this else block will execute
    print("For loop has eneded properly")

for item in ["roti","sabzi","chawal"]:
    print(item)
    break

else:
    print("For loop has ended properly")


for item in ["roti","sabzi","chawal"]:
    if item=='paratha':
        break

else:
    print("Your item was not found")

for item in ["roti","sabzi","chawal"]:
    if item=='roti':
        print("Your item was found")
        break

else:
    print("Your item was not found")

