from os import path
from fastapi import FastAPI, Request, status
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


def create_app(firebase_config_json: str) -> FastAPI:
    app = FastAPI()
    templates = Jinja2Templates(
        directory=path.join(path.dirname(__file__), "templates")
    )

    @app.get("/", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
    async def index(request: Request):
        return templates.TemplateResponse(
            "index.html",
            context={"request": request, "firebase_config_json": firebase_config_json},
        )

    return app
