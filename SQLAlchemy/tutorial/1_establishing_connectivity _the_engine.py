"""

Engine : This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. 
  The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.  
  we will use an in-memory-only SQLite database

  The Engine is created by using create_engine()
  create_engine.future flag set to True so that we make full use of 2.0 style 
    """

from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

"""
    The main argument to create_engine : URL = "sqlite+pysqlite:///:memory:"  

    indicates to the Engine three important facts:
    1 - What kind of database are we communicating with = sqlite , which links in SQLAlchemy to an object known as the dialect?
    2 - What DBAPI are we using? we’re using the name pysqlite, which in modern Python use is the sqlite3 
    * If omitted, SQLAlchemy will use a default DBAPI for the particular database selected.
    3 - How do we locate the database?  in-memory-only . This kind of database is perfect for experimenting as it does not require any server nor does it need to create new files
    
    *Lazy Connecting : The Engine, when first returned by create_engine(), has not actually tried to connect to the database yet; that happens only the first time it is asked to perform a task against the database. This is a software design pattern known as lazy initialization.
     ? create_engine.echo


    """
