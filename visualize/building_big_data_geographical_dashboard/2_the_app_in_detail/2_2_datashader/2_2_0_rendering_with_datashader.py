"""
    three main steps to generate an image with Datashader
        1- create a canvas:

            import datashader as ds
            cvs = ds.Canvas(plot_width=width, plot_height=height)

        2- aggregate the data (to lines in this case):
            agg = cvs.line(df, agg=ds.any(), geometry=”geometry”)

        3- plot the aggregated data:
            img = tf.shade(agg)

    there are obviously many variations and arguments to be passed
    
    our Datashader plot can benefit from lower resolutions in some situations. As Datashader aggregates data, a lower resolution means that the resulting image is going to provide more of a “higher-level” overview.
    
    how to align the map with the Datashader image ? with dash 
    """
