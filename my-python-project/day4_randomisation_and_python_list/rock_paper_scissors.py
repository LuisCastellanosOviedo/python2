from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

welcome = '''
 ,ad8888ba,   88                                                                                                  88                                                              
 d8"'    `"8b  88                                                                                                  88                                                              
d8'        `8b 88                                                                                                  88                                                              
88          88 88,dPPYba,  8b,dPPYba,  ,adPPYba, 8b,dPPYba,  ,adPPYba,  ,adPPYba,    88,dPYba,,adPYba,  ,adPPYYba, 88    8b,dPPYba,  ,adPPYYba,  ,adPPYb,d8  ,adPPYba,  ,adPPYba,  
88          88 88P'    "8a 88P'   "Y8 a8P_____88 88P'   "Y8 a8"     "8a I8[    ""    88P'   "88"    "8a ""     `Y8 88    88P'    "8a ""     `Y8 a8"    `Y88 a8"     "8a I8[    ""  
Y8,        ,8P 88       d8 88         8PP""""""" 88         8b       d8  `"Y8ba,     88      88      88 ,adPPPPP88 88    88       d8 ,adPPPPP88 8b       88 8b       d8  `"Y8ba,   
 Y8a.    .a8P  88b,   ,a8" 88         "8b,   ,aa 88         "8a,   ,a8" aa    ]8I    88      88      88 88,    ,88 88    88b,   ,a8" 88,    ,88 "8a,   ,d88 "8a,   ,a8" aa    ]8I  
  `"Y8888Y"'   8Y"Ybbd8"'  88          `"Ybbd8"' 88          `"YbbdP"'  `"YbbdP"'    88      88      88 `"8bbdP"Y8 88    88`YbbdP"'  `"8bbdP"Y8  `"YbbdP"Y8  `"YbbdP"'  `"YbbdP"'  
                                                                                                                         88                      aa,    ,88                        
                                                                                                                         88                       "Y8bbdP"                         


'''
options = [rock, paper, scissors]

while True:

    user_option = int(
        input("MALDITA SEA :  0 PARA PIEDRA , 1 PARA PAPEL , 2 TIJERAS , MALDITA SEA ESCOJA BIEN MTF CTM !!! "))

    if user_option < 0 or user_option > 2:
        print("IMBECIL !!! LE DIJE QUE 0 PARA PIEDRA , 1 PARA PAPEL , 2 TIJERAS , MALDITA SEA ESCOJA BIEN MTF CTM !!! ")
    else:
        print(f"MAL NACIDO UD ESCOGIO : \n  {options[user_option]}   \n")
        print("ESTA BASURA DE PROGRAMA ESCOGE:\n")
        pc_chose = randint(0, 2)
        print(options[pc_chose])

        if pc_chose == 0 and user_option == 2:
            print("PERDIO GONORREA")
        elif pc_chose == 1 and user_option == 0:
            print("PERDIO GONORREA")
        elif pc_chose == 2 and user_option == 1:
            print("PERDIO GONORREA")
        elif pc_chose == user_option:
            print("SOMOS IGUAL DE BRUTOS !!!!")
        else:
            print("GANO PRRO ")
