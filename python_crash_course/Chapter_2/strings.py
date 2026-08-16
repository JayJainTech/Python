# Variables
message = "Hello World"
print(message)

# F-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}!"
print(message)

# Capitalization
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Tab
print("\tPython")

# New line
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace
favorite_language = ' python '
print(f"{favorite_language}Is there a space?")
print(f"{favorite_language.rstrip()}Is there a space?")
print(f"{favorite_language.lstrip()}Is there a space?")
print(f"{favorite_language.strip()}Is there a space?")
print(f"{favorite_language}Is there a space?")

# Removing Prefixes
nostarch_url = "https://nostarch.com"
print(nostarch_url)
print(nostarch_url.removeprefix("https://"))

# Avoiding Syntax Err0rs With Strings
message = "One of Python's strengths is its diverse community."
print(message)
# message = 'One of Python's strengths is its diverse community.'(Need to use double quotes when using an apostrophy inside quotes)

# Personal Message
name = "Pallavi"
print(f"Hello {name}, how are you doing today?")

# Name Cases
full_name = "Pallavi jain"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# Famous Quote
print('Papa Baby once said, "It\'s not what you know, but what you implement."')

# Famous Quote 2
famous_person = "Papa Baby"
message = "It's not what you know, but what you implement."
print(f'{famous_person.title()} once said, "{message}"')

# Stripping Names
whitespace_name = " \t Pallavi Jain  \n \t "
print(whitespace_name)
print(whitespace_name.lstrip())
print(whitespace_name.rstrip())
print(whitespace_name.strip())

# File Extensions
file_name = "python_notes.txt"
file_name = file_name.removesuffix(".txt")
print(file_name)