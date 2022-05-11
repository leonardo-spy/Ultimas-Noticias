

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from config.config import initialize
from db.fauna import init
from core.route import graph_route

app = FastAPI()

# Dependency
@app.on_event("startup")
def on_startup():
    FastAPICache.init(InMemoryBackend())
    vars_env = initialize()
    init(vars_env)

app.include_router(graph_route)

app.mount("/files", StaticFiles(directory="templates/files"), name="files")
