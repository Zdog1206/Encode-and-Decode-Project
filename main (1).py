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
            print("The encoded password is", encoded_pas, ", and the original password is", encoded_pas,".")
            print("")
        if option == 3:
            break
