# Endpoints - Sistema de Barbearia

Base da API:

```txt
/api/
```

Autenticação nas rotas protegidas:

```http
Authorization: Bearer SEU_ACCESS_TOKEN
```

---

## Tabela de endpoints

| Método | Endpoint | Permissão | Descrição |
|---|---|---|---|
| `POST` | `/api/token/` | Público | Faz login e retorna os tokens JWT |
| `POST` | `/api/token/refresh/` | Público | Gera um novo access token |
| `POST` | `/api/clientes/` | Público | Cadastra um novo cliente |
| `POST` | `/api/usuarios/` | Admin | Cadastra usuário do tipo `barbeiro` ou `cliente` |
| `GET` | `/api/perfis/` | Autenticado | Lista perfis. Admin vê todos; outros veem apenas o próprio |
| `GET` | `/api/perfis/{id}/` | Autenticado | Detalha um perfil |
| `PUT` | `/api/perfis/{id}/` | Autenticado | Atualiza completamente um perfil |
| `PATCH` | `/api/perfis/{id}/` | Autenticado | Atualiza parcialmente um perfil |
| `GET` | `/api/servicos/` | Autenticado | Lista serviços |
| `POST` | `/api/servicos/` | Admin | Cadastra serviço |
| `GET` | `/api/servicos/{id}/` | Autenticado | Detalha serviço |
| `PUT` | `/api/servicos/{id}/` | Admin | Atualiza completamente um serviço |
| `PATCH` | `/api/servicos/{id}/` | Admin | Atualiza parcialmente um serviço |
| `DELETE` | `/api/servicos/{id}/` | Admin | Remove serviço |
| `GET` | `/api/agendamentos/` | Autenticado | Lista agendamentos conforme o tipo do usuário |
| `POST` | `/api/agendamentos/` | Cliente | Cria agendamento |
| `GET` | `/api/agendamentos/{id}/` | Autenticado | Detalha agendamento conforme permissão |
| `PUT` | `/api/agendamentos/{id}/` | Autenticado | Atualiza completamente um agendamento |
| `PATCH` | `/api/agendamentos/{id}/` | Autenticado | Atualiza parcialmente um agendamento |
| `DELETE` | `/api/agendamentos/{id}/` | Autenticado | Remove agendamento conforme permissão |

---

## Regras rápidas de permissão

| Perfil | O que pode fazer |
|---|---|
| Público | Criar conta de cliente e fazer login |
| Cliente | Ver/editar próprio perfil, ver/criar/alterar/remover seus agendamentos |
| Barbeiro | Ver próprio perfil e seus agendamentos |
| Admin | Gerenciar usuários, perfis, serviços e todos os agendamentos |
| Superuser | Tem acesso administrativo total |

---

# Exemplos de request e response

## Login

### `POST /api/token/`

Request:

```json
{
  "email": "admin@admin.com",
  "password": "admin123"
}
```

Response:

```json
{
  "refresh": "token_refresh",
  "access": "token_access"
}
```

---

## Refresh token

### `POST /api/token/refresh/`

Request:

```json
{
  "refresh": "token_refresh"
}
```

Response:

```json
{
  "access": "novo_token_access"
}
```

---

## Cadastrar cliente

### `POST /api/clientes/`

Request:

```json
{
  "nome": "João Silva",
  "telefone": "83999999999",
  "email": "joao@email.com",
  "password": "123456"
}
```

Response:

```json
{
  "id": 1,
  "nome": "João Silva",
  "telefone": "83999999999",
  "tipo": "cliente",
  "email": "joao@email.com"
}
```

---

## Cadastrar barbeiro ou cliente pelo admin

### `POST /api/usuarios/`

Request para criar barbeiro:

```json
{
  "nome": "Carlos Barbeiro",
  "telefone": "83988888888",
  "email": "carlos@barbearia.com",
  "password": "123456",
  "tipo": "barbeiro"
}
```

Request para criar cliente:

```json
{
  "nome": "Maria Cliente",
  "telefone": "83977777777",
  "email": "maria@email.com",
  "password": "123456",
  "tipo": "cliente"
}
```

Response:

```json
{
  "id": 2,
  "nome": "Carlos Barbeiro",
  "telefone": "83988888888",
  "tipo": "barbeiro",
  "email": "carlos@barbearia.com"
}
```

---

## Listar perfis

### `GET /api/perfis/`

Response:

```json
[
  {
    "id": 1,
    "nome": "João Silva",
    "telefone": "83999999999",
    "tipo": "cliente",
    "email": "joao@email.com"
  }
]
```

---

## Detalhar perfil

### `GET /api/perfis/{id}/`

Response:

```json
{
  "id": 1,
  "nome": "João Silva",
  "telefone": "83999999999",
  "tipo": "cliente",
  "email": "joao@email.com"
}
```

---

## Atualizar perfil

### `PUT /api/perfis/{id}/`

Request:

```json
{
  "nome": "João Silva Atualizado",
  "telefone": "83999990000"
}
```

Response:

```json
{
  "id": 1,
  "nome": "João Silva Atualizado",
  "telefone": "83999990000",
  "tipo": "cliente",
  "email": "joao@email.com"
}
```

---

## Atualizar perfil parcialmente

### `PATCH /api/perfis/{id}/`

Request:

```json
{
  "telefone": "83999990000"
}
```

