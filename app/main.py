from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.ocr import extract_text_from_image
from app.ai_analysis import analyze_scam

app = FastAPI(title="Scam-Shield")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None}
    )


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, file: UploadFile = File(...)):
    extracted_text = extract_text_from_image(await file.read())

    if not extracted_text:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": "Unable to extract text from image"}
        )

    analysis_result = analyze_scam(extracted_text)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "text": extracted_text,
            "result": analysis_result
        }
    )
