words = ["hello", "world", "spam", "eggs"]

#This is one method
counter = 0
max_index = len(words) - 1
while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1 

#Another method
print("\nAnother way :")
for i in range(len(words)) :
    print(words[i]+'!')

