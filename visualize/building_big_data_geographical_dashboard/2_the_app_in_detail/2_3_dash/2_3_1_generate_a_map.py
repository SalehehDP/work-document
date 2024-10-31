"""
    first we must Because we will be overlaying the Datashader image.
    just need to scateer_mapbox(df) and choose a base map style 
    
    """

dummy_df = pd.DataFrame(
    [{"x": latmin, "y": lonmin}, {"x": latmax, "y": lonmax}])
fig = px.scatter_mapbox(dummy_df, lat="x", lon="y")

fig.update_layout(mapbox_style="carto-darkmatter")

"""
    in this case :As Carto (along with OpenStreetMaps) uses EPSG:3857 projection, the Datashader image must be rendered with the same projection.
    projection استایلانتخاب شده برای نقشه و تصویر ساخته شده باید یکی باشد 
    """
