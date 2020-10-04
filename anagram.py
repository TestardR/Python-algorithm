def is_anagram(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


is_anagram('Hello', 'dzdzd')


def is_anagram2(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    count = {}

    for l in s1:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1

    for l in s2:
        if l in count:
            count[l] -= 1
        else:
            count[l] = 1

    for l in count:
        if count[l] != 0:
            return False
        return True

print(is_anagram2('Hello', 'elloH'))
