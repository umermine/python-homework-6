#Adding variables
sum = input("Enter a prompt ")
#Writing code
for char in sum:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        print("The prompt contains alphabets")
        break
    else:
        print("It does not contain alphabets")