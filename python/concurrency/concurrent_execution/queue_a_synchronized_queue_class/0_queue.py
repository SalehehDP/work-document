"""
    The queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded programming when information must be exchanged safely between multiple threads. 
    
    queue use locks to temporarily block competing threads; however, they are not designed to handle reentrancy within a thread.
    """
