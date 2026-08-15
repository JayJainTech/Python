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