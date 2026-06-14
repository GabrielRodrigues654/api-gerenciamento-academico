from fastapi import FastAPI
from app.routes import alunos, disciplinas, matriculas, notas, health

app = FastAPI(title="API Acadêmica")

app.include_router(alunos.router, prefix="/v1/alunos")
app.include_router(disciplinas.router, prefix="/v1/disciplinas")
app.include_router(matriculas.router, prefix="/v1/matriculas")
app.include_router(notas.router, prefix="/v1/notas")
app.include_router(health.router, prefix="/v1/health")


@app.get("/")
def root():
    return {"message": "API rodando"}
