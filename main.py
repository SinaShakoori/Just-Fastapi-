from fastapi import FastAPI



app = FastAPI()





@app.get("/")
async def getasli():
    return {" Hello everybody this is my first fastapi project.  thank you for your attention..."}






if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)