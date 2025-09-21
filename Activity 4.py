
full_name = input("Enter your full name (First, Middle, Last): ")

first, middle, last = full_name.split(",")

first = first.strip().capitalize()
middle = middle.strip()[0].upper() + "."
last = last.strip().title()

print("Formatted Name:", last, ",", first,",",middle)
