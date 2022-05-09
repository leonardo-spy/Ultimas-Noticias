
from config.config import initialize
from core.app_temp import app_temp
from db.fauna import init

from threading import Thread
from fastapi import FastAPI
app = FastAPI()
rodando = False

@app.get("/")
def read_root():
    # global rodando
    # if rodando != True:
    #     rodando = True
    #     Thread(target=main).start()
    main()
    return {"message": "Server is up and running!"}

def main():
    vars_env = initialize()
    init(vars_env)  # init db
    # def async para abrir um websocket
    app_temp(vars_env)


