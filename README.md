# Sistema-de-Gerenciamento-Compartilhado-de-Recursos-da-Universidade---SIGCRU

Criar e Ativar o Ambiente Virtual (venv )
python -m venv venv

venv/Scripts/activate

pip install -r requirements.txt

Criar Migrações (se necessário)

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
