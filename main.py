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
    from datetime import datetime
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
    # pause = input("PRESS <ENTER> KEY TO COTINUE...")
    print("TRATANDO DADOS...")
    
    #CRIA COLUNA 'REASON'
    #CRIA COLUNA HOUR, MONTH, DoW
    try:
        df_911["Reason"] = df_911["title"].apply(lambda x: x.split(":")[0])
        
        print("Convertendo timeStamp em datatime")
        df_911["timeStamp"] = pd.to_datetime(df_911["timeStamp"])
        
        print("Criando coluna Hour")
        df_911["Hour"] = df_911["timeStamp"].apply(lambda time: time.hour)
        
        print("Criando coluna Month")
        df_911["Month"] = df_911["timeStamp"].apply(lambda time: time.month)
        
        print("Criando coluna Day of Week")
        df_911["Day of Week"] = df_911["timeStamp"].apply( lambda time: time.dayofweek )
        
        print("Criando coluna Date")
        df_911["Date"] = df_911["timeStamp"].apply(datetime.date)
        

        #Converte DoW de int para str dos dias da semana
        dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
        df_911["Day of Week"] = df_911["Day of Week"].map(dmap)
        
        # # Converte Mes de int para str dos meses do ano
        # dmap = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
        #          7: "Jul", 8: "Ago", 9: "Sep", 10: "Out", 11: "Nov", 12: "Dec"}
        # df_911["Date"] = df_911["Date"].map(dmap)

    except Exception as ex:
        print(ex)
    print("DONE!!")


    print("================== DATA FRAME PREVIEW ==================")
    print(df_911.info())
    print("\n")
    print(df_911.head())
    
    ## LOOP OPCOES
    running = True

    ### CONGELA TELA
    pause = input("PRESS <ENTER> KEY TO COTINUE...")

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


        elif option == "reason_dow":
            print("\n")
            print("----------------------------------------")
            print("\t Common reasons per day of week")
            print("----------------------------------------")
            
            #PLOTA GRAFICO
            sns.countplot( x = "Day of Week", data = df_911, hue = "Reason" )
            plt.show()
            plt.clf()

        elif option == "reason_month":
            print("\n")
            print("----------------------------------------")
            print("\t Common reasons per month")
            print("----------------------------------------")
            
            #PLOTA GRAFICO
            sns.countplot( x = "Month", data = df_911, hue = "Reason" )
            plt.show()
            plt.clf()

        elif option == "plot_by_month":
            print("\n")
            print("----------------------------------------")
            print("\t Plot by month")
            print("----------------------------------------")
            
            byMonth = df_911.groupby("Month").count()
            print( byMonth.head() )
            
            #PLOTA GRAFICO
            byMonth["Reason"].plot()
            plt.show()
            plt.clf()

        elif option == "by_month_linear":
            print("\n")
            print("----------------------------------------")
            print("\t Linear regression by month")
            print("----------------------------------------")
            byMonth = df_911.groupby("Month").count()
            byMonth = byMonth.reset_index()
            print( byMonth.head() )
            
            #PLOTA GRAFICO
            sns.lmplot(x="Month", y="Reason", data=byMonth)
            plt.show()
            plt.clf()

        elif option == "plot_by_date":
            print("\n")
            print("----------------------------------------")
            print("\t Plot by date")
            print("----------------------------------------")
            
            byDate = df_911.groupby("Date").count()
            print(byDate.head())
            #PLOTA GRAFICO
            byDate["Reason"].plot()
            plt.show()
            plt.clf()
            
        elif option == "plot_reason_by_date":
            print("\n")
            print("----------------------------------------")
            print("\t Plot 911 calls especific reason by date")
            print("----------------------------------------")

            reason = ""

            #Valida razao
            while True:
                try:
                    #lista itens unicos
                    list_reasons = list(df_911.Reason.unique())
                    
                    print("== LISTA DE OPCOES ==")
                    for item in list_reasons:
                        print(item)

                    reason = input("\nEscolha a razão de chamados: ")
                    
                    if not(reason in list_reasons):
                        raise ValueError("Digite um dos valores validos")
                except ValueError as ve:
                    print(ve)
                else:
                    break
            
            # Cria dataframe com a razao selecionada
            df_reason = df_911.loc[df_911["Reason"] == reason]
            byReasonDate = df_reason.groupby("Date").count()
            byReasonDate["Reason"].plot()
            #Mostra grafico
            plt.show()
            plt.clf()


        elif option == "quit":
            running = False
            break
        
        if running:
            programPause = input("PRESS <ENTER> KEY TO COTINUE...")

            
                

## END - CODE
