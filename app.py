from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

driver = webdriver.Chrome()
# 1 - navegar até o site
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)
# 2 - digitar o email
email = driver.find_element(By.XPATH,"//input[@id='email']")
sleep(2)
email.send_keys('ederaldo.souza@gmail.com')
# 3 - digitar a senha
senha = driver.find_element(By.XPATH, "//input[@id='senha']")
sleep(2)
senha.send_keys('JavaScriptémelhorquePython')
# 4 - clicar em entrar 
botao_entrar = driver.find_element(By.XPATH, "//button[@id='Entrar']")
sleep(2)
botao_entrar.click()
# 5 - Extrair informações da planilha
empresas = openpyxl.load_workbook('./empresas.xlsx')
pagina_empresas = empresas['dados empresas']
# 6 - clicar em cada campo e preencher com a informação extraíde da planilha
for linha in pagina_empresas.iter_rows(min_row=2,values_only=True):
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_fundacao = linha
    
    driver.find_element(By.ID,'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID,'emailEmpresa').send_keys(email)
    sleep(1)
    driver.find_element(By.ID,'telefoneEmpresa').send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID,'enderecoEmpresa').send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID,'cnpj').send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID,'areaAtuacao').send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID,'numeroFuncionarios').send_keys(quantidade_de_funcionarios)
    sleep(1)
    driver.find_element(By.ID,'dataFundacao').send_keys(data_fundacao)
    sleep(1)

    driver.find_element(By.ID,'Cadastrar').click()
    sleep(3) 
# 7 - repita os passos 5 e 6
