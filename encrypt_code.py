# Importação das bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import pyperclip

# Lê o conteúdo de um arquivo chamado 'encrypt.txt' e copia para a área de transferência
with open('encrypt.txt', 'r') as arquivo:
    texto_a_copiar = arquivo.read()
pyperclip.copy(texto_a_copiar)

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Maximiza o Chrome
driver.maximize_window()

# Abre o site 
driver.get('https://www.criptografarphp.com.br/site/criptografar-html/')

# Diminui o zoom do navegador 7 vezes
for _ in range(7):
    pyautogui.hotkey('ctrl', '-')

# Localiza o campo de entrada (textarea) no site
campo_entrada = driver.find_element(By.XPATH, "//textarea[@name='code']")

# Clica no campo de entrada
campo_entrada.click()

# Cole o texto da área de transferência no campo de entrada
campo_entrada.send_keys(Keys.CONTROL, 'v')

# Minimiza o Chrome
driver.minimize_window()

# Tenta executar o script JavaScript para criptografar o HTML no site
try:
    driver.execute_script("doencrypt(pageform);")
except Exception as e:
    print("Erro ao localizar o botão de submissão:", str(e))

# Aguarda por 2 segundos
time.sleep(2)

# Tenta localizar o campo de saída onde o HTML criptografado é exibido
try:
    campo_saida = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@name='ecode']"))
    )
    texto_resultado = campo_saida.get_attribute('value')
except Exception as e:
    print("Erro ao localizar o campo de saída:", str(e))
    texto_resultado = ""

# Escreve o texto criptografado em um arquivo chamado 'code_encrypted.txt'
with open('code_encrypted.txt', 'w') as arquivo:
    arquivo.write(texto_resultado)

# Exibe uma mensagem de sucesso
print('Encriptado com sucesso,  verifique o resultado em "code_encrypted.txt"')

# Fecha o navegador
driver.quit()
