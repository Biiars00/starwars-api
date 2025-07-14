from fastapi import FastAPI
from src.routers import router

app = FastAPI(
    title="Star Wars API com Swagger",
    description="API para consulta de recursos da franquia Star Wars documentado com Swagger via FastAPI.",
    version="1.0.0"
)

app.include_router(router) 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
    