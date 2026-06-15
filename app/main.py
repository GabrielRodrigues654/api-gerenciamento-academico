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
    @app.get("/disciplinas")
def listar_disciplinas():
    return [
        {
            "id": 1,
            "nome": "Banco de Dados",
            "codigo": "BD001",
            "carga_horaria": 80,
            "professor_responsavel": "Maria Souza"
        }
    ]
@app.get("/turmas")
def listar_turmas():
    return [
        {
            "id": 1,
            "disciplina": "Banco de Dados",
            "semestre": "1",
            "ano": 2025,
            "vagas": 40
        }
    ]


@app.get("/matriculas")
def listar_matriculas():
    return [
        {
            "id": 1,
            "aluno": "João Silva",
            "turma": "Banco de Dados - 2025",
            "data_matricula": "2025-01-10"
        }
    ]


@app.get("/notas")
def listar_notas():
    return [
        {
            "id": 1,
            "aluno": "João Silva",
            "disciplina": "Banco de Dados",
            "nota": 9
        }
    ]
