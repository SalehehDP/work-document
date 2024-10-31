"""
Background callbacks offer a scalable solution for using long-running callbacks by running them in a separate background queue. 
In the background queue, the callbacks are executed one-by-one in the order that they came in by dedicated queue worker(s).
You can configure a callback to run in the background by setting background=True on the callback.
    """
