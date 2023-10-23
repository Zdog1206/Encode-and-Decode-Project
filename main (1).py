# Made by Zack Mankoff

def encoder(number):
    hi = list(number)
    num_list = ""
    for i in range(len(hi)):
        hi[i] = int(hi[i]) + 3
        if hi[i] >= 10:
            hi[i] = hi[i] - 10
        num_list += str(hi[i])
    return num_list

def decode_password(password_decoded):
    pass_decoded = ""
    for digit in password_decoded:
        digit_int = int(digit)
        if digit_int == 3:
            new_digit = 9
            pass_decoded += str(new_digit)
        elif digit_int == 2:
            new_digit = 8
            pass_decoded += str(new_digit)
        elif digit_int == 1:
            new_digit = 7
            pass_decoded += str(new_digit)
        else:
            new_digit = digit_int
            new_digit -= 3
            pass_decoded += str(new_digit)
    return pass_decoded




if __name__ == "__main__":

    while True:
        print("Menu\n---------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input("Please enter an option:"))


        if option == 1:
            input_option = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
            print("")
        if option == 2:
            encoded_pas = encoder(input_option)
            dec_pas = decode_password(encoded_pas)
            print("The encoded password is", encoded_pas, ", and the original password is", dec_pas,".")
            print("")
        if option == 3:
            break
