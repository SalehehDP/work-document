"""
i got error : 
failed to compile `diesel_cli v2.0.1`, intermediate artifacts can be found at `/tmp/cargo-installmlm0UV`
while running cargo install diesel_cli

solutain : 

By default diesel depends on the following client libraries:

libpq for the PostgreSQL backend
libmysqlclient for the Mysql backend
libsqlite3 for the SQlite backend
If you are not sure on how to install those dependencies please consult the documentation of the corresponding dependency or your distribution package manager.

For example, if you only have PostgreSQL installed, you can use this to install diesel_cli with only PostgreSQL:

cargo install diesel_cli --no-default-features --features sqlite

but at first install libsqlite3 : 
sudo apt-get install -y libsqlite3-dev
sudo apt install sqlite3



    """
