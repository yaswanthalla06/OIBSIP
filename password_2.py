#............. Random Password Generator............
import random
import string
print("<=== RANDOM PASSWORD GENERATOR ===>")
def genpas(length ,usenum=True,uselet=True,usesymb=True):
    letters = string.ascii_letters 
    numbers = string.digits
    symbols = string.punctuation
    char =" "
    if usenum:   
        char+=numbers
    if uselet:
        char+=letters
    if usesymb:
        char+=symbols
    if not char:
        return "Error: No character types selected."
    
    password= ''.join(random.choice(char) for i in range(length))
    return password
# Main body
try:
    length = int(input("Enter the password length: "))
    if length <=0:
        raise ValueError("Password length must be positive.")
except ValueError:
    print("Invalid input")
    exit()
    
usenum= input("Include Numbers (yes/no)? : ").lower()=="yes"
uselet= input("Include Letters (yes/no)? : ").lower()=="yes"
usesymb= input("Include Symbols (yes/no)? : ").lower()=="yes"
password= genpas(length ,usenum,uselet,usesymb)
print("Generated password: ",password)