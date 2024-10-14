# Estrutura de Microservices para Cosméticos-co

Após a entrega do MVP inicial utilizando Node.js, estamos em fase de desenvolvimento de uma API mais complexa e robusta utilizando **Python** com **FastAPI**. Abaixo está uma descrição das tecnologias e arquitetura que compõem a nova versão dos microserviços.

## 1. Estrutura de Microservices
- **FastAPI** para criação de cada microserviço, incluindo APIs para **produtos**, **carrinho** e **autenticação**.
- **Celery** para processamento de tarefas assíncronas, como envio de emails e operações de banco de dados demoradas.
- **Redis** para gerenciar filas de mensagens (usado pelo Celery) e para caching de dados.
- **RabbitMQ** ou **Kafka** para mensageria entre microserviços, garantindo comunicação rápida e eficiente.

## 2. Bancos de Dados SQL e NoSQL
- **PostgreSQL** como banco de dados **SQL**, para informações transacionais (produtos, usuários, pedidos).
- **MongoDB** como banco **NoSQL**, ideal para dados não estruturados ou semi-estruturados, como logs, históricos de navegação, e informações de busca.

## 3. Estrutura de Serviços
Os microserviços são divididos da seguinte maneira:

- **Serviço de Produtos**: gerencia listagem, busca e detalhes dos produtos (banco SQL ou NoSQL)(Dev).
- **Serviço de Autenticação/Usuários**: gerencia login, logout e controle de usuários (usando JWT ou OAuth).
- **Serviço de Carrinho/Pedidos**: gerencia o carrinho de compras, checkout e integração com sistemas de pagamento(Dev).
- **Serviço de Processamento Assíncrono**: utiliza Celery e Redis para processar operações demoradas (ex. envio de emails, relatórios)(Dev).

## 4. Testes com TDD e BDD
- **TDD (Test-Driven Development)**: Escrito testes unitários e funcionais com frameworks como **Pytest**.
- **BDD (Behavior-Driven Development)**: Utilizado **Behave** para descrever cenários de comportamento de negócios.

## 5. Orquestração e Infraestrutura com Kubernetes
- Cada microserviço é containerizado utilizando **Docker**.
- Utilizamos **Kubernetes (K8s)** para orquestração de containers e deploy dos microserviços.
- Configuramos **Deployments** e **Services** para cada microserviço.
- Utilizamos **ConfigMaps** e **Secrets** para gerenciar variáveis de ambiente.
- Implementamos **Istio** para gerenciar tráfego de rede entre os serviços.

## 6. Mensageria com Kafka e RabbitMQ
- **Kafka** para stream de dados em tempo real (ex. logs de usuários ou eventos de sistema).
- **RabbitMQ** para mensageria rápida e confiável entre microserviços (ex. notificação de criação de pedidos ao serviço de estoque).

## 7. CI/CD com AWS/GCP
- Pipelines de **CI/CD** são configurados utilizando **GitHub Actions**.
- Deploy automático na é configurado com **Terraform**, para gerenciar a infraestrutura como código.
- Cada microserviço possui um **Dockerfile**, **utilizado** para desenvolvimento local.

## 8. Infraestrutura como Código (IaC) com Terraform
- **Terraform** é utilizado para provisionar toda a infraestrutura, como clusters Kubernetes, bancos de dados (SQL e NoSQL), Redis, Kafka e RabbitMQ, tanto na AWS quanto na GCP.

## 9. Configurações de Observabilidade
- Monitoramento de microserviços com **Prometheus** e **Grafana**.
- **Elastic Stack (ELK)** é utilizado para logging distribuído e análise de logs.

## 10. Balanceamento de Carga e Gestão de Tráfego com Istio
- Implementamos **Istio** para balanceamento de carga, gestão de tráfego, segurança (mTLS), e monitoramento de requisições.

---

Esta arquitetura visa a escalabilidade, modularidade e alta disponibilidade, aproveitando o poder de microserviços para criar uma solução robusta e eficiente para uma loja de cosméticos.
