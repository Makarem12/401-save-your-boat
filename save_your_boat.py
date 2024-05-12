
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display        
def play_game():
    word = "sweden"
    guessed_letters = []
    lives = 5

    print("Word:", display_word(word, guessed_letters))
    print("Lives remaining:", lives)
    print("hints:\n","1-country","\n2-located in northen Europe")
    
    while lives > 0:
        guess = input("Guess a letter (or type 'exit' to quit): ").lower()

        if guess == 'exit':
            print("Thanks for playing!")
            break

       

        if guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
            print("Word:", display_word(word, guessed_letters))
        else:
            lives -= 1
            print("Incorrect guess!")
            print("Lives remaining:", lives)

        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You've saved your boat!")
            break
        if lives == 1:
           print("You have one life remaining! Here's a hint:")
           print("it has the highest rate of entrepreneurship per capita")
    if lives == 0:
        print("Sorry, your boat drowned! The word was:", word)

if __name__ == "__main__":
    print("Welcome to Save Your Boat Game!")
    print("Description:")
    print("1) You have a boat that has 5 lives. When the boat's lives end, it will drown.")
    print("2) You should guess the word by choosing a letter from the English alphabet.")
    print("3) If you guess a letter wrong, you will lose a life.")
    print("4) When you guess the letter right, you will be provided with the updated word.")
    print("5) If you guess everything right, you will win.")
    print("6) If you finish your lives and did not guess the word, you will lose.")
    print("7) To quit, you can write 'exit'.")

    answer = input("Wanna play? (y/n): ")
    if answer.lower() == "y":
        play_game()
    else:
        print("Goodbye!")
