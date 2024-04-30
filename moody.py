from colorama import Fore, Style
import os

def mood_response(mood):    #---lists all of the mood responses
    if mood == 'happy':
        return(Fore.GREEN + 'Thats amazing, a mood very hard to come by!\n' + Style.RESET_ALL)
    elif mood == 'sad':
        return(Fore.LIGHTRED_EX + 'Im sorry, I hope you cheer up soon\n' + Style.RESET_ALL)
    elif mood == 'ok':
        return(Fore.LIGHTBLUE_EX + 'well, theres worse ways to feel...\n' + Style.RESET_ALL)
    elif mood == 'excited':
        return(Fore.GREEN + 'EXCITEMENT! A great feeling to have!\n' + Style.RESET_ALL)
    elif mood == 'anxious':
        return(Fore.LIGHTMAGENTA_EX + 'Remember, you can only control what you can control\n' + Style.RESET_ALL)
    elif mood == 'content':
        return(Fore.GREEN + 'Satisfaction cant be a bad thing\n' + Style.RESET_ALL)
    elif mood == 'irritated':
        return(Fore.LIGHTRED_EX + 'Take a few breaths and never say anything while angry\n' + Style.RESET_ALL)
    elif mood == 'hopeful':
        return(Fore.GREEN + 'Hope saves lives\n' + Style.RESET_ALL)
    elif mood == 'nostalgic':
        return(Fore.LIGHTWHITE_EX + 'Nothing wrong with a stroll down memory lane\n' + Style.RESET_ALL)
    elif mood == 'bye':
        return(Fore.GREEN + Style.BRIGHT + 'HAVE A GREAT DAY!!\n' + Style.RESET_ALL)
    else:
        return(Style.BRIGHT + Fore.RED + 'Invalid MOOOOOOD\n' + Style.RESET_ALL)

def mood_list():    #---Im sure i could have incorporated this into the mood_repsonse but I wanted to see if I could work with
                    #---multiple functions.
    moods = ['happy', 'sad', 'ok', 'excited', 'anxious', 'content', 'irritated', 'hopeful', 'nostalgic']
    print()
    print(Style.BRIGHT + 'List of moods' + Style.RESET_ALL)
    print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
    for m in moods: #---for loop to itereate and print the acceptable moods in a list
        print(Style.DIM + m + Style.RESET_ALL)