def reverse_words(s):
    # Split the string into words
    words = s.split('.')
    # Reverse the order of the words
    reversed_words = words[::-1]
    # Join the words back together with a '.' between them
    reversed_string = '.'.join(reversed_words)
    return reversed_string

# Input string
S = "i.like.this.program.very.much"
# Output
output = reverse_words(S)
print(output)

