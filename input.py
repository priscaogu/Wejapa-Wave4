#Write a script that does the following:

#Ask for user input 3 times. Once for a list of names, once for a list of missing assignment\
#  counts, and once for a list of grades. Use this input to create lists for names, assignments,\
#  and grades.
#Use a loop to print the message for each student with the correct values. \
# The potential grade is simply the current grade added to two times the number\
#  of missing assignments.
#Template code for your script:


def student():
    names = str(input('enter a list of names seperated by comma :')).strip().split(',')  # get and process input for a list of names

    assignments = str(input('enter a list of assignment seperated by comma : ')).split(',')
    # get and process input for a list of the number of assignments
    #assignment_list = assignments.split()
    grades = str(input('enter a list of grades seperated by comma: ')).split(',') # get and process input for a list of grades
    print(names)
    print(assignments)
    print(grades)

    for (i, j, k) in zip(names, assignments, grades):
        potential_grade = int(k) + 2 * int(j)
        print(potential_grade)
        message = "Hi {},\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"
        print(message.format(i, j, k, potential_grade ))


    return potential_grade
student()

# message string to be used for each student
# HINT: use .format() with this string in your for loop

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
