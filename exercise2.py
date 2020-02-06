import logging

def checkPermutation( string1, string2 ):
    if len( string1 ) != len( string2 ):
        return False
    letters = {}
    for letter in string1:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    for letter in string2:
        if letter in letters:
            letters[letter]-=1
        else:
            return False
    for _, quantity in letters.items():
        if quantity != 0:
            return False
    return True


def main():
    test_correct = checkPermutation('aacdb','baadc')
    test_incorrect = checkPermutation('aaabbcc','baccbba')
    print('The test 1 returns ', test_correct)
    print("the test 2 returns", test_incorrect)

main()