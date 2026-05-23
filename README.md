# API — SaaS de Barbearia

API REST desenvolvida com Django REST Framework para um sistema SaaS de barbearia. O projeto permite o cadastro de clientes, autenticação com JWT, gerenciamento de serviços e controle de agendamentos entre clientes e barbeiros.

A aplicação utiliza autenticação via JSON Web Token, com geração de access token e refresh token. As rotas protegidas exigem o envio do token no header `Authorization: Bearer <access_token>`.

## Principais funcionalidades

- Cadastro de clientes
- Login com JWT
- Renovação de token com refresh token
- Listagem de serviços disponíveis
- CRUD de serviços restrito a usuários administradores
- Criação de agendamentos por clientes
- Listagem de agendamentos conforme o perfil do usuário autenticado
- Controle de permissões para cliente, barbeiro e admin
- Validação de dados nos serializers
- Tratamento de erros HTTP como 400, 401, 403 e 404

## Entidades principais

- Usuário
- Perfil
- Serviço
- Agendamento

## Perfis do sistema

O sistema trabalha com três tipos de perfil:

- `cliente`: pode criar e visualizar seus próprios agendamentos.
- `barbeiro`: pode visualizar os agendamentos em que está associado como barbeiro.
- `admin`: pode gerenciar serviços e visualizar os agendamentos do sistema.

## Endpoints principais

- `POST /api/registro/` — cadastro de cliente
- `POST /api/token/` — login e geração dos tokens JWT
- `POST /api/token/refresh/` — renovação do access token
- `GET /api/servicos/` — listagem de serviços
- `POST /api/servicos/` — criação de serviço por admin
- `PUT/PATCH/DELETE /api/servicos/{id}/` — gerenciamento de serviços por admin
- `GET /api/agendamentos/` — listagem de agendamentos conforme o perfil logado
- `POST /api/agendamentos/` — criação de agendamento por cliente
- `PUT/PATCH/DELETE /api/agendamentos/{id}/` — atualização ou remoção de agendamentos permitidos ao usuário

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite/PostgreSQL
- Django Admin

## Objetivo do projeto

Este backend foi desenvolvido para servir como base de uma aplicação de barbearia, permitindo a integração com um front-end moderno e oferecendo uma estrutura inicial para autenticação, permissões, serviços e agendamentos.
