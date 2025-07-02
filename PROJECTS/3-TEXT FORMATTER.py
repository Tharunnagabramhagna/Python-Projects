print("💬TEXT FORMATTER💬")
text = input("\n 🤷 Enter some text: ")
print("1.UPPPER case")
print("2.lower case")
print("3.Title case")
print("4.Sentence case")

choice = input("Choose a Format(1-4): ")

if choice == "1":
    print(text.upper())  # this upper's all lower cases
elif choice == "2":
    print(text.lower())  # this lower's all upper cases
elif choice == "3":
    print(text.title())  # this makes the sentence as a title
elif choice == "4":
    print(text.capitalize())  # this makes the first letter captial


''' 
in another method we can make the choice as an integer 
  ex:- choice = int(input("Choose a format(1-4): "))

with this method we can  make "1" as 1
ex:- if choice == 1:
'''
