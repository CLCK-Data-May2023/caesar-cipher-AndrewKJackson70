#define unencrypted alphabet as a list
original_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#gain original message from user
message = input("Please enter the message you want to encrypt: ")
#define where to shift in the index
shift = 5 
#used to convert list into a dictionary
cipher = {}
cipherText = " "
#ensures that input is converted to lowercase to match output constraints
message = message.lower()

#converting each entry in the dictionary into an integer and defining the correct range for those integers, defning the shift
for i in range(0, 26):
    letter = original_alpha[i]
    shifted_letter = original_alpha[(i + shift)%26]
    cipher[letter] = shifted_letter

#for each letter, we are applying the shift conditions, returning the shift condition and also not shifting spaces or unexpected characters/symbols 
for letter in message:
    if letter in original_alpha:
        letter = cipher[letter]
        cipherText = cipherText + letter
    else: 
        cipherText = cipherText + letter

print(cipherText)