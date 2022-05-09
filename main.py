
from config.config import initialize
from core.app_temp import app_temp
from db.fauna import init

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

def main():
    vars_env = initialize()
    init(vars_env)  # init db
    # def async para abrir um websocket
    app_temp(vars_env)


if __name__ == '__main__':
    main()
