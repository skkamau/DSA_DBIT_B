word = "hello world"
list_words = ["Hello","world","python"]
word_count = {}
for char in word:
   if char in word_count:
      word_count[char] += 1
      # word_count[char] = word_count[char] + 1
      print(word_count)
   else:
        word_count[char] = 1
        print(word_count)

print(f"The final result is {word_count}")