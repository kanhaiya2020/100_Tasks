# importing the module
import wikipedia

# setting language to hindi
lang = ['en','hi']
a = int(input('Enter the Number for language Hindi 1 or English 0 '))
search = input("What do you want to search in wikipedia: ")
if lang[a] in lang:
    wikipedia.set_lang(lang[a])

    # printing the summary
    print(wikipedia.summary(search))
else:
    print('Wrong Input')