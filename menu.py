import os
from MyException import InvalidOption

def menu_gui():
    #Limpa tela terminal
    os.system("cls" if os.name == 'nt' else 'clear')
    option_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14]
    print("------------------------------ 911 CALLS DATA -----------------------------")
    print("1. Print head data frame 911 calls")
    print("2. Top 5 zip codes for 911 calls")
    print("3. Top 5 townships for 911 calls")
    print("4. Count unique titles codes")
    print("5. Most common reason for 911 calls")
    print("6. Common reasons per day of week")
    print("7. Common reasons per month")
    print("8. Plot 911 calls by Month")
    print("9. Linear regression 911 calls by month")
    print("10. Plot 911 calls by Date")
    print("11. Plot count 911 calls especific reason by date")
    print("12. Heatmap hours per day of week")
    print("13. Exit")
    print("14. Exit")
    print("---------------------------------------------------------------------------")

    while True:
        try:
            option = int(input("Enter your choice [{}-{}]:".format(option_list[0], option_list[-1])))
            
            if option in option_list:
                print(option)
            else:
                raise ValueError("Tente outra opcao")
        except ValueError as ve:
            print(ve)
        else:
            if option == 1:
                return "print_df"
            if option == 2:
                return "top_zips"
            if option == 3:
                return "top_towns"
            if option == 4:
                return "unique_titles"
            if option == 5:
                return "top_common-reasons"
            if option == 6:
                return "reason_dow"
            if option == 7:
                return "reason_month"
            if option == 8:
                return "plot_by_month"
            if option == 9:
                return "by_month_linear"
            if option == 10:
                return "plot_by_date"
            if option == 11:
                return "plot_reason_by_date"
            if option == 12:
                return "heatmap_hours_dow"
            if option == 14:
                return "quit"


if __name__ == "__main__":
    pass
