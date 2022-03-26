# 단어공부
# 65~90 A~Z
# 97~122 a~z
import sys
input = sys.stdin.readline

words = input()
word_count = [0 for _ in range(26)]
for word in words:
    if 123 > ord(word) > 96:
        word_count[ord(word)-97] += 1
    elif 64 < ord(word) < 91:
        word_count[ord(word)-65] += 1

if word_count.count(max(word_count)) > 1:
    print('?')
elif word_count.count(max(word_count)) == 1:
    print(chr(word_count.index(max(word_count))+65))