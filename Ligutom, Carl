userrrr = input("Enter a sentence: ").lower()
words = userrrr.split()
vowels = ('a', 'e', 'i', 'o', 'u')
vowelcount = 0
consonantcount = 0
out = ""

for word in words:
    if word[0] in vowels:  
        out += word.upper() + " "
        vowelcount += 1
    else: 
        out += word.lower() + " "
        consonantcount += 1

print("Transformed Word:", out.strip())
print("Words starting with vowel:", vowelcount)
print("Words starting with consonant:", consonantcount)