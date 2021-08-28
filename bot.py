from selenium import webdriver
from random import choice
from selenium.webdriver.common.keys import Keys
from time import sleep
import string

def criarContas(vezes,palavraChave): 
    navegador = webdriver.Chrome()
    arquivo = open('contas.txt','w') 
    i=0
    while i<vezes:
        nickname = palavraChave + str(i)
        email = nickname + '@'+'gmail.com'
        senha = gerarSenha()

        navegador.get('https://signup.br.leagueoflegends.com/pt/signup/index')
        sleep(5)
        navegador.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/form/div[1]/input').send_keys(email)
        navegador.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/form/div[2]/button').send_keys(Keys.ENTER)
        sleep(5)
        navegador.find_element_by_name('dob-day').send_keys('23')
        navegador.find_element_by_name('dob-month').send_keys('fev')
        navegador.find_element_by_name('dob-year').send_keys('2001')
        navegador.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/form/div[2]/button').send_keys(Keys.ENTER)
        sleep(5)
        navegador.find_element_by_name('username').send_keys(nickname)
        navegador.find_element_by_name('password').send_keys(senha)
        navegador.find_element_by_name('confirm_password').send_keys(senha)
        navegador.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/form/div[4]/label/div').click()
        navegador.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/form/div[6]/button').send_keys(Keys.ENTER)
        sleep(20)
        arquivo.write("===============================\n")
        arquivo.write("Nickname : " + nickname +'\n')
        arquivo.write("Senha : " + senha +'\n')
        arquivo.write("Email : " + email +'\n')
        arquivo.write("===============================\n")
        i = i + 1
    arquivo.close    
    
    
def gerarSenha():
    tamanho = 8
    valores = string.ascii_lowercase + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    return senha

