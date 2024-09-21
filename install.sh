#!/bin/bash

# Actualizar el sistema
echo "Actualizando el sistema..."
sudo pacman -Syu --noconfirm

# Instalar dependencias de Python
echo "Instalando Python y pip..."
sudo pacman -S python python-pip --noconfirm

# Instalar dependencias requeridas desde requirements.txt
if [ -f requirements.txt ]; then
    echo "Instalando dependencias de requirements.txt..."
    pip install -r requirements.txt
else
    echo "No se encontró requirements.txt. Asegúrate de que exista."
    exit 1
fi

# Configurar permisos para el script de lanzamiento
echo "Configurando permisos para launch_whatsapp.sh..."
chmod +x /home/carlosn/proyectos/whatsapp_fl/launch_whatsapp.sh

echo "Instalación completada. Puedes lanzar WhatsApp ejecutando ./launch_whatsapp.sh"
