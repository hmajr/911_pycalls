if __name__ == "__main__":
##
## IMPORT
##
    ## LIBRARIES
    print("CARREGANDO BIBLIOTECAS...", end=" ")
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from plotly.offline import download_plotlyjs, plot, iplot
    import cufflinks as cf

    import menu
    from MyException import InvalidOption
    print("DONE")

    ## Interative plot offline
    cf.go_offline()
## END - IMPORT

##
## CODE
##
    ## Importa CSV
    print("\nCARREGANDO DADOS...", end=" ")
    df_911 = pd.read_csv("./dataset/911.csv")
    print("DONE")

    print("================== DATA FRAME PREVIEW ==================")
    print(df_911.info())
    print("\n")
    print(df_911.head())
    
    pause = input("PRESS ANY KEY TO COTINUE...")
    
    print("TRATANDO DADOS...", end=" ")
    #CRIA COLUNA 'REASON'
    df_911["Reason"] = df_911["title"].apply(lambda x: x.split(":")[0])
    #CRIA COLUNA HOUR, MONTH, DoW
    try:
        df_911["timeStamp"] = pd.to_datetime(df_911["timeStamp"])
        df_911["Hour"] = df_911["timeStamp"].apply(lambda time: time.hour)
        df_911["Month"] = df_911["timeStamp"].apply(lambda time: time.month)
        df_911["Day of Week"] = df_911["timeStamp"].apply(lambda time: time.dayofweek)
    except Exception as ex:
        print(ex)
    print("DONE")
    pause = input("PRESS ANY KEY TO COTINUE...")
    ## LOOP OPCOES
    running = True

    while running:
        option = menu.menu_gui()

        if option == "print_df":
            print("----------------------------------------")
            print("\t FIRST 5 OF DATA FRAME")
            print("----------------------------------------")
            print(df_911.head())
        elif option == "top_zips":
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
            print("\n")
            print("----------------------------------------")
            print("\t Counted Unique Titles Codes")
            print("----------------------------------------")
            print( "{} unique titles".format(len(df_911.groupby("title"))) )
            print("\n")

        elif option == "top_common-reasons":
            print("\n")
            print("----------------------------------------")
            print("\t TOP 5 COMMON REASONS CALLS")
            print("----------------------------------------")
            
            print(df_911["Reason"].value_counts().head(5))

            #PLOTA GRAFICO
            sns.countplot(x="Reason", data=df_911)
            plt.show()
            plt.clf()

        elif option == "quit":
            running = False
            break
        
        if running:
            programPause = input("PRESS ANY KEY TO COTINUE...")

            
                

## END - CODE
