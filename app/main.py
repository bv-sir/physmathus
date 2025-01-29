from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routers import ege, advanced

app = FastAPI()

app.include_router(ege.router, prefix="/ege", tags=["EGE"])
app.include_router(advanced.router, prefix="/advanced", tags=["Advanced"])

# Настройка Jinja2
templates = Jinja2Templates(directory="app/templates")

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/ege", response_class=HTMLResponse)
async def get_ege_subjects(request: Request):
    return templates.TemplateResponse("ege.html", {"request": request})

@app.get("/advanced", response_class=HTMLResponse)
async def get_advanced_subjects(request: Request):
    return templates.TemplateResponse("advanced.html", {"request": request})