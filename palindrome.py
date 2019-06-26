word = input("Enter your word: ")
reverse_word = ""

for i in range(len(word)-1,-1,-1):
  reverse_word += word[i]

if word == reverse_word:
  print(f"{word} is a palindrome.") 
  
else:
  print(f"{word} is not a palindrome.")