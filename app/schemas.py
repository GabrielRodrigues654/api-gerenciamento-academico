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

```
class Config:
    from_attributes = True
```

class ProfessorBase(BaseModel):
nome: str
email: str
especialidade: str

class ProfessorCreate(ProfessorBase):
pass

class Professor(ProfessorBase):
id: int

```
class Config:
    from_attributes = True
```

class DisciplinaBase(BaseModel):
nome: str
codigo: str
carga_horaria: int
professor_responsavel: str

class DisciplinaCreate(DisciplinaBase):
pass

class Disciplina(DisciplinaBase):
id: int

```
class Config:
    from_attributes = True
```

class TurmaBase(BaseModel):
disciplina: str
semestre: str
ano: int
vagas: int

class TurmaCreate(TurmaBase):
pass

class Turma(TurmaBase):
id: int

```
class Config:
    from_attributes = True
```

class MatriculaBase(BaseModel):
aluno: str
turma: str
data_matricula: str

class MatriculaCreate(MatriculaBase):
pass

class Matricula(MatriculaBase):
id: int

```
class Config:
    from_attributes = True
```

class NotaBase(BaseModel):
aluno: str
disciplina: str
nota: int

class NotaCreate(NotaBase):
pass

class Nota(NotaBase):
id: int

```
class Config:
    from_attributes = True
```
