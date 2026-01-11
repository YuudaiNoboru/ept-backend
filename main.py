from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utilidades.database import criar_tabelas
from routes.usuarios import router as usuario_router
from routes.token import router as token_router
from routes.assuntos import router as assunto_router
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

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
app.include_router(token_router, prefix="/api")
app.include_router(assunto_router)

# Configuração do OAuth2 para o Swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

# Personalização do OpenAPI para incluir autenticação
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="API de Estudos",
        version="1.0.0",
        description="API para gerenciamento de estudos",
        routes=app.routes,
    )
    
    # Adicionar componente de segurança
    openapi_schema["components"] = {
        "securitySchemes": {
            "OAuth2PasswordBearer": {
                "type": "oauth2",
                "flows": {
                    "password": {
                        "tokenUrl": "api/token",
                        "scopes": {}
                    }
                }
            }
        }
    }
    
    # Aplicar segurança global
    openapi_schema["security"] = [{"OAuth2PasswordBearer": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Rota de exemplo
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de estudos!"}