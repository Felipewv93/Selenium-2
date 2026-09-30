from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Parte 1: Configuração inicial, Headless e Segurança de Rede
options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


# Parte 2: Orquestração de Abas
print("Processo de automação iniciado...\n")
driver.get("https://the-internet.herokuapp.com/dropdown")
print(f'Título da Aba 0: {driver.title}')

driver.execute_script("window.open('https://the-internet.herokuapp.com/dynamic_loading/2')")

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

driver._switch_to.window(driver.window_handles[1])
print(f'Título da Aba 1: {driver.title}')

driver.execute_script("window.open('https://pt.wikipedia.org')")
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))

driver._switch_to.window(driver.window_handles[2])
print(f'Título da Aba 2: {driver.title}')


#Parte 3: Interação com Dropdowns
driver._switch_to.window(driver.window_handles[0])

dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_visible_text("Option 1")
opcao = dropdown.first_selected_option
print(f'\nOpção selecionada no menu dropdown: {opcao.get_attribute("value")}')


# Parte 4: Sincronização Dinâmica
driver._switch_to.window(driver.window_handles[1])

botao = driver.find_element(By.TAG_NAME, "button")
botao.click()

texto = WebDriverWait(driver, 15).until(EC.visibility_of(driver.find_element(By.ID, "finish")))
print(f'\nTexto visível após clique no botão "Start": {texto.text}')


# Parte 5: Extração de Dados e Evidências
driver._switch_to.window(driver.window_handles[2])

pesquisa = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(driver.find_element(By.ID, "searchInput")))
pesquisa.click()


pesquisa = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(driver.find_element(By.ID, "searchInput")))
pesquisa.send_keys("Automação")

menu = driver.find_element(By.TAG_NAME, "input")
menu.click()

link = driver.find_element(By.LINK_TEXT, "Conteúdo destacado")

texto_link = link.text
print(f'\nTexto do link escolhido no menu da Wikipédia: {texto_link}')

caminho_link = link.get_attribute("href")
print(f'Caminho do link: {caminho_link}')

driver.save_screenshot("assets/evidencia_wiki.png")
print("Print da página salvo na pasta assets")


# Parte 6: Encerramento
print("\nAutomação concluída com sucesso! Processo encerrado.")
driver.quit()
