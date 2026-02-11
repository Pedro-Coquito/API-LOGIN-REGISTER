🚀 API de Autenticação (Login & Register)
Este projeto é uma API RESTful de autenticação desenvolvida para gerenciar o registro e login de usuários de forma segura, utilizando as tecnologias mais modernas do ecossistema Java.

🛠️ Tecnologias Utilizadas
Java 21 (LTS)

Spring Boot 3.x

Spring Security (Autenticação e Autorização)

JSON Web Token (JWT) (Para tokens de acesso seguros)

Spring Data JPA (Persistência de dados)

PostgreSQL/MySQL/H2 (Especifique qual você usou)

Lombok (Produtividade no código)

Maven (Gerenciador de dependências)

📌 Funcionalidades
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

# Rodar a aplicação com Maven
mvn spring-boot:run
