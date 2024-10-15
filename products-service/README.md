# Fastify Product API

Esta é uma API RESTful simples desenvolvida com **Fastify**, **MongoDB**, e **Docker**, seguindo os princípios de **Clean Architecture**, **SOLID**, e **Clean Code**. A API permite listar, buscar e adicionar produtos, com ênfase em performance, cobertura de testes e tratamento de erros.

## Funcionalidades

- Listagem de até 40 produtos
- Busca de produtos por nome ou descrição
- Adição de produtos ao banco de dados
- Documentação via Swagger

## Tecnologias Utilizadas

- **Node.js** com **Fastify**
- **MongoDB** para persistência de dados
- **Swagger** para documentação da API
- **Docker** e **Docker Compose** para orquestração de serviços
- **Jest** e **Supertest** para testes automatizados

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter instalado:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Como Rodar

### 1. Clonar o Repositório

### 2. Configurar Variáveis de Ambiente

Crie um arquivo .env no diretório raiz e adicione as seguintes variáveis:


MONGO_URL=mongodb://mongo:27017/mydb

### 3. Rodar com Docker Compose
Inicie os contêineres com o Docker Compose:


docker-compose up --build
Isso irá levantar tanto o servidor da API quanto o MongoDB. A API estará disponível em http://localhost:3000.

### 4. Acessar a Documentação da API
A documentação da API, gerada via Swagger, pode ser acessada em:


http://localhost:3000/docs

### API em python 
Esta é a API inicial da loja **Cosméticos-co**, desenvolvida com **Node.js** para atender às funcionalidades básicas do sistema. Essa versão é um **MVP (Minimum Viable Product)**, estando em construção uma api com uma arquitetura mais escalável e robusta, baseada em **microserviços** com **Python** ,**SQL** e **FastAPI**.

https://github.com/leocalazans/cosmetics-microservices

