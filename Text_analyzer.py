'''
author = Pavel Vanacek
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive topographic 
feature that rises sharply some 1000 feet 
above Twin Creek Valley to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
#Formating
letterhead = 50 * "="
letterbody = 150 * "-"

# User's ID
print(letterhead)
Name = input("Please enter your name: ")
Password = input("Please enter your password: ")
print(letterhead)

# Database of Users
database = {"bob": 123, "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Validation of User's ID against to database
if str(database.get(Name)) == Password:
    print(f'Welcome to the app, {Name.title()}.')
else:
    print(f'I am sorry. Name: {Name.title()} or Password: {Password} are incorrect.')
    exit()

#Text selection
print(letterhead)
print(f'We have currently up to {len(TEXTS)} texts to be analyzed.')

while True:
    Selection = input("Please select no. of text that you want to analyze: ")
    if Selection == "":
        continue
    else:
        break
print(letterhead)
try:
    Selection_number = int(Selection)
except:
    Selection_number = -1

if Selection_number in tuple(range(1,len(TEXTS)+1)):
    Selection_idexed = TEXTS[int(Selection)-1]
    print(f'Your selection: {Selection_idexed}')

elif Selection_number < 1 or Selection_number > 3:
    print(f'Error. Please select no. of text: {tuple(range(1,len(TEXTS)+1))}')
    exit()
else:
    print(f'Error. Please select no.')
    exit()
print(letterhead)

# Text analysis
    # 1) number of words
pocet_slov = Selection_idexed.split()
pocet_slov_cleaned = []
for slovo in pocet_slov:
    pocet_slov_cleaned.append(slovo.strip(",.!'"))
print(pocet_slov_cleaned)

pocet_slov_number = len(pocet_slov_cleaned)
print(f'There are {pocet_slov_number} words in the selected text.')

    # 2) number of words with first titlecase letter
pocet_slov_titlecase = 0
titlecase_slova = []
for slovo in pocet_slov_cleaned:
    if slovo[0].isupper():
        titlecase_slova.append(slovo)
        pocet_slov_titlecase += 1
print(f'There are {pocet_slov_titlecase} titlecase words.')
display_titlecase_words = input("To display titlecase words type 'display', otherwise continue by pressing any key in analyzis.")
if display_titlecase_words == "display":
    print(letterbody)
    print(f'Here are titlecase words in analyzed text: {titlecase_slova}')
    print(letterbody)
else:
    print(letterbody)

    # 3) number of words with first uppercase letter
pocet_slov_uppercase = 0
uppercase_slova = []
for slovo in pocet_slov_cleaned:
    if slovo[::].isupper() and slovo[::].isalpha():
        uppercase_slova.append(slovo)
        pocet_slov_uppercase += 1
print(f'There are {pocet_slov_uppercase} uppercase words.')
display_uppercase_words = input("To display uppercase words type 'display', otherwise continue by pressing any key in analyzis.")
if display_uppercase_words == "display":
    print(letterbody)
    print(f'Here are uppercase words in analyzed text: {uppercase_slova}')
    print(letterbody)
else:
    print(letterbody)

    # 4) number of words with first lowercase letter
pocet_slov_lowercase = 0
lowercase_slova = []
for slovo in pocet_slov_cleaned:
    if slovo[::].islower():
        lowercase_slova.append(slovo)
        pocet_slov_lowercase += 1
print(f'There are {pocet_slov_lowercase} lowercase words.')
display_lowercase_words = input("To display lowercase words type 'display', otherwise continue by pressing any key in analyzis.")
if display_lowercase_words == "display":
    print(letterbody)
    print(f'Here are lowercase words in analyzed text: {lowercase_slova}')
    print(letterbody)
else:
    print(letterbody)

    # 5) number of numeric strings
pocet_numeric_strings = 0
numeric_strings = []
for slovo in pocet_slov_cleaned:
    if slovo[::].isdigit():
        numeric_strings.append(slovo)
        pocet_numeric_strings += 1
print(f'There are {pocet_numeric_strings} numeric strings.')
display_numeric_strings = input("To display numeric strings type 'display', otherwise continue by pressing any key in analyzis.")
if display_numeric_strings == "display":
    print(letterbody)
    print(f'Here are numeric strings in analyzed text: {numeric_strings}')
    print(letterbody)
else:
    print(letterbody)

    # 6) sum of all the numbers
total_numbers = 0
for slovo in numeric_strings:
    ciselne_slovo = int(slovo)
    total_numbers += ciselne_slovo
print(f'The sum of all the numbers {total_numbers}.')

# Occurence of words according to their lenght
print(letterhead)
print("""LEN | OCCURENCES | NR.""")

counts = {}
for slovo in sorted(pocet_slov, key =len, reverse = True):
    counts[len(slovo)] = counts.setdefault(len(slovo), 0) + 1
#print(counts)

while counts:
     info = counts.popitem()
     print(f'{info[0]} | {"*" * info[1]}{(15 -info[1])* " "} | {info[1]}')
