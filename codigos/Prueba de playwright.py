#Prueba de playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)  # headless=True si no quieres ver la ventana
    pagina = navegador.new_page()
    
    # Abrir Google
    pagina.goto("https://icp.administracionelectronica.gob.es/icpplus/index.html")

    #Selecionar provincia
    pagina.select_option("select[name='form']", label="Madrid")

    #Presiona el aceptar del formulario
    pagina.click("#btnAceptar")

    #Pasa a la siguiente pagina

    #Selecionar tranmites
    pagina.select_option("select[name='tramiteGrupo[0]']", "20")

    # Escribir en el buscador
    #pagina.fill("textarea[name='q']", "Hola desde Playwright en Arch Linux")
    
    # Presionar Enter
   # pagina.keyboard.press("Enter")
    
    # Esperar 5 segundos para ver el resultado
    pagina.wait_for_timeout(3000)

    #navegador.close()
