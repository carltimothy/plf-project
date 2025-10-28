
sentence = input("Enter a sentence: ")


words = sentence.split()


vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
vowel_count = 0
consonant_count = 0
transformed_words = []

for word in words:
    if word[0] in vowels:  
        transformed_words.append(word.upper())
        vowel_count += 1
    else: 
        transformed_words.append(word.lower())
        consonant_count += 1

print("\nTransformed Word:", " ".join(transformed_words))
print("Words starting with vowel:", vowel_count)
print("Words starting with consonant:", consonant_count)