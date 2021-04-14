'''Read Files'''

file = open('samplefile.txt')
print('Reading the first line \n'+ file.readline())
print("="*25)
print('Reading the second line \n'+ file.readline())
print("="*25)
print('Reading the third line to end of file \n'+ str(file.readlines()))
print("="*25)
print('as pointer is at end of the file, it will not read any line, output will be blank \n' +file.read())
print("="*25)
print('as pointer is at end of the file, it will not read any line, output will be blank \n' + str(file.readlines()))
print("="*25)

file.close()

with open('samplefile.txt') as f:
    print('printing the list of lines in the file \n'+ str(f.readlines()))
f.close()
print("="*25)

'''Iterating through the file'''

with open('samplefile.txt') as y:
    for line in y:
        print(line.upper())

with open('samplefile.txt') as y:
    for line in y:
        print(line.strip().upper())
  
# Sample output #    
'''
 Reading the first line 
1. When in doubt, go to the library

=========================
Reading the second line 
2. We can't choose our fate, but we can choose others

=========================
Reading the third line to end of file 
['3. Fear of a name only increases fear of the thing itself.\n', '4. But you know, happiness can be found even in the darkest of times, if one only remembers to turn on the light.\n', '5. It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.\n', '6. It matters not what someone is born, but what they grow to be.\n', '7. It is the unknown we fear when we look upon death and darkness, nothing more.\n', '8. Things we lose have a way of coming back to us in the end, if not always in the way we expect.\n', '9. Anything’s possible if you’ve got enough nerve.\n', '10. To the well-organized mind, death is but the next great adventure']
=========================
as pointer is at end of the file, it will not read any line, output will be blank 

=========================
as pointer is at end of the file, it will not read any line, output will be blank 
[]
=========================
printing the list of lines in the file 
['1. When in doubt, go to the library\n', "2. We can't choose our fate, but we can choose others\n", '3. Fear of a name only increases fear of the thing itself.\n', '4. But you know, happiness can be found even in the darkest of times, if one only remembers to turn on the light.\n', '5. It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.\n', '6. It matters not what someone is born, but what they grow to be.\n', '7. It is the unknown we fear when we look upon death and darkness, nothing more.\n', '8. Things we lose have a way of coming back to us in the end, if not always in the way we expect.\n', '9. Anything’s possible if you’ve got enough nerve.\n', '10. To the well-organized mind, death is but the next great adventure']
=========================


Iterating through file with for loop : 

1. WHEN IN DOUBT, GO TO THE LIBRARY

2. WE CAN'T CHOOSE OUR FATE, BUT WE CAN CHOOSE OTHERS

3. FEAR OF A NAME ONLY INCREASES FEAR OF THE THING ITSELF.

4. BUT YOU KNOW, HAPPINESS CAN BE FOUND EVEN IN THE DARKEST OF TIMES, IF ONE ONLY REMEMBERS TO TURN ON THE LIGHT.

5. IT TAKES A GREAT DEAL OF BRAVERY TO STAND UP TO OUR ENEMIES, BUT JUST AS MUCH TO STAND UP TO OUR FRIENDS.

6. IT MATTERS NOT WHAT SOMEONE IS BORN, BUT WHAT THEY GROW TO BE.

7. IT IS THE UNKNOWN WE FEAR WHEN WE LOOK UPON DEATH AND DARKNESS, NOTHING MORE.

8. THINGS WE LOSE HAVE A WAY OF COMING BACK TO US IN THE END, IF NOT ALWAYS IN THE WAY WE EXPECT.

9. ANYTHING’S POSSIBLE IF YOU’VE GOT ENOUGH NERVE.

10. TO THE WELL-ORGANIZED MIND, DEATH IS BUT THE NEXT GREAT ADVENTURE
Iterating through file with for loop, newline endings removed : 

1. WHEN IN DOUBT, GO TO THE LIBRARY
2. WE CAN'T CHOOSE OUR FATE, BUT WE CAN CHOOSE OTHERS
3. FEAR OF A NAME ONLY INCREASES FEAR OF THE THING ITSELF.
4. BUT YOU KNOW, HAPPINESS CAN BE FOUND EVEN IN THE DARKEST OF TIMES, IF ONE ONLY REMEMBERS TO TURN ON THE LIGHT.
5. IT TAKES A GREAT DEAL OF BRAVERY TO STAND UP TO OUR ENEMIES, BUT JUST AS MUCH TO STAND UP TO OUR FRIENDS.
6. IT MATTERS NOT WHAT SOMEONE IS BORN, BUT WHAT THEY GROW TO BE.
7. IT IS THE UNKNOWN WE FEAR WHEN WE LOOK UPON DEATH AND DARKNESS, NOTHING MORE.
8. THINGS WE LOSE HAVE A WAY OF COMING BACK TO US IN THE END, IF NOT ALWAYS IN THE WAY WE EXPECT.
9. ANYTHING’S POSSIBLE IF YOU’VE GOT ENOUGH NERVE.
10. TO THE WELL-ORGANIZED MIND, DEATH IS BUT THE NEXT GREAT ADVENTURE

Process finished with exit code 0
=======================================================================================================================================================
'''


