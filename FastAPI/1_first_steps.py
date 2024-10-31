from fastapi import FastAPI

# The simplest FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


"""
    to use this code copy and paste to main.py then run the app with command line 

    uvicorn main:app --reload

    """
"""
    The command uvicorn main:app refers to:

        main: the file main.py (the Python "module").
        app: the object created inside of main.py with the line app = FastAPI().
        --reload: make the server restart after code changes. Only use for development.
    """
