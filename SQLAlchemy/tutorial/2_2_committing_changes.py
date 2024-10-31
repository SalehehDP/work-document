"""
    to create a table and insert some data, and the transaction is then committed using the Connection.commit() method, invoked inside the block where we acquired the Connection object:
    """
# "commit as you go"
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()

# BEGIN(implicit)
# CREATE TABLE some_table(x int, y int)
# [...]()
# <sqlalchemy.engine.cursor.CursorResult object at 0x... >
# INSERT INTO some_table(x, y) VALUES(?, ?)
# [...]((1, 1), (2, 4))
# <sqlalchemy.engine.cursor.CursorResult object at 0x... >
# COMMIT

"""
SQL statements : 
    - CREATE TABLE
    - INSERT

Connection.commit() method which commits the transaction

style of committing data : 
    - commit as you go
    - begin once:  we use the Engine.begin() method to acquire the connection, rather than the Engine.connect() method. This method will both manage the scope of the Connection and also enclose everything inside of a transaction with COMMIT at the end, assuming a successful block, or ROLLBACK in case of exception raise
     """
# "begin once"
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )
# BEGIN (implicit)
# INSERT INTO some_table (x, y) VALUES (?, ?)
# [...] ((6, 8), (9, 10))
# <sqlalchemy.engine.cursor.CursorResult object at 0x...>
# COMMIT


"""
“Begin once” style is often preferred as it is more succinct and indicates the intention of the entire block up front. However, within this tutorial we will normally use “commit as you go” style as it is more flexible for demonstration purposes.

“implicit” here means that SQLAlchemy did not actually send any command to the database; it just considers this to be the start of the DBAPI’s implicit transaction. You can register event hooks to intercept this event, for example.

"""
