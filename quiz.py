#FLASH CARD QUIZ APP
#Thought process:
# - There are several questions with choices and answers in "general.txt"
# - We need to extract one question at a time
# - Store each question (excluding the choices and answers) in its own variable
# - Do the same process with choices and answers
# - In the terminal, We need to print each question, choices for the question, and if the user gets the wrong answer, print the answer

#-----------------------------------------------------------------------------------------------

import random   #importing the random module

file_path = "general.txt"      #file containing the various questions

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()      # storing the contents in the file to the variable called content


def display_question(lines):
    question = lines[0]         #stores the question
    print(question)

def display_choices(lines,choices):
    for line in lines[1:]:                         #loops over the list from index 1
        line = line.strip()

        if line.startswith(("A","B","C","D")):      #checks whether the item in the list starts with(A,B,C,D)
            choices.append(line[2:])                #stores the items in the list called choices (Without A,B,C,D)

    random.shuffle(choices)                          #randomly shuffles the list

    for num,choice in enumerate(choices, start=1):
        print(f"{num}. {choice}")


def main():
    while True:
        questions = content.split("#Q")               #splits the content wherever there is "#Q"
        random.shuffle(questions)                     #randomly shuffles the questions
        choices = []                                  #empty list called choices to store the various choices
        score = 0                                     #final score

        for num in range(1,6):

            lines = questions[num].strip().splitlines()             #splits each question whenever there is a new line
            correct_answer = lines[1].replace("^", "").strip()      #stores the correct answer 

            print("\n")
            print("=============================================================")
            print(f"Question {num} of 5 ")
            print("=============================================================")

            display_question(lines)                       #calls the function "display_question"

            display_choices(lines,choices)                 #calls the function "display_choices"

            choices_copy = choices.copy()                  #replicates the choices list

            while True:
                answer = input("Enter your answer: ").strip()          #asks the user for an answer

                if answer.isdigit() and 1 <= int(answer) <= len(choices_copy):     #checks whether the user entered a valid answer
                    break
                else:
                    print("Invalid choice.......")          #if not, asks the user again for an answer

           
            answer_index = int(answer) - 1                  #converts the answer to an index

            selected_answer = choices_copy[answer_index]        #stores the choice at the user's index

            if selected_answer == correct_answer:              #checks for similarity
                print("Correct 🎉")
                score += 1                      #increases the score by 1

            else:
                print("❌ Incorrect.....")
                print(f"Correct answer: {correct_answer} ✅")           #outputs the correct answer

            choices.clear()                     #clears the choices list

        print("\n")

        print("You finished the quiz........")
        print(f"Your final score is: {score}/5")            #prints the final score
        print("\n")

        play_again = input("Do you want to play again(Y/N)? ").upper()         #asks the user to play again 

        if play_again == "Y":
            continue

        else:
            print("Thank you for playing.....")
            break


if __name__ == "__main__":
    main()