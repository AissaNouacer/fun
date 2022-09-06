import random


class GussingGame:

    def __init__(self):
        self.score = 0
        print("Please guess the number between 0..10 ... you have 5 times to guess wrong")
        self.rand_num = random.randint(0,11)

        while self.score >= -5:
            if self.rand_num %2 == 0:
                print("the number is divisble by 2")
            else:
                print("the number is not even")
            user_input = int(input("> "))
            if user_input == self.rand_num:
                self.score += 1
                print("Your score is : ", self.score)
                self.rand_num = random.randint(0,11)
            else:
                self.score -= 1
                print("Your score is : ", self.score)

            if self.score == 10:
                print("Congratulations, you won the game.")
                print("Your score is : ", self.score)
                break
        if self.score <= -5 :
            print("Game Over, you lose.... try agin!")



if __name__ == "__main__":
    GussingGame()
