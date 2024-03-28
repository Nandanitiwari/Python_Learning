import re
pattern = r"[A-Z]egular"
text = '''A Regular Expression or RegEx is a special sequence of characters that uses a search pattern to find a string or set of strings.
It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern into one or more sub-patterns.
Regex Module in Python:-
Python has a built-in module named “re” that is used for regular expressions in Python. We can import this module by using the import statement.'''

matches = re.finditer(pattern, text)
for match in matches:
   print(match.span())
   print(type(match.span()))
   print(text[match.span()[0]:match.span()[1]])
