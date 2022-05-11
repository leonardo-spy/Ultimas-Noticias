from fastapi import APIRouter, Response, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi_cache.decorator import cache
from fastapi_cache.coder import PickleCoder
from fastapi.encoders import jsonable_encoder


from controller.G1 import G1
from controller.Oglobo import Oglobo
from controller.Extra import Extra
from controller.Estadao import Estadao
from controller.Folha import Folha
from controller.Uol import Uol
from controller.database import get_noticias

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH.parent / "templates"))

# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()

graph_route = APIRouter()

@cache(expire=(14*60)+45, coder=PickleCoder) 
async def get_noticias_async(portal):
    return jsonable_encoder(get_noticias(portal))

@graph_route.get("/", status_code=200)
async def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "noticias": await get_noticias_async('todos')},
    )

@graph_route.get("/estadao", status_code=200)
async def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "noticias": await get_noticias_async('estadao')},
    )

@graph_route.get("/extra", status_code=200)
async def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "noticias": await get_noticias_async('extra')},
    )

@graph_route.get("/folha", status_code=200)
async def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "noticias": await get_noticias_async('folha')},
    )

@graph_route.get("/g1", status_code=200)
async def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "noticias": await get_noticias_async('g1')},
    )

@graph_route.get("/oglobo", status_code=200)
async def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "noticias": await get_noticias_async('oglobo')},
    )
    
@graph_route.get("/uol", status_code=200)
async def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "noticias": await get_noticias_async('uol')},
    )

    

@graph_route.post("/Estadao")
def app_estadao(response: Response, token: str = Depends(token_auth_scheme)):
    VerifyToken(token.credentials)
    print('iniciando serviço para Estadão')
    estadao = Estadao()
    estadao.run()
    return {"message": "Index Estadão completo!"}

@graph_route.post("/Extra")
def app_extra(response: Response, token: str = Depends(token_auth_scheme)):
    VerifyToken(token.credentials)
    print('iniciando serviço para Extra')
    extra = Extra()
    extra.run()
    return {"message": "Index Extra completo!"}

@graph_route.post("/Folha")
def app_folha(response: Response, token: str = Depends(token_auth_scheme)):
    VerifyToken(token.credentials)
    print('iniciando serviço para Folha')
    folha = Folha()
    folha.run()
    return {"message": "Index Folha completo!"}

@graph_route.post("/G1")
def app_g1(response: Response, token: str = Depends(token_auth_scheme)):
    VerifyToken(token.credentials)
    print('iniciando serviço para G1')
    g1 = G1()
    g1.run()
    return {"message": "Index G1 completo!"}


@graph_route.post("/OGlobo")
def app_oglobo(response: Response, token: str = Depends(token_auth_scheme)):
    VerifyToken(token.credentials)
    print('iniciando serviço para O Globo')
    oglobo = Oglobo()
    oglobo.run()
    return {"message": "Index O Globo completo!"}

@graph_route.post("/Uol")
def app_uol(response: Response, token: str = Depends(token_auth_scheme)):
    VerifyToken(token.credentials)
    print('iniciando serviço para Uol')
    uol = Uol()
    uol.run()
    return {"message": "Index Uol completo!"}

def VerifyToken(token):
    if token != 'teste':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token invalid!")