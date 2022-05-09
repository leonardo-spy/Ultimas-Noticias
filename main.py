
from config.config import initialize
from core.app_temp import app_temp,app_estadao,app_extra,app_folha,app_g1,app_oglobo,app_uol
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

@app.get("/Estadao")
def main_estadao():
    app_estadao()

@app.get("/Extra")
def main_extra():
    app_extra()

@app.get("/Folha")
def main_folha():
    app_folha()

@app.get("/G1")
def main_g1():
    app_g1()

@app.get("/OGlobo")
def main_oglobo():
    app_oglobo()

@app.get("/Uol")
def main_euol():
    app_uol()

def main():
    vars_env = initialize()
    init(vars_env)  # init db
    # def async para abrir um websocket
    app_temp(vars_env)


