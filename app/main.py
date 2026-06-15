from fastapi import FastAPI

app = FastAPI(
    title="API Gerenciamento Acadêmico"
)

@app.get("/")
def home():
    return {
        "mensagem": "API Acadêmica funcionando com sucesso!"
    }

@app.get("/alunos")
def listar_alunos():
    return [
        {
            "id": 1,
            "nome": "João Silva",
            "email": "joao@email.com"
        }
    ]
    @app.get("/professores")
def listar_professores():
    return [
        {
            "id": 1,
            "nome": "Maria Souza",
            "email": "maria@email.com",
            "especialidade": "Banco de Dados"
        }
    ]
