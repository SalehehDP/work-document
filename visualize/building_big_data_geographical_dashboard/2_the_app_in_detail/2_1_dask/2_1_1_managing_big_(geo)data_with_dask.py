"""
    The raw data is in a shapefile (.shp)
    The geometry column and their constituent Linestring objects
    geopandas is not suitable for using directly with Dask, and so we use spatialpandas here instead. We begin by building a spatialpandas GeoDataFrame
    
    """
from spatialpandas import GeoDataFrame
df = GeoDataFrame(trans_lines)
df = df.pack_partitions(npartitions=2)
"""
    One key feature of spatialpandas is its packing of partitions based on geometry. This means the resulting dataframe is split into spatially optimised (i.e. divided by their positions in space) partitions like so:
    Its impact becomes more and more important as the dataset size increases, as you can imagine performance penalties for constantly loading different Dask partitions from disk onto memory.
    Additionally, the location data in longitudes/latitudes is converted to a different coordinate system (EPSG:3857) based on Eastings/Northings which we will use later. Geopandas provides the built-in .to_crs() method for this job, so we modify the “geometry” column with the appropriate coordinate system:
    """

df = df.assign(geometry_ll=df["geometry"])  # Save lon/lat geometry
en_geom = trans_lines["geometry"].to_crs("EPSG:3857")  # Convert data
df = df.assign(geometry=GeoSeries(en_geom))  # Add new data
