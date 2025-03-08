from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utilidades.database import criar_tabelas
from routes.usuarios import router as usuario_router

# Criação do aplicativo FastAPI
app = FastAPI()

# Configuração do CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (em produção, restrinja isso)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Cria as tabelas no banco de dados ao iniciar a aplicação
@app.on_event("startup")
def on_startup():
    criar_tabelas()

# Integração das rotas
app.include_router(usuario_router, prefix="/api")

# Rota de exemplo
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de estudos!"}