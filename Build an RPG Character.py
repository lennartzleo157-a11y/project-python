#Build an RPG Character


full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    #name conditions
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:# i didnt know how to write character so i kinda searched it up 
        return "The character name is too long"
    if " " in name:# saw this on the internet and im thinking theres a bit of a better way to put this as imagen there where two spaces does it also consider that?i checked and it does so there i go
        return "The character name should not contain spaces"
    
    #stats conditions
    if (not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma, int)):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    stats_summed = strength + intelligence + charisma
    if stats_summed != 7:
        return "The character should start with 7 points"
#If all values pass the verification, the function should return a string with four lines:
    else:
        return name + "\n" + "STR " + (full_dot * strength) + empty_dot * (10 - strength) + "\n" + "INT " + (full_dot * intelligence) + empty_dot * (10 - intelligence) + "\n" + "CHA " + (full_dot * charisma) + empty_dot * (10 - charisma)

print(create_character("ren",4,2,1))