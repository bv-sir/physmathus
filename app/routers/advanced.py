from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Настройка Jinja2
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def get_advanced_subjects(request: Request):
    return templates.TemplateResponse("advanced.html", {"request": request})

@router.get("/math")
def get_advanced_math(request: Request):
    return templates.TemplateResponse("advanced_math.html", {"request": request})

@router.get("/phys")
def get_advanced_phys(request: Request):
    return templates.TemplateResponse("advanced_phys.html", {"request": request})

@router.get("/inf")
def get_advanced_inf(request: Request):
    return templates.TemplateResponse("advanced_inf.html", {"request": request})