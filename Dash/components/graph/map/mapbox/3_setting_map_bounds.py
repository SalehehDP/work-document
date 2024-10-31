"""
    resurses : https://plotly.com/python/mapbox-layers/
    
    Set bounds for a map to specify an area outside which a user interacting with the map can't pan or zoom.
    """

fig.update_layout(
    mapbox_bounds={"west": 30, "east": 70, "south": 30, "north": 70})
