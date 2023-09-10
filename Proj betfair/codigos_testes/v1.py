from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
def pegar_dados(requisição):
    css_dados = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(3) > div > div'
    out = requisição.find(By.CSS_SELECTOR, css_dados).g
    return out


lista1 = []
lista2 = []
dic1 = ()

futebol = webdriver.Chrome()

link = 'https://www.betfair.com/exchange/plus/'
link_home_futebol = 'https://www.betfair.com/exchange/plus/pt/futebol/col%C3%B4mbia-primera-b/boyaca-patriotas-x-real-cartagena-apostas-32507385'

def cssdinamic(numero):
    css = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.\\3' + str(numero)
    return css
def cssdinamic_plus(numero):
    css = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(' + str(numero) +')'
    return css
def cssdinamic_dow(numero):
    css = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(' + str(numero) +') > div > div > div'
    css1 = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent'
    css3 = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div'
    css4 = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper'
    return css1
# def juntar(lista1,lista2):
#     lista1.app

futebol.get(link_home_futebol)
sleep(5)
# pegando quantidade de aba
try:
    quant = futebol.find_elements(By.CSS_SELECTOR,'#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li')
    qt_abas = len(quant)
    qt_abas2 =+ qt_abas-1
    sleep(3)

    # b_aba_text = futebol.find_element(By.CSS_SELECTOR,cssdinamic(qt_abas2)).get_attribute('innerText')
    # ultima = b_aba_text
    # lista1.append(ultima)


    #pegando dados 1


    pegar_dados = futebol.find_element(By.CSS_SELECTOR,cssdinamic_dow(2)).get_attribute('innerText')
    lista1.append(pegar_dados)
    lista2.append(lista1)
    lista1 = []

    # laço abas

    for c in range(1,qt_abas-1):
        b_aba = futebol.find_element(By.CSS_SELECTOR,cssdinamic(c))
        b_aba2 = futebol.find_element(By.CSS_SELECTOR,cssdinamic(c)).get_attribute('innerText')
        print(b_aba2)
        b_aba.click()

        sleep(2)
        #pegando dados
        pegar_dados2 = futebol.find_element(By.CSS_SELECTOR,cssdinamic_dow(c+1)).get_attribute('innerText')
        lista1.append(pegar_dados2)
        lista2.append(lista1)
        lista1 = []
    # Botao aba plus
    try:
        b_abaM = futebol.find_element(By.CSS_SELECTOR,'#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more')
        b_abaM.click()
        sleep(2)
            #quantidade deabas do botao plus

        qt_abas_plus_botao = futebol.find_elements(By.CSS_SELECTOR,'#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li')
        qt_abas_plus = len(qt_abas_plus_botao)
        qt_abas_plus += 1
        print(qt_abas_plus)

        for d in range(1,qt_abas_plus):
            b_aba_plus = futebol.find_element(By.CSS_SELECTOR,cssdinamic_plus(d))
            print(cssdinamic_plus(d))
            b_aba_plus.click()
            sleep(20)
            #pegandodados2
            pegar_dados3 = futebol.find_element(By.CSS_SELECTOR,cssdinamic_dow(d+qt_abas)).get_attribute('innerText')
            lista1.append(pegar_dados3)
            lista2.append(lista1)
            lista1 = []
            #seleciona novbamente
            b_abaM2 = futebol.find_element(By.CSS_SELECTOR,'#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > div')
            b_abaM2.click()
            
            
            sleep(2)

    except:
        b_aba_final = futebol.find_element(By.CSS_SELECTOR,cssdinamic(qt_abas))
        b_aba_final.click()
        sleep(2)
        pegar_dados4 = futebol.find_element(By.CSS_SELECTOR,cssdinamic_dow(qt_abas)).get_attribute('innerText')
        lista1.append(pegar_dados4)
        lista2.append(lista1)
        lista1 = []
except:
    full = futebol.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler')
    full.click()

sleep(2)
print(lista2)
for c in lista2:
    print(c)
    print('=='*30)
# entrando na aba 2

# b_aba2 = futebol.find_element(By.CSS_SELECTOR,'#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.\\31')
# b_aba2.click()
# sleep(1)
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(2)

#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(1)


#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.\31 .active


#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(3)

#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(2)
futebol.quit()
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > div
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(2)
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(3)
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent

#onetrust-accept-btn-handler
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div