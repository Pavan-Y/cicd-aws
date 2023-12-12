from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="py-app/templates")

@app.get('/')
def main(request: Request):
    content = "Your application is running..."
    return templates.TemplateResponse("index.html", {"request": request, "content": content})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='0.0.0.0',port=8000)
