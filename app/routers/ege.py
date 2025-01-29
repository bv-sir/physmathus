from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Настройка Jinja2
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def get_ege_subjects(request: Request):
    return templates.TemplateResponse("ege.html", {"request": request})

@router.get("/math")
def get_ege_math(request: Request):
    return templates.TemplateResponse("ege_math.html", {"request": request})

@router.get("/phys")
def get_ege_phys(request: Request):
    return templates.TemplateResponse("ege_phys.html", {"request": request})

@router.get("/inf")
def get_ege_inf(request: Request):
    return templates.TemplateResponse("ege_inf.html", {"request": request})