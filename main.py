if __name__ == "__main__":
##
## IMPORT
##
    ## LIBRARIES
    import numpy as np
    import pandas as pd
    from plotly.offline import download_plotlyjs, plot, iplot
    import cufflinks as cf

    import menu
    from MyException import InvalidOption
    ## Interative plot offline
    cf.go_offline()
## END - IMPORT

##
## CODE
##
    ## Importa CSV
    df_911 = pd.read_csv("./dataset/911.csv")

    print(df_911.info())
    print("\n")
    print(df_911.head())
    
    ## LOOP OPCOES
    running = True

    while running:
        option = menu.menu_gui()

        if option == "top_zips":
            print("\n")
            print("----------------------------------------")
            print("\t TOP 5 ZIP CODES")
            print("----------------------------------------")
            print(df_911["zip"].value_counts().head(5))
            print("\n")
            # for zip in df_911["zip"].value_counts(5).head():
            #     rank = 1
            #     print("{}. {}".format(rank,zip[1]))
            #     rank += 1

        elif option == "top_towns":
            print("\n")
            print("----------------------------------------")
            print("\t TOP 5 TOWNSHIPS")
            print("----------------------------------------")
            print(df_911["twp"].value_counts().head(5))
            print("\n")

        elif option == "unique_titles":
        elif option == "quit":
            running = False
        
        if running:
            programPause = input("PRESS ANY KEY TO COTINUE...")

                
            
                

## END - CODE
