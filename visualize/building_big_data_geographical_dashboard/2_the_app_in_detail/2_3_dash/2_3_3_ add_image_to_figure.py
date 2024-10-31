"""
    filtered dataframe will be passed onto Datashader to be rendered,
    whereby the rendered image is added to a dictionary
    and added to the Plotly figure as an additional layer.

    """
grid_layer = {"sourcetype": "image", "source": img_out,
              "coordinates": curr_coords_ll_out}
mapbox_layers.append(grid_layer)
fig.update_layout(mapbox_layers=mapbox_layers)
