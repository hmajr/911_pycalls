import os
from MyException import InvalidOption

def menu_gui():
    #Limpa tela terminal
    os.system("cls" if os.name == 'nt' else 'clear')
    option_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
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
    print("13. Clustermap hours per day of week")
    print("14. Heatmap day of week per month")
    print("15. Clustermap day of week per month")
    print("16. Exit")
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
                print("----------------------------------------")
                print("\t FIRST 5 OF DATA FRAME")
                print("----------------------------------------")
                return "print_df"
            if option == 2:
                print("\n")
                print("----------------------------------------")
                print("\t TOP 5 ZIP CODES")
                print("----------------------------------------")
                return "top_zips"
            if option == 3:
                print("\n")
                print("----------------------------------------")
                print("\t TOP 5 TOWNSHIPS")
                print("----------------------------------------")
                return "top_towns"
            if option == 4:
                print("\n")
                print("----------------------------------------")
                print("\t Counted Unique Titles Codes")
                print("----------------------------------------")
                return "unique_titles"
            if option == 5:
                print("\n")
                print("----------------------------------------")
                print("\t TOP 5 COMMON REASONS CALLS")
                print("----------------------------------------")
                return "top_common-reasons"
            if option == 6:
                print("\n")
                print("----------------------------------------")
                print("\t Common reasons per day of week")
                print("----------------------------------------")
                return "reason_dow"
            if option == 7:
                print("\n")
                print("----------------------------------------")
                print("\t Common reasons per month")
                print("----------------------------------------")
                return "reason_month"
            if option == 8:
                print("\n")
                print("----------------------------------------")
                print("\t Plot by month")
                print("----------------------------------------")
                return "plot_by_month"
            if option == 9:
                print("\n")
                print("----------------------------------------")
                print("\t Linear regression by month")
                print("----------------------------------------")
                return "by_month_linear"
            if option == 10:
                print("\n")
                print("----------------------------------------")
                print("\t Plot by date")
                print("----------------------------------------")
                return "plot_by_date"
            if option == 11:
                print("\n")
                print("----------------------------------------")
                print("\t Plot 911 calls especific reason by date")
                print("----------------------------------------")
                return "plot_reason_by_date"
            if option == 12:
                print("\n")
                print("----------------------------------------")
                print("\t Heatmap day of week per month")
                print("----------------------------------------")
                return "heatmap_hours_dow"
            if option == 13:
                print("\n")
                print("----------------------------------------")
                print("\t Cluster day of week per month")
                print("----------------------------------------")
                return "cluster_hours_dow"

            if option == 14:
                print("\n")
                print("----------------------------------------")
                print("\t Heatmap day of week per month")
                print("----------------------------------------")
                return "heatmap_month_dow"

            if option == 15:
                print("\n")
                print("----------------------------------------")
                print("\t Cluster day of week per month")
                print("----------------------------------------")
                return "cluster_month_dow"

            if option == 16:
                return "quit"



if __name__ == "__main__":
    pass
