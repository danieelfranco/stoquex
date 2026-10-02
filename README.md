# Stoquex

Sistema de controle de estoque de equipamentos de TI, feito em Django como projeto de portfólio.

## Funcionalidades

- Cadastro, listagem, detalhe, edição e exclusão de equipamentos
- Vínculo de cada equipamento a um funcionário responsável
- Painel administrativo do Django para gerenciar funcionários e equipamentos

## Tecnologias

- Python e Django
- SQLite
- HTML e CSS

## Como rodar

1. Clone o repositório e entre na pasta:

```
   git clone https://github.com/danieelfranco/stoquex.git
   cd stoquex
```

2. Crie e ative o ambiente virtual:

```
   python -m venv venv
   venv\Scripts\activate
```

3. Instale as dependências:

```
   python -m pip install -r requirements.txt
```

4. Copie o arquivo de exemplo de variáveis de ambiente e preencha com a sua chave:

```
   copy .env.example .env
```

   Para gerar uma chave secreta:

```
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

   Cole a chave no `.env`, em `DJANGO_SECRET_KEY`.

5. Crie o banco e um usuário administrador:

```
   python manage.py migrate
   python manage.py createsuperuser
```

6. Inicie o servidor:

```
   python manage.py runserver
```

7. Acesse `http://127.0.0.1:8000/listaequipamento/`

## Próximos passos

- Status do equipamento com opções fixas
- Template base e estilização com CSS
