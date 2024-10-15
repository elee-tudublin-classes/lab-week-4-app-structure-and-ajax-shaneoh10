from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
import httpx
from contextlib import asynccontextmanager

from app.routes.home_routes import router as home_router
from app.routes.todo_routes import router as todo_router

main_router = APIRouter()

main_router.include_router(home_router)
main_router.include_router(todo_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.requests_client = httpx.AsyncClient()
    yield
    await app.requests_client.aclose()


# create app instance
app = FastAPI(lifespan=lifespan)

# add route for static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

# include routes in app
app.include_router(main_router)
