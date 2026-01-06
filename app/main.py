from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="FastAPI CI/CD SHASHANK")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "FastAPI CI/CD Demo",
            "message": "FastAPI CI/CD app is running 🚀"
        }
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}
