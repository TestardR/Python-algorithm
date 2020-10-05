def rev_word(str):
    return " ".join(reversed(str.split()))


def rev_word1(str):
    return " ".join(str.split()[::-1])


def rev_word2(str):
    words = []
    length = len(str)
    space = [' ']

    i = 0

    while i < length:
        if str[i] not in space:
            word_start = i

            while i < length and str[i] not in space:
                i += 1

            words.append(str[word_start:i])

        i += 1

    return ' '.join(reversed(words))


print(rev_word1('hello mamacita'))
