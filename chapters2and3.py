def print_lol(a_list, indent=False, level=0):
    """Prints each item in a list, recursively descending
       into nested lists (if necessary)."""

    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item, True, level + 1)
        else:
            if indent:
                for l in range(level):
                    print("\t"),
            print(each_item)


a = [5, 6, 7, 8, 9, 10]

print_lol(a)

b = [1, 2, 3, ["a", "b", "c"], 9, 10]

print_lol(b)

person = {"name": "Jack", "age": 34}

print(person)

print(person.viewkeys())

cities = set(("Paris", "Lyon", "London", "Berlin", "Paris", "Birmingham"))

print(cities)

c = (1, 2, 3)

print(c)


# chapter 2
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)


# chapter 3
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

# final part of chapter 3
vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)

