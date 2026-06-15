from sqlalchemy import Column, Integer, String
from database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    matricula = Column(String, unique=True)
    periodo = Column(String)
    
   class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    especialidade = Column(String)


class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    codigo = Column(String, unique=True)
    carga_horaria = Column(Integer)
    professor_responsavel = Column(String)
class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)
    aluno = Column(String)
    turma = Column(String)
    data_matricula = Column(String)


class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, index=True)
    aluno = Column(String)
    disciplina = Column(String)
    nota = Column(Integer)

class Turma(Base):
    __tablename__ = "turmas"

    id = Column(Integer, primary_key=True, index=True)
    disciplina = Column(String)
    semestre = Column(String)
    ano = Column(Integer)
    vagas = Column(Integer)
