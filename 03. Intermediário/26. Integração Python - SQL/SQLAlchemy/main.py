from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine(f"sqlite:///03. Intermediário/26. Integração Python - SQL/SQLAlchemy/meubanco.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

#Tabelas
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

class Livro(Base):
    __tablename__ = 'livros'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    titulo = Column('titulo', String)
    qtde_paginas = Column('qtde_paginas', Integer)
    dono = Column('dono', ForeignKey('usuarios.id'))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono

Base.metadata.create_all(bind=db)


#CRUD

#CREATE
usuario = Usuario(nome='Paulo', email='paulo@gmail.com', senha='12345')
session.add(usuario)
session.commit()

livro = Livro(titulo='Curso Analise de dados', qtde_paginas=120, dono=1)
session.add(livro)
session.commit()

#READ
lista_usuarios = session.query(Usuario).all()
usuario_paulo = session.query(Usuario).filter_by(nome='Paulo').first()
print(lista_usuarios[0])
print(usuario_paulo.email)

#UPDATE
usuario_paulo.nome = 'Paulo Pinho'
session.add(usuario_paulo)
session.commit()

#DELETE
session.delete(usuario_paulo)
session.commit()