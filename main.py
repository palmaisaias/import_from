import moody
import os

while True: #---incorporated a while loop to give user the ability to keep playing with moods until they want to leave the program
    moody.mood_list()   #---calling on the imported function
    print()
    mood = input('''    Tell me your mood! 
OR if you want to be alone,
      enter "bye" ''').lower().strip()
    os.system('clear')
    if mood == 'bye':   #---I dont know if this is best practice but it was the only way I could figure out to use the import in a loop
                        #--- and still be able to break it.
        print(moody.mood_response(mood))    #---calling on the imported function
        break
    else:
        print(moody.mood_response(mood))
