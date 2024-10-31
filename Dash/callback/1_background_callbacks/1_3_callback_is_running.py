"""
    sometimes we need  visual indication that the background callback is running or need  disable the button while the callback is running and re-enable it when the callback completes.

    use the running argument to @dash.callback

    This argument accepts a list of 3-element tuples :
    1- Output : dependency object referencing a property of a component in the app layout.
    2- value that the property should be set to while the callback is running
    3- the value the property should be set to when the callback completes 
    """
