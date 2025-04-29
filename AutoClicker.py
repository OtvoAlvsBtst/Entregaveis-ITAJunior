import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def n_cookies(drive):
    num=(drive.find_element(By.ID,"cookies").text.split()[0])
    n=num.split(",")
    x=''
    for m in n:
        x=x + m
    return int (x)

cookies=0
cursores=0
preco0=15
vovos=0
preco1=100
preco2=1100
upgrade0=False
upgrade1=False
upgrade2=False
navegador=webdriver.Firefox()
navegador.get("https://orteil.dashnet.org/cookieclicker/")
navegador.fullscreen_window()
try:
    lingua=WebDriverWait(navegador,10).until(
        EC.presence_of_element_located((By.ID,"langSelect-EN"))
    )
    lingua.click()

except:
    navegador.quit()
time.sleep(0.3)
nome=navegador.find_element(By.ID,"bakeryName")
nome.click()
time.sleep(0.3)
nome=navegador.find_element(By.ID,"bakeryNameInput")
nome.send_keys("Cookies do Balela")
nome=navegador.find_element(By.ID,"promptOption0")
nome.click()
navegador.find_element(By.ID,"statsButton").click()
clique=WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "bigCookie")))
while True:
    clique.click()
    cookies=n_cookies(navegador)
    if cookies>115 and upgrade0==False:
        compra=navegador.find_element(By.ID, "product0")
        compra.click()
        preco0*=1.15
        cursores+=1
        compra=navegador.find_element(By.ID, "upgrade0")
        compra.click()
        upgrade0=True
    if cookies>500 and upgrade1==False:
        compra=navegador.find_element(By.ID, "upgrade0")
        compra.click()
        upgrade1=True
    if upgrade1==True:
        if cookies>preco2:
            compra=navegador.find_element(By.ID, "product2")
            compra.click()
            preco2*=1.15
        elif cookies>1000 and vovos==6:
            compra=navegador.find_element(By.ID, "upgrade0")
            compra.click()
            vovos+=1
        elif cookies>preco1 and vovos!=6 and vovos<11:
            compra=navegador.find_element(By.ID, "product1")
            compra.click()
            preco1*=1.15
            vovos+=1
        elif cookies>preco0 and cursores <10:
            compra=navegador.find_element(By.ID, "product0")
            compra.click()
            preco0*=1.15
            cursores+=1