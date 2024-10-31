"""
    Callbacks with background=True use a backend configured by you to run the callback logic. There are currently two options:
    - A DiskCache backend that runs callback logic in a separate process and stores the results to disk using the diskcache library. This is the easiest backend to use for local development, but is not recommended for production.
    - A Celery backend that runs callback logic in a Celery worker and returns results to the Dash app through a Celery broker like Redis.

    """
