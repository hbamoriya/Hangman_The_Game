import random
from hangman_art import stages, logo
from hangman_words import word_list
while True:
    print(logo)
    end_of_game = False
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    display = []     #displaying the empty underscores of the word 
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()      

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}.")

        if not "_" in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])
    play_again = input("want to play again? Y/N ")   
    if play_again=='Y':
        continue
    else:
        print("Thank You For Playing")
        break
