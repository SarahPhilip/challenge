import re
fname =  "paragraph_3.txt"
with open(fname, 'r') as f:
    paragraph = f.read().replace('\n', ' ')
    words = re.split(' ', paragraph)
    word_count = len(words)
letter_count = []
for word in words:
	letter_count.append(len(word))
avg_letter_count = sum(letter_count)
sentence_count = len(re.findall(r'\.', paragraph))
print("Paragraph Analysis")
print("-" * 25)
print("Approximate word count: " +str(word_count))
print("Approximate sentence count: " +str(sentence_count))
print("Average Letter Count:" +str(sum(letter_count)/word_count))
print("Average sentence length:" + str(word_count/sentence_count))