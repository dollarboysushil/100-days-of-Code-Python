


user_input = int(input("Enter your number:"))

def prime_checker(num):
    div = 2
    while div <= num:
        ans = num % div
        if ans == 0:
            if div != num:
                print("Entered number is not a Prime Number.")
                div = div + num
            elif (div == num):
                print("Entered number is a Prime Number.")
        div += 1

prime_checker(user_input)

