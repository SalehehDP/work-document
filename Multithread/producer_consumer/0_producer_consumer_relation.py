"""
    A very common relation between two threads is that of producer and consumer. For example, the downloading of an audio file is production, while listening is consumption ,printing a document where multiple applications want to print a document, downloading the data over the network and storing in a database, etc.

    It involves producer tasks, consumer tasks and a shared buffer or queue that connects these two types of tasks.
        Producer Tasks: Generate work that is added to the shared buffer.
        Consumer Tasks: Remove work from the shared buffer and process it in some way.
        Shared Buffer: Thread-safe data structure that connects producers and consumers that may be bounded.Additionally, the shared buffer must be thread-safe, ensuring that items can be added and removed concurrently by multiple threads or processes without race condition or corruption of the internal data structures.

    There may be one or more producers and one or more consumer tasks operating on the same shared buffer concurrently.
        For example: One Producer, One Consumer -  Multiple Producers, One Consumer - One Producer, Multiple Consumers - Multiple Producers, Multiple Consumers.
    
    """
