"""
you first need to configure a manager using your chosen backend.

You can provide the manager instance to the dash.Dash app constructor as the background_callback_manager keyword argument, or as the manager argument to the @dash.callback decorator.
    """

if 'REDIS_URL' in os.environ:
    # Use Redis & Celery if REDIS_URL set as an env variable
    from celery import Celery
    celery_app = Celery(
        __name__, broker=os.environ['REDIS_URL'], backend=os.environ['REDIS_URL'])
    background_callback_manager = CeleryManager(celery_app)

else:
    # Diskcache for non-production apps when developing locally
    import diskcache
    cache = diskcache.Cache("./cache")
    background_callback_manager = DiskcacheManager(cache)


"""
call is going to be like : 

@dash.callback(
    output=Output("paragraph_id", "children"),
    inputs=Input("button_id", "n_clicks"),
    background=True,
    manager=background_callback_manager,
)
"""
