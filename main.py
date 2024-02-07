#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    if word1 == '' or word2 == '':
        anagram = False
        return anagram
    anagram = True
    letters1 = []
    letters2 = []
    word1 = word1.replace(' ','')
    word2 = word2.replace(' ','')
    word1 = word1.lower()
    word2 = word2.lower()
    for letter in word1:
        letters1.append(letter)
    for letter in word2:
        letters2.append(letter)
    for letter in letters1:
        if letter in letters2:
            continue
        else:
            anagram = False
            break
    for letter in letters2:
        if letter in letters1:
            continue
        else:
            anagram = False
            break
    return anagram

if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    word1 = input()
    word2 = input()
    print(anagram(word1, word2))
    