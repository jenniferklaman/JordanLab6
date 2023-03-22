
def encode(original_pass):
    ls_pass = list(original_pass)
    enc_pass = ""
    for i in (ls_pass):
        updated_pass = int(i) + 3
        string = str(updated_pass)
        enc_pass += string
    return enc_pass


def decode(password):
    password_lst = []
    decoded_password = ""

    try:

        for i in password:
            password_lst.append(i)

        for digit in password_lst:
            digit = int(digit)
            digit -= 3
            digit = str(digit)
            decoded_password += digit

        return decoded_password

    except TypeError as exc:
        print(exc)

def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')

original_pass = None

while True:

    menu()
    option_num = int(input('Please enter an option: '))
    if option_num == 1:
        original_pass = str(input('Please enter your password to encode: '))
        print('Your password has been encoded and stored!\n')
        encoded_pass = encode(original_pass)
    elif option_num == 2:
        if original_pass is None:
            print('No password to be decoded\n')
            continue
        decoded_pass = decode(encoded_pass)
        print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
    else:
        break


