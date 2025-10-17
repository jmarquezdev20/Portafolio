#!/bin/bash
# build.sh - Script para preparar Django para producció
set -o errexit
# 2. Instalar dependencias actualizadas
pip install -r requirements.txt

# 4. Recolectar archivos estáticos
python manage.py collectstatic --noinput
ptrhon manage.py migrate