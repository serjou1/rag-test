import uvicorn
from api import app

if __name__ == '__main__':
    uvicorn.run("main:app", port=4455, host="0.0.0.0", reload=True)