Response:

```json
{
  "id": 1,
  "nome": "João Silva",
  "telefone": "83999990000",
  "tipo": "cliente",
  "email": "joao@email.com"
}
```

---

## Cadastrar serviço

### `POST /api/servicos/`

Request:

```json
{
  "nome": "Corte Masculino",
  "valor": "35.00",
  "duracao_minutos": 30
}
```

Response:

```json
{
  "id": 1,
  "nome": "Corte Masculino",
  "valor": "35.00",
  "duracao_minutos": 30
}
```

---

## Listar serviços

### `GET /api/servicos/`

Response:

```json
[
  {
    "id": 1,
    "nome": "Corte Masculino",
    "valor": "35.00",
    "duracao_minutos": 30
  }
]
```

---

## Detalhar serviço

### `GET /api/servicos/{id}/`

Response:

```json
{
  "id": 1,
  "nome": "Corte Masculino",
  "valor": "35.00",
  "duracao_minutos": 30
}
```

---

## Atualizar serviço

### `PUT /api/servicos/{id}/`

Request:

```json
{
  "nome": "Corte Premium",
  "valor": "45.00",
  "duracao_minutos": 40
}
```

Response:

```json
{
  "id": 1,
  "nome": "Corte Premium",
  "valor": "45.00",
  "duracao_minutos": 40
}
```

---

## Atualizar serviço parcialmente

### `PATCH /api/servicos/{id}/`

Request:

```json
{
  "valor": "40.00"
}
```

Response:

```json
{
  "id": 1,
  "nome": "Corte Masculino",
  "valor": "40.00",
  "duracao_minutos": 30
}
```

---

## Remover serviço

### `DELETE /api/servicos/{id}/`

Response:

```txt
204 No Content
```

---

## Criar agendamento

### `POST /api/agendamentos/`

O campo `cliente` não deve ser enviado. Ele é definido automaticamente pelo usuário logado.

Request:

```json
{
  "barbeiro": 2,
  "servicos": [1, 2],
  "data_hora": "2026-05-25T14:00:00Z"
}
```

Response:

```json
{
  "id": 1,
  "cliente": 3,
  "barbeiro": 2,
  "servicos": [1, 2],
  "data_hora": "2026-05-25T14:00:00Z",
  "hora_fim": "2026-05-25T14:50:00Z",
  "valor_total": "60.00",
  "duracao_total_minutos": 50
}
```

---

## Listar agendamentos

### `GET /api/agendamentos/`

Response:

```json
[
  {
    "id": 1,
    "cliente": 3,
    "barbeiro": 2,
    "servicos": [1, 2],
    "data_hora": "2026-05-25T14:00:00Z",
    "hora_fim": "2026-05-25T14:50:00Z",
    "valor_total": "60.00",
    "duracao_total_minutos": 50
  }
]
```

---

## Detalhar agendamento

### `GET /api/agendamentos/{id}/`

Response:

```json
{
  "id": 1,
  "cliente": 3,
  "barbeiro": 2,
  "servicos": [1, 2],
  "data_hora": "2026-05-25T14:00:00Z",
  "hora_fim": "2026-05-25T14:50:00Z",
  "valor_total": "60.00",
  "duracao_total_minutos": 50
}
```

---

## Atualizar agendamento

### `PUT /api/agendamentos/{id}/`

Request:

```json
{
  "barbeiro": 2,
  "servicos": [1],
  "data_hora": "2026-05-25T15:00:00Z"
}
```

Response:

```json
{
  "id": 1,
  "cliente": 3,
  "barbeiro": 2,
  "servicos": [1],
  "data_hora": "2026-05-25T15:00:00Z",
  "hora_fim": "2026-05-25T15:30:00Z",
  "valor_total": "35.00",
  "duracao_total_minutos": 30
}
```

---

## Atualizar agendamento parcialmente

### `PATCH /api/agendamentos/{id}/`

Request:

```json
{
  "data_hora": "2026-05-25T16:00:00Z"
}
```

Response:

```json
{
  "id": 1,
  "cliente": 3,
  "barbeiro": 2,
  "servicos": [1, 2],
  "data_hora": "2026-05-25T16:00:00Z",
  "hora_fim": "2026-05-25T16:50:00Z",
  "valor_total": "60.00",
  "duracao_total_minutos": 50
}
```

---

## Remover agendamento

### `DELETE /api/agendamentos/{id}/`

Response:

```txt
204 No Content
```

---

# Observações importantes

## Criação de barbeiro

Não existe endpoint separado `/api/barbeiros/`.

Para criar barbeiro, use:

```txt
POST /api/usuarios/
```

com:

```json
{
  "tipo": "barbeiro"
}
```

## Campos somente leitura

### Perfil

```txt
id
email
tipo
```

### Agendamento

```txt
id
cliente
hora_fim
valor_total
duracao_total_minutos
```

## Validações principais de agendamento

- O usuário precisa estar autenticado.
- Apenas cliente pode criar agendamento.
- O barbeiro precisa ter perfil do tipo `barbeiro`.
- É obrigatório selecionar pelo menos um serviço.
- Não é permitido agendar para uma data/hora no passado.
- O barbeiro não pode ter outro agendamento no mesmo intervalo.
- O cliente não pode ter outro agendamento no mesmo intervalo.
