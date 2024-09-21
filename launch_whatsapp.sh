#!/bin/bash

# Configura el logging
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>/tmp/whatsapp_launch.log 2>&1

# Imprime información de depuración
echo "Script iniciado: $(date)"
echo "Usuario actual: $(whoami)"
echo "Directorio actual: $(pwd)"

# Cambia al directorio del proyecto
cd /home/carlosn/proyectos/whatsapp_fl || { echo "No se pudo cambiar al directorio del proyecto"; exit 1; }
echo "Cambiado al directorio: $(pwd)"

# Crea un entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "Creando el entorno virtual..."
    python -m venv venv || { echo "No se pudo crear el entorno virtual"; exit 1; }
    echo "Entorno virtual creado"
fi

# Activa el entorno virtual
source venv/bin/activate || { echo "No se pudo activar el entorno virtual"; exit 1; }
echo "Entorno virtual activado"

# Imprime información sobre el entorno Python
echo "Python path: $(which python)"
echo "Python version: $(python --version)"

# Ejecuta el script Python en segundo plano
echo "Ejecutando app.py en segundo plano..."
nohup python app.py >/dev/null 2>&1 &

# Espera un momento para asegurarse de que la aplicación se inicie
sleep 5

echo "Script finalizado: $(date)"
