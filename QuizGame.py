def ask_question(question, correctAnswer):
    userAnswer = input(question).strip().lower()
    return userAnswer == correctAnswer

def main():
    print("Welcome to the Game!")

    play = input("Do you want to play? (yes/no) ").strip().lower()

    if play != "yes":
        print("Ok, have a great day")
        return

    print("Then let's start!")

    questions = [
        ("What does CPU stand for? ", "central processing unit"),
        ("What does GPU stand for? ", "graphics processing unit"),
        ("What does RAM stand for? ", "random access memory")]

    score = sum(ask_question(q,a) for q,a in questions)

    
    total_questions = len(questions)
    percentage = (score/total_questions) * 100

    print(f"You got {score} questions correct")
    print(f"Which means you got {percentage:.2f}%")

if __name__ == "__main__":
    main()