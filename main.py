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

    ## Interative plot offline
    cf.go_offline()
## END - IMPORT

##
## CODE
##
    ## Importa CSV
    df_911 = pd.read_csv("./dataset/911.csv")
    # try:
    #     df_911 = pd.read_csv("./dataset/911.csv")
        
    #     if pd.isnull(df_911):
    #         raise OSError
    # except Exception as ex:
    #     print(ex)
    # else:
    #     print(df_911.info())
    #     print("\n")
    #     print(df_911.head())

    print(df_911.info())
    print("\n")
    print(df_911.head())
    
    ## LOOP OPCOES
    running = True

    while running:
        option = menu.menu_gui()

        if option == "top_zips":
            pass
        elif option == "top_towns":
            pass
        elif option == "unique_titles":
            pass
        elif option == "quit":
            running = False
        

## END - CODE
