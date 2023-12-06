def shortest_palindrome(s):
    def is_palindrome(string):
        return string == string[::-1]

    for i in range(len(s) - 1, -1, -1):
        if is_palindrome(s[:i + 1]):
            return s[i + 1:][::-1] + s


input_1 = "aacecaaa"
output_1 = shortest_palindrome(input_1)
print(f"Output for input '{input_1}': {output_1}")

input_2 = "abcd"
output_2 = shortest_palindrome(input_2)
print(f"Output for input '{input_2}': {output_2}")
