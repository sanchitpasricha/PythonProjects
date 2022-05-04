import encrypt_dcrypt
import logo

print(logo.logo)
direction = input("Type 'Encode' to Encrypt and Type 'Decode' to Decrypt\n")
text = input('Type your message :: \n').lower()
shift = int(input("Enter the shift number :: "))

if direction == 'encode':
    Etext = encrypt_dcrypt.caesar(text, shift, 'encode')
    print(Etext)
elif direction == 'decode':
    Dtext = encrypt_dcrypt.caesar(text, shift, 'decode')
    print(Dtext)
else:
    print("Wrong Input!")