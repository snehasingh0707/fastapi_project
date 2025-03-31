from fastapi import FastAPI 

app = FastAPI() 

@app.get("/") 
def read_root(): 
    return {"message": "Welcome to FastAPI"}  # Proper indentation

@app.get("/add/{num1}/{num2}") 
def add(num1: int, num2: int): 
    return {"result": num1 + num2}  # Proper indentation

@app.get("/subtract/{num1}/{num2}") 
def subtract(num1: int, num2: int): 
    return {"result": num1 - num2}  # Proper indentation

@app.get("/multiply/{num1}/{num2}") 
def multiply(num1: int, num2: int): 
    return {"result": num1 * num2}  # Proper indentation

if __name__ == "__main__": 
    import uvicorn 
    uvicorn.run("apiserver:app", host="127.0.0.1", port=8000, reload=True)  # Proper indentation
