"""
    Dask dataframe enables processing of larger-than-memory datasets by breaking down the dataset into multiple dataframes and coordinating them, whether it be on a single machine, or distributed throughout a cluster.


    pandas dataframe may be loaded with:
    import pandas as pd
    df = pd.read_csv(“…”)

    A Dask dataframe may be loaded with:
    import dask.dataframe as dd
    df = dd.read_csv("...")

    This consistency in interfacing between pandas and Dask dataframe is one of its strengths and Dask’s core tenets.
    
    Dask was chosen here for data analysis and manipulation.
    """
