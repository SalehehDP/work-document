from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
"""
# log : 
BEGIN(implicit)
select 'hello world'
[...]()
[('hello world',)]
ROLLBACK
"""
"""
framed the operation inside of a transaction. 
The default behavior of the Python DBAPI includes that a transaction is always in progress; when the scope of the connection is released, a ROLLBACK is emitted to end the transaction.
The transaction is not committed automatically; when we want to commit data we normally need to call Connection.commit() as we’ll see in the next section. (“autocommit” mode is available for special cases)    
    
    """
