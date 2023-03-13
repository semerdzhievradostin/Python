#Write your code below this line 👇

def prime_checker(number):
    flag = False

    if number == 1:
        print("It's not a prime number.")
    elif number > 1:
    # check for factors
        for i in range(2, number):
            if (number % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break

    # check if flag is True
        if flag:
            print("It's not a prime number.")
        else:
            print("It's a prime number. ")
        



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
