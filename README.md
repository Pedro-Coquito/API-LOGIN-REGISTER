## 🚀 API de Autenticação (Login & Register)
Este projeto é uma API RESTful de autenticação desenvolvida para gerenciar o registro e login de usuários de forma segura, utilizando as tecnologias mais modernas do ecossistema Python.

## 🛠️ Tecnologias Utilizadas
Python 3.12.1

FastAPI

Uvicorn (ASGI server)

Pydantic (validação de dados)

JWT (JSON Web Token) para autenticação

Hash de senha (bcrypt/passlib)

PostgreSQL

## 📌 Funcionalidades
[x] Registro de Usuários: Criação de novos usuários com senha criptografada (BCrypt).

[x] Login: Autenticação de credenciais e geração de Token JWT.

[x] Proteção de Rotas: Apenas usuários autenticados podem acessar endpoints específicos.

[x] Validação de Dados: Uso de @Valid para garantir a integridade das requisições.


## 🚀 Como clonar e rodar

Abra o seu terminal e execute os comandos abaixo:

```bash
# Clonar o repositório
git clone https://github.com/Pedro-Coquito/API-LOGIN-REGISTER.git

# Entrar na pasta do projeto
cd API-LOGIN-REGISTER

# Criar um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rodar a aplicação com uvicorn
uvicorn app.main:app --reload

```
Método,Endpoint,Descrição,Proteção
POST,/register,Cria um novo usuário,Pública
POST,/login,Gera o token JWT,Pública
GET,/profile,Retorna dados do perfil,Privada (JWT)

## 🛣️ Endpoints da API

| Método | Endpoint | Descrição | Autenticação |
| :--- | :--- | :--- | :--- |
| `POST` | `/login` | Autentica usuário e gera token JWT | Publica |
| `POST` | `/register` | Cria um novo usuário no sistema | Publica |
| `GET` | `/profile` | Retorna dados do perfil | Privada JWT |

