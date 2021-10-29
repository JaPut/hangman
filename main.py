import random
import sys
global vardi
global sakums
global skaits
vardi = ["suns", "kakis", "zive"]
skaits = 0
def exit():
    sys.exit()
def pievienot_vardu():
    vards = str(input('Uzraksti vārdu: \n'))
    vardi.append(vards)
    spele()
def spele():
    global skaits
    global uzminets
    global display
    global skaits
    global vards
    burts = str(input("Ieraksti burtu: "))
    if burts in vards:
        uzminets.extend([burts])
        print(f'Jau uzminētie burti: {uzminets}')
        print("Minamais vārds: ")
        for letter in vards:
            if letter in uzminets:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("\nTev izdevās, mēģini nākamo burtu! ")
        ga = len(uzminets)
        string = str(vards)
        s = set(string)
        a = len(s)
        while ga < a:
            spele()
        else:
            print("Tu esi uzvarējis")
        sakums()
    else:
        skaits +=1

        if skaits == 0:
            print("   _____ \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "_______|__\n")
            for letter in vards:
                if letter in uzminets:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("")
            spele()
        if skaits == 1:
            print("  _____ \n"
                  "  |    |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "_______|__\n")
            for letter in vards:
                if letter in uzminets:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("")
            spele()
        if skaits == 2:
            print("  _____ \n"
                  "  |    |      \n"
                  "  o    |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "_______|__\n")
            for letter in vards:
                if letter in uzminets:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("")
            spele()
        if skaits == 3:
            print("  _____ \n"
                  "  |    |      \n"
                  "  o    |      \n"
                  "  |    |      \n"
                  "       |      \n"
                  "       |      \n"
                  "       |      \n"
                  "_______|__\n")
            for letter in vards:
                if letter in uzminets:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("")
            spele()
            if skaits == 4:
                print("  _____ \n"
                      "  |    |      \n"
                      "  o    |      \n"
                      " /|    |      \n"
                      "       |      \n"
                      "       |      \n"
                      "       |      \n"
                      "_______|__\n")
                for letter in vards:
                    if letter in uzminets:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                print("")
                spele()
            if skaits == 5:
                print("  _____ \n"
                      "  |    |      \n"
                      "  o    |      \n"
                      " /|\   |      \n"
                      "       |      \n"
                      "       |      \n"
                      "       |      \n"
                      "_______|__\n")
                for letter in vards:
                    if letter in uzminets:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                print("")
                spele()
            if skaits == 6:
                print("  _____ \n"
                      "  |    |      \n"
                      "  o    |      \n"
                      " /|\   |      \n"
                      " /     |      \n"
                      "       |      \n"
                      "       |      \n"
                      "_______|__\n")
                for letter in vards:
                    if letter in uzminets:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                print("")
                spele()
            if skaits == 7:
                print("  _____ \n"
                      "  |    |      \n"
                      "  o    |      \n"
                      " /|\   |      \n"
                      " / \   |      \n"
                      "       |      \n"
                      "       |      \n"
                      "_______|__\n")
                for letter in vards:
                    if letter in uzminets:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                print("")
                print("Tu esi zaudējis!")
                sakums()
def sakums():
    global vards
    global garums
    global uzminets
    global display
    uzminets = []
    vards = random.choice(vardi)
    garums = len(vards)
    display = '_' * garums
    print("1_spēlēt, 2_pievienot_vārdu, 3_beigt")
    cipars = int(input("Ievadi skaitli: "))
    if (cipars == 1):
        spele()
    elif (cipars == 2):
        pievienot_vardu()
    else:
        print("atā")
        exit()
sakums()

