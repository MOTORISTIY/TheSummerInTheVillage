import keyboard
import time
from data import *

def attach(enemy):
    print("\n----------------------------------------")
    print(f"Вы встретили: {enemy['name']}")
    print(f"""
ВАШЕ ХП: {IBRAGIM["hp"]}
СЕМКИ: {INVENTORI["Semki"]}
водки: {INVENTORI["vodka"]}
ДЕНЕЖКИ: {IBRAGIM["bablo"]}
""")
    print("----------------------------------------\n")
    
    if enemy["name"] == "Баба Зина":
        print("Привет внучок! Как ты понял, это я, Баба Зина!")
        print("Тебе придется откупиться от меня СЕМОЧКАМИ или получишь костылем по челюсти!")
        print("\nНажмите ENTER, чтобы откупиться, или нажмите SPACE, чтобы получить костылем!")
        
        while True:
            if keyboard.is_pressed("enter"):
                if INVENTORI['Semki'] > 0:
                    INVENTORI['Semki'] -= 1
                    print("\nТы откупился семочками!\n")
                    break
                else:
                    print("\nАХ ТЫ НЕГОДНИК! ХОТЕЛ МЕНЯ ОБМАНУТЬ!")
                    print("НА С ВЕРТУХИ!")
                    print("Потрачено hp -20\n")
                    IBRAGIM['hp'] -= 20
                    IBRAGIM['bablo'] -= 100
                    break
            elif keyboard.is_pressed('space'):
                print("\nПотрачено hp -20")
                IBRAGIM['hp'] -= 20
                IBRAGIM['bablo'] -= 100
                break
            time.sleep(0.1)

    elif enemy["name"] == "Алкаш Володя":
        print("Здарова, ЩЕГОЛ! Есть опохмЯлица?")
        print("\nНажмите ENTER, чтобы откупиться, или нажмите SPACE, чтобы получить шершавой рукой!\n")
        
        while True:
            if keyboard.is_pressed("enter"):
                if INVENTORI['vodka'] > 0:
                    INVENTORI['vodka'] -= 1
                    print("\nТы откупился водярой!\n")
                    break
                else:
                    print("\nДА ТЫ ЧЕ АШАЛЕЛ ЧТОЛИ!?🤬")
                    print("НААААААААААААА!")
                    print("Потрачено hp -20\n")
                    IBRAGIM['hp'] -= 20
                    IBRAGIM['bablo'] -= 200
                    break
            elif keyboard.is_pressed('space'):
                print("\nПотрачено hp -20")
                IBRAGIM['hp'] -= 20
                IBRAGIM['bablo'] -= 200
                break
            time.sleep(0.1)

    elif enemy["name"] == "АЗАМБЕК":
        print("Здарова! Помнишь меня? Я же тебя еще вооооот таким помню!")
        print("\nНапоишь чаем или как?\n")
        print("нажмите ENTER чтобы принять✔\n или SPACE чтобы отказать")
        
        while True:
            if keyboard.is_pressed("enter"):
                print("\nООООХ, хороший чаек!")
                print("ТЬФУ ТЫ! СОВСЕМ ЗАБЫЛ, Я ЖЕ тебе ГОСТИНЦЕВ ПРИВЕЗ!\n")
                print("\nВОДКА +1 \nСЕМКИ +1 \nБАБОСИКИ +500\n \n hp +30")
                break
            elif keyboard.is_pressed('space'):
                print("\nНу что ты... Я НЕ ПРИМУ ОТКАЗ! ДЕРЖИ😁")
                print("\nВОДКА +1 \nСЕМКИ +1 \nБАБОСИКИ +500\n")
                IBRAGIM['bablo'] += 500
                INVENTORI['vodka'] += 2
                INVENTORI['Semki'] += 3
                IBRAGIM['hp'] += 30
                break
            time.sleep(0.1)