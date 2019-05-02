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
            #Printa head data frame
            print(df_911.head())
        
        elif option == "top_zips":
            #Printa top CEPS
            print(df_911["zip"].value_counts().head(5))
            print("\n")

        elif option == "top_towns":
            #Printa top cidades
            print(df_911["twp"].value_counts().head(5))
            print("\n")

        elif option == "unique_titles":
            #Printa valores unicos
            print( "{} unique titles".format(len(df_911.groupby("title"))) )
            print("\n")

        elif option == "top_common-reasons":
            #Printa HEAD
            print(df_911["Reason"].value_counts().head(5))
            #Plota grafico Razoes
            sns.countplot(x="Reason", data=df_911)
            plt.show()
            plt.clf()

        elif option == "reason_dow":
            #Plota grafico Razoes por dia da semana
            sns.countplot( x = "Day of Week", data = df_911, hue = "Reason" )
            plt.show()
            plt.clf()

        elif option == "reason_month":
            #Plota grafico razoes por mes
            sns.countplot( x = "Month", data = df_911, hue = "Reason" )
            plt.show()
            plt.clf()

        elif option == "plot_by_month":
            #Casos por mes
            byMonth = df_911.groupby("Month").count()
            print( byMonth.head() )
            #Plota grafico casos por mes
            byMonth["Reason"].plot()
            plt.show()
            plt.clf()

        elif option == "by_month_linear":
            #Agrupa por mes casos
            byMonth = df_911.groupby("Month").count()
            byMonth = byMonth.reset_index()
            print( byMonth.head() )
            #Ploota grafico evolucao casos por mes
            sns.lmplot(x="Month", y="Reason", data=byMonth)
            plt.show()
            plt.clf()

        elif option == "plot_by_date":
            #Agrupa por data
            byDate = df_911.groupby("Date").count()
            print(byDate.head())
            #Plota grafico casos por data
            byDate["Reason"].plot()
            plt.show()
            plt.clf()
            
        elif option == "plot_reason_by_date":
            #inicializa opcao de razao
            reason = ""

            #Valida input razao
            while True:
                try:
                    #lista de opcoes
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
            #Plota grafico de evolucao de razao especifica
            byReasonDate["Reason"].plot()
            plt.show()
            plt.clf()

        elif option == "heatmap_hours_dow" or option == "cluster_hours_dow":
            #Cria matriz casos hora por dia da semana
            byHourDOW = df_911.groupby(["Day of Week", "Hour"]).count()["Reason"].unstack()
            
            if option == "heatmap_hours_dow":
                sns.heatmap(byHourDOW)
            else:
                sns.clustermap(byHourDOW)
            plt.show()
            plt.clf()

        elif option == "heatmap_month_dow" or option == "cluster_month_dow":
            #Cria matriz casos dia da semana por mes
            byMonthDOW = df_911.groupby(["Day of Week", "Month"]).count()["Reason"].unstack()

            if option == "heatmap_month_dow":
                sns.heatmap(byHourDOW)
            else:   
                sns.clustermap(byHourDOW)
            plt.show()
            plt.clf()

        elif option == "quit":
            running = False
            break
        if running:
            programPause = input("PRESS <ENTER> KEY TO COTINUE...")

 
## END - CODE
