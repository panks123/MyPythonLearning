import  random
def my_custom_random(s,e,i):
  exclude=[i]
  randInt = random.randint(s,e)
  return my_custom_random(s,e,i) if randInt in exclude else randInt
def jumble_word(first_name, lastt_name, number):
    for i in range(0, number):
        # Changing the last name
        joumbled_name = first_name[i] + " " + lastt_name[my_custom_random(0, number - 1,i)]
        print(joumbled_name)


if __name__ == "__main__":
    # Length of the name list
    number = int(input("Enter the number of names:\n"))

    nameList = []
    first_name = []
    lastt_name = []

    # Asking the name of the friends
    for i in range(1, number + 1):
        name = input("Enter the name:")
        # append to the name list
        nameList.append(name)

    # Spliting the elements of the name list
    for ele in nameList:
        split_name = ele.split(" ")
        # For the first name
        first_name.append(split_name[0])
        # For the second name
        lastt_name.append(split_name[1])

    jumble_word(first_name, lastt_name, number)