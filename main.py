# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import os
from pathlib import Path

try:
    import googletrans
except:
    os.system("pip install googletrans==3.1.0a0")
    import googletrans

ENGLISH_WORDS = []
TRANSLATED_WORDS = []
directory = ""
CHOSEN_LANGUAGE = ""
translator = googletrans.Translator()
isAndroid = True

def main():
    global directory
    checkSaveFolder()
    chosenLanguage = promptUserLanguage()
    chosenFormatting = promptUserFormatting()
    print("Opening File...")
    openCSV()

    print("Translating words...")
    translateWords(chosenLanguage)
    print("Writting to file...")
    if chosenFormatting == 1:
        writeToFileIOS(chosenLanguage)
    elif chosenFormatting == 2:
        writeToFileAndroid(chosenLanguage)
    else:
        writeToFileAndroid(chosenLanguage)
        writeToFileIOS(chosenLanguage)
    print("Successfully Translated file! Saved in - %s" % directory)
    response = input("Translate another language with same file? (y/n) - ")
    while True:
        if response == "y":
            main()
        elif response == "n":
            exit()
        else:
            response = input("Incorrect response! Translate another language? (y/n) - ")

def checkSaveFolder():
    global directory
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    directory = ROOT_DIR + "\\translatedFiles"
    if not os.path.exists(directory):
        os.makedirs(directory)

def openCSV():
    with open('localize.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for string in row:
                ENGLISH_WORDS.append(string)
                line_count += 1

def translateWords(chosenLanguage):
    for line in ENGLISH_WORDS:
        translatedWord = (translator.translate(line, src='en', dest=chosenLanguage)).text
        if type(translatedWord) == list:
            translatedWord = translatedWord[0]
        TRANSLATED_WORDS.append(translatedWord)

def writeToFileAndroid(chosenLanguage):
    file_name = '%s\\%s-translatedFile-Android.txt' % (directory, chosenLanguage)
    with open(file_name, 'w+', encoding="utf-8") as translatedFile:
        translatedFile.truncate()
        for index, line in enumerate(ENGLISH_WORDS):
            translatedFile.write('<string name="%s">%s</string>\n' % (ENGLISH_WORDS[index], TRANSLATED_WORDS[index]))
        translatedFile.close()

def writeToFileIOS(chosenLanguage):
    file_name = '%s\\%s-translatedFile-IOS.txt' % (directory, chosenLanguage)
    with open(file_name, 'w+', encoding="utf-8") as translatedFile:
        translatedFile.truncate()
        for index, line in enumerate(ENGLISH_WORDS):
            translatedFile.write('"%s" = "%s";\n' % (ENGLISH_WORDS[index], TRANSLATED_WORDS[index]))
        translatedFile.close()


def promptUserLanguage():
    languages = googletrans.LANGUAGES
    print("Loaded Translator for Localizing IOS and Android apps.\nInstructions -")
    print("     Create a file called localize.csv, and put it in the root directory of the project")
    print("     Ensure the file is prefilled with data that you want translated.")
    print("     e.g. Register,Login,Home,Email,Password,About,Forgot,Two Words, etc...")
    print("     Words or phrases can be used, so long as they are separated by ','")
    print("     Resulting file will be stored in the same directory called translatedFile.txt\n")

    response = input("What language do you want to translate it to? Enter value KEY e.g. 'es' (Type ls to view options)\n")
    while True:
        if response == "ls":
            print(languages)
            response = input(
            "What language do you want to translate it to? Enter value KEY e.g. 'es' (Type ls to view options)\n")
        else:
            for key in languages:
                # print(key, response)
                if response == key:
                    return response
            response = input(
            "Incorrect Language KEY! Enter value KEY e.g. 'es' (Type ls to view options)\n")


def promptUserFormatting():
    print("What device are you wanting to convert this for? Type the corresponding number -")
    print("     1. IOS (IPhones)")
    print("     2. Android")
    print("     3. Both\n")
    response = input("Number - ")
    while True:
        if response == "1":
            return 1
        elif response == "2":
            return 2
        elif response == "3":
            return 3
        else:
            response = input("Incorrect Input!\nNumber - ")




if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
