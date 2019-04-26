import os
from MyException import InvalidOption

def menu_gui():
    #Limpa tela terminal
    os.system("cls" if os.name == 'nt' else 'clear')

    print("------------------------------ 911 CALLS DATA -----------------------------")
    print("1. Top 5 zip codes for 911 calls")
    print("2. Top 5 townships for 911 calls")
    print("3. Count unique titles codes")
    print("4. Menu Option 4")
    print("5. Exit")
    print("---------------------------------------------------------------------------")

    while True:
        try:
            option = int(input("Enter your choice[1-5]:"))
            print(option)
            
            if (option < 1) or (option > 5):
                raise InvalidOption
        except InvalidOption as iopt:
            print("Tente outra opcao")
        except ValueError as ve:
            print(ve)
        else:
            if option == 1:
                return "top_zips"
            if option == 2:
                return "top_towns"
            if option == 3:
                return "unique_titles"
            if option == 5:
                return "quit"


if __name__ == "__main__":
    pass
