word = str(input("Enter word"))
print(word)
revword=word[::-1]
print(revword)
if revword == word:
    print("YES")
else:
    print("NO")