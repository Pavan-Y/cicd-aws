from fastapi import FastAPI,Response

app = FastAPI()

@app.get('/')
def main():
    return Response(content="Application is running...", media_type="text/plain")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='0.0.0.0',port=8000)
    