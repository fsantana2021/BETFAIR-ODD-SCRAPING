from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import pytz



def extract_table_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    table_data = []

    # Encontra todas as linhas da tabela (tr)
    rows = soup.find_all('tr')

    for row in rows:
        row_data = []
        # Encontra todas as colunas da linha (td)
        cols = row.find_all(['th', 'td'])
        for col in cols:
            # Adiciona o texto de cada coluna à lista de dados da linha
            row_data.append(col.get_text(strip=True))
        table_data.append(row_data)

    return table_data
def extract_ng_bind_value(html):
    # Analisa o HTML usando BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # Encontra o elemento que contém o atributo "ng-bind" com o valor desejado
    element = soup.find(attrs={"ng-bind": "ctrl.data.marketNameSettings.label"})
    return element.text

def captardados(chamda):
    mercados  = chamda.find_elements(By.CSS_SELECTOR,'bf-mini-marketview > div')
    # tab_geral = pd.DataFrame()
    lista_dataframe = []
    for mercados in mercados:
        
        table_data = extract_table_data(mercados.get_attribute('innerHTML'))
        df = pd.DataFrame(table_data)
        
        mercad = extract_ng_bind_value(mercados.get_attribute('innerHTML'))
        df['mercado'] = mercad
        
        delimitador = "$"
        
        df[df.columns[1]] = df[df.columns[1]].str.replace("R","",)
        df[df.columns[1]] = df[df.columns[1]].str.split(delimitador)

        df[df.columns[2]] = df[df.columns[2]].str.replace("R","",)
        df[df.columns[2]] = df[df.columns[2]].str.split(delimitador)

        #hora

        hora_data_local = datetime.now()
        fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
        hora_data_brasilia = hora_data_local.astimezone(fuso_horario_brasilia)
        df['HORA'] = str(hora_data_brasilia)
        # tab_geral = pd.concat(df, axis=0)
        lista_dataframe.append(df)

        # # .str.split(delimitador)
        # # print(df)
        # print("*="*30)


    data_frame_juntado  = pd.concat(lista_dataframe, axis=0)    
    # print(data_frame_juntado)
    return(data_frame_juntado)

def captardados_main(chamda):
    mercados  = chamda.find_elements(By.CSS_SELECTOR,'bf-main-marketview > div')
    # tab_geral = pd.DataFrame()
    lista_dataframe = []
    for mercados in mercados:
        
        table_data = extract_table_data(mercados.get_attribute('innerHTML'))
        df = pd.DataFrame(table_data)

        df[df.columns[1]] = df[df.columns[3]]
        
        df[df.columns[2]] = df[df.columns[4]]

        # df = df.drop(df[df.columns[5]])
        
        # mercad = extract_ng_bind_value(mercados.get_attribute('innerHTML'))
        df['mercado'] = "Mercado final"
        
        delimitador = "$"
        
        df[df.columns[1]] = df[df.columns[1]].str.replace("R","",)
        df[df.columns[1]] = df[df.columns[1]].str.split(delimitador)

        df[df.columns[2]] = df[df.columns[2]].str.replace("R","",)
        df[df.columns[2]] = df[df.columns[2]].str.split(delimitador)

        #hora

        hora_data_local = datetime.now()
        fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
        hora_data_brasilia = hora_data_local.astimezone(fuso_horario_brasilia)
        df['HORA'] = str(hora_data_brasilia)
        # tab_geral = pd.concat(df, axis=0)
        lista_dataframe.append(df)

        # # .str.split(delimitador)
        # # print(df)
        # print("*="*30)


    data_frame_juntado  = pd.concat(lista_dataframe, axis=0)    
    # print(data_frame_juntado)
    return(data_frame_juntado)


def quanti(chamda,css,css2):
    try:
        try:
            pegar_dados = chamda.find_elements(By.CSS_SELECTOR,css)
            um = len(pegar_dados)
        except:
            pegar_dados = chamda.find_elements(By.CSS_SELECTOR,css2)
            um = len(pegar_dados)
            pegar_dados.click()
        return um
    except:
        aceitar(chamda)
        try:
            pegar_dados = chamda.find_elements(By.CSS_SELECTOR,css)
            um = len(pegar_dados)
        except:
            pegar_dados = chamda.find_elements(By.CSS_SELECTOR,css2)
            um = len(pegar_dados)
            pegar_dados.click()
        return um


def texto(chamada,css):
    pegar_dados = chamada.find_element(By.CSS_SELECTOR,css).get_attribute('innerText')
    um = pegar_dados
    return um

def htmll(chamada,css):   
    pegar_dados = chamada.find_element(By.CSS_SELECTOR,css).get_attribute('innerHTML')
    um = pegar_dados
    return um

