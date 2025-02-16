def firstRepeatedCharacter(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return "No repeated characters"

s = "abcabcbb"
print(firstRepeatedCharacter(s))