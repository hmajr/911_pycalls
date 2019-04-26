if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    from plotly.offline import download_plotlyjs, plot, iplot
    import cufflinks as cf

    cf.go_offline()

    try:
        df_911 = pd.read_csv("./dataset/911.csv")
    except OSError as os:
        print(os)
    else:
        print(df_911.info())
        print("\n {}".format(df_911.head())

    