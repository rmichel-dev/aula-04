#!/usr/bin/env bash
# exit on error
set -o errexit

echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo "🛠 Aplicando migrações..."
python manage.py migrate --noinput

echo "📂 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "✅ Build finalizado com sucesso!"