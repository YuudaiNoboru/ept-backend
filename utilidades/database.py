from sqlmodel import SQLModel, create_engine, Session

# Configuração do banco de dados
DATABASE_URL = "sqlite:///./meu_banco_de_dados.db"  # Exemplo usando SQLite

# Criação do engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True para ver logs no terminal


# Função para criar as tabelas no banco de dados
def criar_tabelas():
    SQLModel.metadata.create_all(engine)


# Função para obter uma sessão do banco de dados
def get_session():
    with Session(engine) as session:
        yield session
