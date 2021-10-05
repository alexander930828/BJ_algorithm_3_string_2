#6

word = input().split()
print(len(word))


#7

a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)

else:
    print(b)


#8

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()

ret = 0

for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3

print(ret)


#9

cro_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in cro_word:
    word = word.replace(i, '*')
print(len(word))


# 10

n = int(input())

group_word = 0

for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1): # 인덱스 범위 생성: 0부터 단어 개수 -1까지
        if word[index] != word[index+1]: # 연달은 두 문자가 다를 때;
            new_word = word[index+1:] # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0: # 남은 문자열에서 현재 글자가 있었다면
                error += 1
    if error == 0:
        group_word += 1

print(group_word)