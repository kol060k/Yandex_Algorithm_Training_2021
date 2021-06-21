import sys

def create_dict():
    word_dict = {}
    n = int(input())
    for i in range(n):
        word = input()
        if word.lower() in word_dict:
            word_dict[word.lower()].extend([i for i in range(len(word)) if word[i] < 'a'])
        else:
            word_dict[word.lower()] = [i for i in range(len(word)) if word[i] < 'a']
    return word_dict


def check_text(word_dict):
    errors = 0
    text = sys.stdin.read().split()
    for word in text:
        stress = [i for i in range(len(word)) if word[i] < 'a']
        if len(stress) != 1:
            errors += 1
        else:
            stress = stress[0]
            if word.lower() in word_dict and stress not in word_dict[word.lower()]:
                errors += 1
    return errors

        
word_dict = create_dict()
errors = check_text(word_dict)
print(errors)