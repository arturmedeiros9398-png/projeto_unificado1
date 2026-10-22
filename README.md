# Projeto Unificado – Prevenção Escolar

Backend Django unificado dos módulos:
- Prevenção às Drogas
- Saúde Mental
- Qualidade de Vida

Com **banco único** + **autenticação centralizada (JWT)**.


TESTE DE PULL E PUSH

---

## Estrutura

```
projeto_unificado/
├── config/                 # Settings, URLs
├── apps/
│   ├── users/              # Auth + Usuario + Perfil
│   ├── comum/              # Administrador + Categoria (compartilhados)
│   ├── drogas/             # Conteúdo, FAQ, Canal, Relato, Avaliação
│   ├── saude_mental/       # Conteúdo, FAQ, Canal, Relato
│   └── qualidade_vida/     # Conteúdo, FAQ, Canal, Relato
├── manage.py
├── requirements.txt
└── .env.example
```

---

## Setup rápido

```bash
# 1. Criar uma pasta vazia, abrir o terminal e rodar os seguintes comandos:

# 2. Clonar o repositório:
git clone https://github.com/arturmedeiros9398-png/projeto_unificado1

# 3. Acessar o projeto
cd projeto_unificado1

# 4. Criar o Venv
python -m venv venv

# 5. Ativar o ambiente virtual
venv\Scripts\activate    # Windows

# 6. Instalar dependências
pip install -r requirements.txt

# 7. Migrations
python manage.py makemigrations
python manage.py migrate

# 8. Criar o superuser (email, nome, data de nascimento e senha)
python manage.py createsuperuser

# 9. Rodar
python manage.py runserver
```

---

## Endpoints principais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/auth/login/` | Login (retorna access + refresh + user) |
| POST | `/api/auth/register/` | Cadastro |
| POST | `/api/auth/refresh/` | Renovar access token |
| GET | `/api/auth/me/` | Dados do usuário logado |
| GET | `/api/auth/perfis/` | Listar perfis |
| GET/POST | `/api/comum/categorias/` | Categorias (compartilhadas) |
| GET/POST | `/api/drogas/conteudos/` | Conteúdos do módulo Drogas |
| POST | `/api/drogas/conteudos/{id}/avaliar/` | Avaliar conteúdo |
| GET/POST | `/api/drogas/faqs/` | FAQs Drogas |
| GET/POST | `/api/drogas/canais-apoio/` | Canais de apoio Drogas |
| POST | `/api/drogas/relatos/` | Relato anônimo Drogas |
| ... | `/api/saude-mental/...` | Mesmo padrão |
| ... | `/api/qualidade-vida/...` | Mesmo padrão |
| GET | `/api/docs/` | Swagger UI |

---

## Permissões

| Ação | Quem pode |
|------|-----------|
| Listar/ver conteúdos publicados | Qualquer um |
| Criar/editar conteúdos | Professor ou Admin |
| Gerenciar FAQs, Canais | Admin |
| Criar relato anônimo | Qualquer um (sem login) |
| Ver relatos | Admin |
| Avaliar conteúdo (Drogas) | Usuário autenticado |

---

## Próximos passos sugeridos

1. Rodar as migrations e criar o superuser
2. Cadastrar algumas categorias pelo admin ou API
3. Cada grupo preencher os conteúdos do seu módulo
4. Integrar o frontend React com os endpoints acima
5. Em produção: trocar para PostgreSQL e configurar `SECRET_KEY` forte
