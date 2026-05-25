# API Backend - Sistema de Barbearia

API desenvolvida para o sistema de barbearia, responsável por gerenciar usuários, perfis, serviços e agendamentos.

O backend foi desenvolvido com **Python**, **Django** e **Django REST Framework**, utilizando autenticação via **JWT**. A API permite cadastro de clientes, login, gerenciamento de barbeiros, serviços e controle de agendamentos.

## Principais funcionalidades

- Cadastro de clientes
- Login com JWT
- Gerenciamento de perfis
- Cadastro de barbeiros pelo admin
- Cadastro e gerenciamento de serviços
- Criação e controle de agendamentos
- Controle de permissões por tipo de usuário:
  - Admin
  - Barbeiro
  - Cliente

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL ou SQLite
- Docker

---

## Como rodar o projeto normalmente

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_PROJETO
```

### 2. Criar e ativar o ambiente virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar um superusuário

```bash
python manage.py createsuperuser
```

### 6. Rodar o servidor

```bash
python manage.py runserver
```

A API ficará disponível em:

```txt
http://127.0.0.1:8000/
```

---

## Como rodar com Docker

### 1. Subir os containers

```bash
docker compose up --build
```

ou, dependendo da versão do Docker:

```bash
docker-compose up --build
```

### 2. Rodar as migrações dentro do container

Se o serviço do backend no `docker-compose.yml` se chamar `web`:

```bash
docker compose exec web python manage.py migrate
```

Se o serviço tiver outro nome, substitua `web` pelo nome correto.

### 3. Criar um superusuário dentro do container

```bash
docker compose exec web python manage.py createsuperuser
```

### 4. Acessar a API

```txt
http://localhost:8000/
```

---

## Endpoints principais

```txt
POST /api/token/
POST /api/token/refresh/

POST /api/clientes/
POST /api/usuarios/
GET  /api/perfis/

GET  /api/servicos/
POST /api/servicos/

GET  /api/agendamentos/
POST /api/agendamentos/
```

---

## Autenticação

Para acessar rotas protegidas, envie o token JWT no header da requisição:

```http
Authorization: Bearer SEU_TOKEN
```

---

## Observação

As configurações de banco de dados, variáveis de ambiente e Docker podem variar conforme o ambiente de execução do projeto.
