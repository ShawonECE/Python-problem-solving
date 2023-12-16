cipher = input("Enter your encrypted text: ")
key = int(input("Enter the key between 0 to 10: "))
text = ''
cip_len = len(cipher)

for i in range(0, cip_len - key, key + 1):
    text = text + cipher[i]
print(text)