def botao(chamada,css,css2):   
    try:
        try:
            pegar_dados = chamada.find_element(By.CSS_SELECTOR,css)
            pegar_dados.click()
            sleep(2)
        except:
            pegar_dados = chamada.find_element(By.CSS_SELECTOR,css2)
            pegar_dados.click()
            sleep(2)
    except:
        aceitar(chamada)
        try:
            pegar_dados = chamada.find_element(By.CSS_SELECTOR,css)
            pegar_dados.click()
            sleep(2)
        except:
            pegar_dados = chamada.find_element(By.CSS_SELECTOR,css2)
            pegar_dados.click()
            sleep(2)

def cssdinamic_abas234(num):
    css_abas = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.\\3' + str(num)
    return css_abas
def cssdinamic_abasfiais(num):
    css_abas  = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(' + str(num) + ')'
    return css_abas 
def cssdinamic_mercado(num):
    css = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(' + str(num) + ') > div > div > div > div >'
    return css
def aceitar(chamada):
    css = '#onetrust-accept-btn-handler'
    try:
        elemento = chamada.find_element(By.CSS_SELECTOR,css)
        elemento.click()
    except:
        ...

def minute(chamda):
    css = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div:nth-child(1) > div > bf-sports-header > div > div > div > ng-include > div.bf-col-19-24.inplay > p'
    css2 = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div:nth-child(1) > div > bf-sports-header > div > div > div > ng-include > div.bf-col-19-24.inplay > ng-include'
    try:
        minute = chamda.find_element(By.CSS_SELECTOR,css).get_attribute('innerText')
        minute2 = chamda.find_element(By.CSS_SELECTOR,css2).get_attribute('innerText')
    except:
        minute = 'Jogo off'
        minute2 = 'Jogo off'

    return minute,minute2



css_mercados = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(2) > div > div > div'   
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(3) > div > div > div
css_biscoito = '#onetrust-accept-btn-handler'
css_abas = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li'
css_aba_principal = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.\\30 .active'
css_aba_principal_active = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.\\30'
css_bota_abri_abaplus = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more > div'
css_principal = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.\30 .active'
css_aba_more_len = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li'
css_aba_more_len2 = '#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > ul > li.tab-container.more.active > ul > li:nth-child(1)'


lista_fullabas = []

futebol = webdriver.Chrome()

link_home_futebol = 'https://www.betfair.com/exchange/plus/pt/futebol/brasileiro-s%C3%A9rie-a/corinthians-x-vasco-da-gama-apostas-32498586'
futebol.get(link_home_futebol)
sleep(5)

# quantidade de abas

qt_abas = quanti(futebol,css_abas,css_abas)
print(qt_abas)


# selecionar aba 1

botao(futebol,css_aba_principal,css_aba_principal_active)
# mercados = quanti(futebol,'bf-mini-marketview','bf-mini-marketview')

lista_fullabas.append(captardados(futebol))
lista_fullabas.append(captardados_main(futebol))


# selecionar aba 2 e 3
# try:
#     for c in range(1,(qt_abas-1)):
        
#         botao(futebol,cssdinamic_abas234(c),cssdinamic_abas234(c))
#         lista_fullabas.append(captardados(futebol))
#         #aba more
#     botao(futebol,css_bota_abri_abaplus,css_bota_abri_abaplus)
#     a = quanti(futebol,css_aba_more_len,css_aba_more_len)
#     print(a)
#     for t in range(1,((a)+1)):
        
#         try:
#             botao(futebol,cssdinamic_abasfiais(t),cssdinamic_abasfiais(t))
#             lista_fullabas.append(captardados(futebol))
#             botao(futebol,css_bota_abri_abaplus,css_bota_abri_abaplus)
#         except:
#             print('erro')




#seleciona o 4 se nao tiver botao more
# except:
    
#     botao(futebol,cssdinamic_abas234(qt_abas),cssdinamic_abas234(qt_abas))
#     lista_fullabas.append(captardados(futebol))



#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div.bf-row.main-mv-container > div > bf-main-market > bf-main-marketview > div






local2 = 'G:/Meu Drive/PROGRAMAÇÃO/pyCFB/betfair/excel32.xlsx' 

dados = minute(futebol)



futebol.quit()

planilha_final = pd.concat(lista_fullabas, axis=0)
planilha_final = planilha_final.drop(planilha_final.columns[8],axis=1)
planilha_final = planilha_final.drop(planilha_final.columns[7],axis=1)
planilha_final = planilha_final.drop(planilha_final.columns[6],axis=1)
planilha_final = planilha_final.drop(planilha_final.columns[5],axis=1)
planilha_final['minute'] = dados[0]
planilha_final['minute2'] = dados[1]
print(dados)
print(planilha_final)
# planilha_final.to_excel(local2,index=0)

#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div.bf-row.main-mv-container > div > bf-main-market > bf-main-marketview > div > div.main-mv-runners-list-wrapper