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
# 1. Criar e ativar virtualenv
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar ambiente
cp .env.example .env
# Edite o .env se for usar PostgreSQL

# 4. Migrations
python manage.py makemigrations
python manage.py migrate

# 5. Criar perfis iniciais + superuser
python manage.py shell -c "
from apps.users.models import Perfil
for d in ['Aluno', 'Professor', 'Administrador']:
    Perfil.objects.get_or_create(descricao=d)
print('Perfis criados.')
"
python manage.py createsuperuser

# 6. Rodar
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

## Autenticação (Frontend)

```javascript
// Login
const { data } = await api.post('/auth/login/', { email, password });
localStorage.setItem('access_token', data.access);
localStorage.setItem('refresh_token', data.refresh);

// Header em todas as requisições
Authorization: Bearer <access_token>
```

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
