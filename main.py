import random
import string


print("Message Encryption/Decryption Program")
print("1. Encryption\n2. Decryption")
choice = int(input("Enter your choice : "))
l = []
if choice == 1:
    messages = input("Enter your message here : ")   
    lst = messages.split(" ") 
    for message in lst:
        if len(message) < 3:
            encrypt_message = message[::-1]
            l.append(encrypt_message)
        else:
            character_pool = string.ascii_letters
            random_string1 = "".join(random.choices(character_pool, k=3))
            random_string2 = "".join(random.choices(character_pool, k=3))
            first_char = message[0]
            rest_message = message[1:]
            encrypt_message = f"{random_string1+rest_message+first_char+random_string2}"
            l.append(encrypt_message)
    print(f"Your Encrypting message : {" ".join(l)}")

elif choice == 2:
    messages = input("Enter your message here : ")
    lst = messages.split(" ")
    for message in lst:
        if len(message) < 3:
            decrypt_message = message[::-1]
            l.append(decrypt_message)
        else:
            left_trim_message = message[3:]
            right_trim_message = left_trim_message[:-3]
            last_char = right_trim_message[-1]
            rest_message = right_trim_message[:-1]
            decrypt_message = f"{last_char+rest_message}"
            l.append(decrypt_message)
    print(f"Your Decrypt message : {" ".join(l)}")
