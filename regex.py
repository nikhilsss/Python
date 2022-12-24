import re 

value ="This is a string"
output = re.search("^This.*string$", value)

print(output)

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"