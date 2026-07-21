from fastapi import FastAPI
from routes import router
from database import Base, engine
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the URL Shortener API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)