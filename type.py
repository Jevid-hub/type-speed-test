from time import time

sen = "this is your typing speed test"
print(">>",sen)

start = time()
givensen = input (">> ")
end = time()

total_characters = len(sen)
total_characters_given = len(givensen)
r = min(total_characters , total_characters_given)
correct_characters = 0


for i in range(r):
    if sen[i] == givensen[i]:
        correct_characters += 1


time_taken = round((end-start),2)
cpm = round((correct_characters/time_taken)*60)
wpm = cpm/4
acc = round((correct_characters/total_characters)*100,2)



print("Clicks per min :",cpm)
print("Words per min :",wpm)
print("Accuracy :",acc)


print("Correct characters :", correct_characters)
print("Time taken :",time_taken)
