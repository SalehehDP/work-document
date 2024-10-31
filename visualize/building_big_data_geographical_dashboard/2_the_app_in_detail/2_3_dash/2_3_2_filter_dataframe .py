"""
    At the same time, we also use the relayout data to filter our dataframe to only include that to be shown on the map.
    """
tmp_df = (df_in
          .query(f"LAT > {lat0}")
          .query(f"LAT < {lat1}")
          .query(f"LON > {lon0}")
          .query(f"LON < {lon1}")
          )
