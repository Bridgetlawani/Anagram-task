# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    # find_anagrams["earth", "heart"]
    word1 = word1.strip()
    word2 = word2.strip()

    if(sorted(word1) == sorted(word2)):
        print(True)
    else:
        print('false')

        # return True
        #print(find_anagrams('earth', 'heart'))
find_anagrams('peach', 'cheap')

