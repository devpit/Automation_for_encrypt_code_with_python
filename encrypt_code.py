from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import pyperclip

with open('encrypt.txt', 'r') as arquivo:
    texto_a_copiar = arquivo.read()
    
pyperclip.copy(texto_a_copiar)

driver = webdriver.Chrome()
driver.get('https://www.criptografarphp.com.br/site/criptografar-html/')
driver.maximize_window()

for _ in range(7):
 pyautogui.hotkey('ctrl', '-')

campo_entrada = driver.find_element(By.XPATH, "//textarea[@name='code']") 
campo_entrada.click()
campo_entrada.send_keys(Keys.CONTROL, 'v')

try:
    driver.execute_script("doencrypt(pageform);")
except Exception as e:
    print("Erro ao localizar o botão de submissão:", str(e))

time.sleep(2)

try:
    campo_saida = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@name='ecode']"))
    )
    texto_resultado = campo_saida.get_attribute('value')
except Exception as e:
    print("Erro ao localizar o campo de saída:", str(e))
    texto_resultado = ""

with open('code_encrypted.txt', 'w') as arquivo:
    arquivo.write(texto_resultado)

print('Encriptado com sucesso')
driver.quit()