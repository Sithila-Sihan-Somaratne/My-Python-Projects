#This is UOM Python 2 
#Lesson 1.3: Dictionaries

############# Dictionaries #############

longest_words_dict = dict() 
longest_words_dict = {1:"Pneumonoultramicroscopicsilicovolcanoconiosis", 2:"Hippopotomonstrosesquippedaliophobia", 3:"Supercalifragilisticexpialidocious", 4:"Pseudopseudohypoparathyroidism"}

print(longest_words_dict)

print(longest_words_dict[2])
print(longest_words_dict.get(3))

longest_words_dict[5]="Honorificabilitudinitatibus"
print(longest_words_dict)

longest_words_dict[5]="Floccinaucinihilipilification"
print(longest_words_dict)

longest_words_dict[6]="Thyroparathyroidectomized"
print(longest_words_dict)

longest_words_dict.pop(6)
print(longest_words_dict)

longest_words_dict.clear()
print(longest_words_dict)
print("Dictionary is empty")

longest_words_dict = {1: "Pneumonoultramicroscopicsilicovolcanoconiosis", 2: "Hippopotomonstrosesquippedaliophobia", 3: "Supercalifragilisticexpialidocious", 4: "Pseudopseudohypoparathyroidism", 5: "Floccinaucinihilipilification", 6: "Antidisestablishmentarianism", 7: "Honorificabilitudinitatibus", 8: "Thyroparathyroidectomized", 9: "Dichlorodifluoromethane", 10: "Incomprehensibilities"}
for key in longest_words_dict:
    if key < 10:
        print(key, " "+longest_words_dict[key])
    else:
        print(key, longest_words_dict[key])

        

#       ----------      #



words = ["some", "any", "no", "every", "some", "any", "no", "every", "some", "any", "every", "some", "every", "every"]

counts = dict()

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1

print(counts)




