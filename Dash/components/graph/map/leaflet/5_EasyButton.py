dl.Map(
    [
        # geojson,
        dl.TileLayer(),
        dl.FullscreenControl(),
        dl.LayerGroup(id="layer"),
        dl.EasyButton(icon='fa-home',
                      n_clicks=0, id="btn"),
        dl.Marker(
            position=[36.750181122351556, 58.9561819285166], icon=icon_transformer, id="meter"),
        dl.Marker(
            position=[36.7501, 58.9551819285166], icon=icon_transformer,  id="meter"),
    ],
    id="lv_map",  center=(36.7479, 58.955), zoom=15)
