"""
    we use the relayoutData property from graphs rendered in Dash (with dcc.Graph objects) that relay information on layout-level edits by the user.
    So when the user zooms or pans across, the dcc.Graph object sends back information 
    
    steps :
    1- generate a map.
    2- filter our datafreame 
    3- add image to figure(pass df to datashader , create image , ....)
    
    
    result : 
    As we zoom in and out (and pan), the Dash app dynamically responds to our inputs and renders the data on-the-fly.
    It’s simply magic. 🪄
    
    """
