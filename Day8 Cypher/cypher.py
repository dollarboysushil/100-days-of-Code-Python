alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']






def encription(message_enc , num):
    i = 0
    encripted = ""
    for msg in message_enc:

        while i < 26:
            if alphabet[i] == msg:
                encripted = encripted + alphabet[i + num]

            i += 1
        i = 0
    print(encripted)


def decription(message_dec , num):
    i = 0
    decripted = ""
    for msg in message_dec:
        while i < 26:
            if alphabet[i] == msg:
                decripted = decripted + alphabet[i - num]

            i += 1
        i = 0
    print(decripted)


while True:
    print("Type 'encode' to encrypt and 'decode' to decrypt and 'quit' to terminate:  ")
    demand = input("").lower()

    if demand == 'encode':
        print("#################################")
        print("           ENCODING")
        print("#################################")
        message = input("Type Your Message: ")
        num1 = int(input("Type the shift number: "))
        encription(message, num1)
    elif demand == 'decode':
        print("#################################")
        print("           Decoding")
        print("#################################")
        message_dec = input("Type Your Message: ")
        num2 = int(input("Type the shift number: "))

        decription(message_dec, num2)

    elif demand == 'quit':
        break

    else :
        print("Enter Valid Input.")






