sentence = list(input("Enter a string: "))
collected  = {}
for i in range(len(sentence)):
    if sentence[i] not in collected:
        collected[sentence[i]] = 1
    else:
        collected[sentence[i]] +=1
print(collected)