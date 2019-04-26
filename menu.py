import os
from MyException import InvalidOption

def menu_gui():
    #Limpa tela terminal
    os.system("cls" if os.name == 'nt' else 'clear')
    option_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("------------------------------ 911 CALLS DATA -----------------------------")
    print("1. Top 5 zip codes for 911 calls")
    print("2. Top 5 townships for 911 calls")
    print("3. Count unique titles codes")
    print("4. Most common reason for 911 calls")
    print("5. Menu Option 4")
    print("6. Menu Option 4")
    print("7. Menu Option 4")
    print("8. Menu Option 4")
    print("9. Menu Option 4")
    print("10. Exit")
    print("---------------------------------------------------------------------------")

    while True:
        try:
            option = int(input("Enter your choice [{}-{}]:".format(option_list[0], option_list[-1])))
            
            if option in option_list:
                print(option)
            else:
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
            if option == 4:
                return "top_common-reasons"
            if option == 10:
                return "quit"


if __name__ == "__main__":
    pass
