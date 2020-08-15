#For the following practice question you will need to write code in Python in the workspace below.\
# This will allow you to practice the concepts discussed in the \Scripting lesson, such as reading\
#  and \
# writing files. You will see some older concepts too, but again, we have them there \
# to review and reinforce\
# your understanding of those concepts.

#Question: Create a function that opens the flowers.txt, reads every line in it, and saves \
# it as a dictionary.\
# The main (separate) function should take user input \
# (user's first name and last name) and parse the user input\
# to identify the first letter of the first name.\
#  It should then use it to print the flower name with the same first \
# letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower
def flower_name():

    flower_text = str(input("Enter your First [space] name only: "))
    while (len(flower_text.split('" "')) != 1):
        flower_text = str(input("Enter your First [space] name only: "))

    flowers = {}
    with open("flowers.txt" , "r") as f:
        for line in f.readlines():
            v = line.split(':')
            flowers[v[0]] = v[1].strip('\n')
    f.close()
    first_letter = str(flower_text)[0].capitalize()
    print(flowers.get(first_letter))


flower_name()


# HINT: create a dictionary from flowers.txt

# HINT: create a function
        