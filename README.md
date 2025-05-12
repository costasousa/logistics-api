# API de Gerenciamento de Entregas e Motoristas

Uma API RESTful desenvolvida com **FastAPI** e **PostgreSQL** para gerenciar motoristas e entregas, com persistência de dados e operações CRUD.

---

## Funcionalidades Principais

### **Motoristas**
- **Criar motorista**: Registre novos motoristas com nome e placa do veículo.
- **Listar motoristas**: Obtenha a lista completa de motoristas cadastrados.

### **Entregas**
-  **Criar entrega**: Registre novas entregas com detalhes do pacote e destino.
-  **Listar entregas**: Filtre entregas por status (`pending`, `in_transit`, `delivered`).
-  **Atribuir motorista**: Associe um motorista a uma entrega específica.
-  **Atualizar status**: Altere o status da entrega conforme o progresso.

---

## Tecnologias Utilizadas

| Tecnologia          | Descrição                                  |
|---------------------|--------------------------------------------|
| **FastAPI**         | Framework para construção da API           |
| **PostgreSQL**      | Banco de dados relacional                  |
| **SQLAlchemy**      | ORM para integração com o PostgreSQL       |
| **Docker**          | Containerização da aplicação e do banco    |
| **Pydantic**        | Validação de dados e modelos               |

---

## ⚙️ Pré-requisitos

- Docker 
- Docker Compose 

---
