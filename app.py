import logging
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from webdriver_manager.chrome import ChromeDriverManager

# Configuración del logging
logging.basicConfig(
    filename='/tmp/whatsapp_app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info(f"Script iniciado. Directorio de trabajo: {os.getcwd()}")
logging.info(f"Ejecutable de Python: {sys.executable}")
logging.info(f"Versión de Python: {sys.version}")
logging.info(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'No establecido')}")

def main():
    logging.info("Aplicación iniciada")

    # Configura las opciones del navegador
    chrome_options = Options()
    chrome_options.add_argument("--app=https://web.whatsapp.com/")
    chrome_options.add_argument("--window-size=1024,768")
    chrome_options.add_argument("--window-position=center")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--enable-notifications")
    chrome_options.add_argument("--use-system-clipboard")
    chrome_options.add_argument("--password-store=basic")

    # Configurar el directorio de usuario para Chrome
    user_data_dir = os.path.expanduser('~/.config/google-chrome')
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")

    # Especifica la ruta correcta de chromedriver
    service = Service("/usr/bin/chromedriver")

    # Añadir opciones para el icono y la clase de ventana
    chrome_options.add_argument('--class=WhatsApp')
    chrome_options.add_argument(f'--icon=/home/carlosn/proyectos/whatsapp_fl/static/img/whatsapp_icon.png')

    try:
        # Inicializa el navegador con el servicio y opciones
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logging.info("Navegador Chrome iniciado correctamente")

        # Mantén la ventana abierta hasta que el usuario la cierre
        while True:
            try:
                driver.current_url
            except:
                break

    except Exception as e:
        logging.exception("Se produjo un error al iniciar el navegador")

    finally:
        try:
            driver.quit()
            logging.info("Navegador Chrome cerrado correctamente")
        except Exception as e:
            logging.warning("Error al intentar cerrar el navegador")

    logging.info("Aplicación finalizada")

if __name__ == "__main__":
    logging.info(f"Versión de Python: {sys.version}")
    try:
        main()
    except Exception as e:
        logging.exception("Se produjo un error en la ejecución del programa")