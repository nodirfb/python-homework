def reverse_string(str):
    return str[::-1]
def count_vowels(str):
    vowels = 'aeiou'
    count = 0
    for i in str:
        n = vowels.count(i)
        count += n
    return count
