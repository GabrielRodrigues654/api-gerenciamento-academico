from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    email: str
    matricula: str
    periodo: str

class AlunoCreate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int

    class Config:
        from_attributes = True
