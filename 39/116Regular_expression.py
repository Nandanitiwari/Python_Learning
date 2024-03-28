import re
pattern = "Regular"
text = '''A Regular Expression or RegEx is a special sequence of characters that uses a search pattern to find a string or set of strings.
It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern into one or more sub-patterns.
Regex Module in Python:-
Python has a built-in module named “re” that is used for regular expressions in Python. We can import this module by using the import statement.'''

match = re.search(pattern, text)
print(match)