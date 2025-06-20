# API-LOGIN-REGISTER
Esta é uma aplicação basica integrando Backend com Frontend, criando um Dashbord com login, e cadastro com todos os dados sendo indexados a um banco de dados no PostGress

Para ultilizar é necessario ter instalado em sua maquina ou ambiente virtual o SqlModel, django, python, FastAPI e Uvicorn para fazer o acesso localmente
Em Backend/Config.py é necessario adicionar a URL da sua db

Para rodar a aplicação ultilize o comando:'uvicorn: app:FastAPI -- reload' e em outro prompt dentro da pasta "Frontend" ultilize o comando py manage.py runserver 8001"

O Uvicorn rodará a parte do backend na porta 8000 e o Frontend rodará na porta 8001

Este projeto conta com um artigo descrevendo cada principal função e suas ultilzações e a #complexidade de cada uma.
Projeto desenvolvido por: Pedro Cavalcanti Coquito e Matheus Soares Simão
