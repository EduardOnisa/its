#Antonio Zottola
#18/04/2024

print("Hello World!")

#2.3 Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some python today "
name="Mario"
print(f"Hi Eric i'm {name},would you like to learn some python today?")

#2.4 Use a variable to represent a person's name and then print that person's name in lowercase,uppercase and titlecase.
lowercase=name.lower()
uppercase=name.upper()
titlecase=name.title()
print(f"{lowercase},{uppercase},{titlecase}")

#2.5 find a quote from a famous person, print the quote and the name of his author.
Albert="Albert Einstein"
print(f'{Albert} once said "A person who never made a mistake never tried something new"')

#2.6 Repeat Exercise 2.5 but this time,represent the name of the vip using a variable called: famous_name
famous_name="Kanye West"
message="My greatest pain in life is i will never be able to see me perform"
print(f'{famous_name} once said "{message}"')

#2.8 assign the value "python_notes.txt" to a variable called filename. then use the removesuffix() method to display the filename without th fie extension, like some browsers do.
filename="python_notes.txt"
print(filename.removesuffix('.txt'))

#3.1 Store the names of a few of your friends in a list called names. print each person's name by accessing each element in the list, one at a time.
names=["antonio", "carlo","marco"]
for name in names:
    print(names)
