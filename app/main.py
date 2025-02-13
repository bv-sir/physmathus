from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routers import ege, advanced
from pydantic import BaseModel

class GenerateRequest(BaseModel):
    prompt: str  # Ожидается строка

app = FastAPI()

# Подключаем роутеры
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

@app.get("/chat", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import transformers

model_id = "microsoft/Phi-2"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Модель данных для запроса
class GenerateRequest(BaseModel):
    prompt: str  # Ожидается строка

@app.post("/generate/")
async def generate_text(request: GenerateRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_new_tokens=150)
    return {"generated_text": tokenizer.decode(output[0], skip_special_tokens=True)}