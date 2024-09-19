from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, collections

driver = webdriver.Edge()

driver.get("https://www.kabum.com.br/")

wait = WebDriverWait(driver, 10)
search_form = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

# Encontra o campo de pesquisa e faz a busca
search_input = search_form.find_element(By.TAG_NAME, 'input')
search_input.send_keys('notebooks')
search_input.send_keys(Keys.ENTER)

time.sleep(5)
# == PAG 1 ========================================================================================

# Seleciona o primeiro filtro (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a opcao 0 do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[0].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks pagina inicial 1
nb_ini_1 = []

for i in range(len(h3)):
    nb_ini_1.append(h3[i].text)
# =================================================================================================

# Seleciona o filtro (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a quarta opcao do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[3].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks mais avaliados 1
nb_ava_1 = []

for i in range(len(h3)):
    nb_ava_1.append(h3[i].text)

# =================================================================================================

# Seleciona o filtro denovo (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a opcao 2 do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[2].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks mais baratos 1
nb_bar_1 = []

for i in range(len(h3)):
    nb_bar_1.append(h3[i].text)
# == SCROLL ========================================================================================

# Scrolla para baixo ate achar o botao para trocar de pagina do site
page_selector = driver.find_element(By.XPATH, '//ul[@class="pagination"]')
page_number = page_selector.find_elements(By.TAG_NAME, 'li')

scroll_to = driver.find_element(By.CLASS_NAME, 'pagination')
driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", scroll_to)

time.sleep(2)
page_number[2].click()
time.sleep(5)

# Scrolla para cima ate achar o filtro dos notebooks
scroll_to = driver.find_element(By.CLASS_NAME, 'cUHvqY')
driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", scroll_to)

time.sleep(2)
# == PAG 2 ========================================================================================

# Seleciona o primeiro filtro (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a opcao 0 do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[0].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks pagina inicial 2
nb_ini_2 = []

for i in range(len(h3)):
    nb_ini_2.append(h3[i].text)
# =================================================================================================

# Seleciona o filtro (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a quarta opcao do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[3].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks mais avaliados 2
nb_ava_2 = []

for i in range(len(h3)):
    nb_ava_2.append(h3[i].text)

# =================================================================================================

# Seleciona o filtro denovo (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a opcao 2 do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[2].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks mais baratos 2
nb_bar_2 = []

for i in range(len(h3)):
    nb_bar_2.append(h3[i].text)

# == SCROLL ========================================================================================

# Scrolla para baixo ate achar o botao para trocar de pagina do site
page_selector = driver.find_element(By.XPATH, '//ul[@class="pagination"]')
page_number = page_selector.find_elements(By.TAG_NAME, 'li')

scroll_to = driver.find_element(By.CLASS_NAME, 'pagination')
driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", scroll_to)

time.sleep(2)
page_number[3].click()
time.sleep(5)
# =================================================================================================

# Seleciona o primeiro filtro (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a opcao 0 do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[0].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks pagina inicial 3
nb_ini_3 = []

for i in range(len(h3)):
    nb_ini_3.append(h3[i].text)

# =================================================================================================

# Scrolla para baixo ate achar o filtro dos notebooks
scroll_to = driver.find_element(By.CLASS_NAME, 'cUHvqY')
driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", scroll_to)

time.sleep(2)

# Seleciona o filtro (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a quarta opcao do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[3].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks mais avaliados 3
nb_ava_3 = []

for i in range(len(h3)):
    nb_ava_3.append(h3[i].text)

# =================================================================================================

# Seleciona o filtro denovo (ajuste as classes caso necessário)
select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
select.click()
time.sleep(2)
# seleciona a opcao 2 do filtro
options = select.find_elements(By.TAG_NAME, 'option')
options[2].click()

# Aguarda até que os resultados estejam visíveis
main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
h3 = main_class.find_elements(By.TAG_NAME, 'h3')

### CRIA A LISTA nootebooks mais baratos 3
nb_bar_3 = []

for i in range(len(h3)):
    nb_bar_3.append(h3[i].text)

# =================================================================================================

# Conta os 5 notebooks que mais aparecem
conjunto_nb = nb_ini_1 + nb_ava_1 + nb_bar_1 + nb_ini_2 + nb_ava_2 + nb_bar_2 + nb_ini_3 + nb_ava_3 + nb_bar_3

notebook_counts = collections.Counter(conjunto_nb)
top5 = notebook_counts.most_common(5)

print("\n == TOP 5 notebooks =========================================================================== \n")
for notebook, count in top5:
    print(f"{notebook}: \n{count} vezes")
print("\n == TOP 5 notebooks =========================================================================== \n")

time.sleep(10)
driver.quit()
