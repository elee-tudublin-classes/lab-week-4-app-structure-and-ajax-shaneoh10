from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from starlette.config import Config

# Load environment variables from .env
config = Config(".env")

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# define a router instance
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Handle http get requests for the site root / and return the index.html page"""
    serverTime: datetime = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    return templates.TemplateResponse(
        "index.html", {"request": request, "serverTime": serverTime}
    )


@router.get("/advice", response_class=HTMLResponse)
async def advice(request: Request):
    """Handle http get requests for the /advice route and return the advice.html page"""
    requests_client = request.app.requests_client
    response = await requests_client.get(config("ADVICE_URL"))

    return templates.TemplateResponse(
        "advice.html", {"request": request, "data": response.json()}
    )


@router.get("/apod", response_class=HTMLResponse)
async def apod(request: Request):
    requests_client = request.app.requests_client
    response = await requests_client.get(
        config("NASA_APOD_URL") + config("NASA_API_KEY")
    )

    return templates.TemplateResponse(
        "apod.html", {"request": request, "data": response.json()}
    )


@router.get("/params", response_class=HTMLResponse)
async def params(request: Request, name: str | None = ""):
    """Handle http get requests for the /params route and return the params.html page"""

    return templates.TemplateResponse("params.html", {"request": request, "name": name})


@router.post("/clicked", response_class=HTMLResponse)
async def clicked(request: Request):
    """Handle http post requests for the htmx /clicked route and return clicked_button.html"""
    return templates.TemplateResponse(
        "./partials/clicked_button.html", {"request": request}
    )


@router.get("/server_time", response_class=HTMLResponse)
async def server_time(request: Request):
    """Handle http get requests for the /server_time route and return server time"""
    server_time: datetime = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    return server_time
