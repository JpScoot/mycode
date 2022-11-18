#!/bin/evn/ python3

#print title of project
print("How well do you know the 90's hit sictcom Martin?")

#create var for question(s)
question_1 = "What was DragonFly Jones' real job?"
question_2 = "Where did the character 'Tommy' work at?"
question_3 = "Who won a one on one date with guest star 'Kid' from the hip hop group Kid n Play?"


def main():

#print questions
    print(question_1)

    #print out all possible answers
    print("A. Karate Instructor")
    print("B. Mechanic")
    print("C. Dentist")
    print("D. Mayor")

    #create a while statement
    condition = True
    while condition:
        # indenting these lines so they fall under the while loop
        #create answer input
        answer_input = input("Choose an answer\n>").capitalize()

        answer = answer_input
        # check if answer is a correct one:
        if answer in ["A","B","C","D"]:
            break
        else:
            print("You must choose A, B, C, or D.")
            # this will cause the while loop to repeat, so they must type in an answer again

    #if statement
    if answer == "A":
        print("Get to steppin!.. try again!")
    elif answer == "B":
        print("Wazzup, Wazzup, Waaazzzzuuuupppp!..you chose right!")
    elif answer == "C":
        print("Get to steppin!.. try again!")
    elif answer == "D":
        print("Get to steppin!.. try again!")
    else:
        print("smh..Nope, try again!")

#run main function
if __name__ == "__main__":
    main() 
