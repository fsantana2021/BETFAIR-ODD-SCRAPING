from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

lista = []
futebol = webdriver.Chrome()
link = 'https://www.betfair.com/exchange/plus/'
link_home_futebol = 'https://www.betfair.com/exchange/plus/pt/futebol/primera-division-da-argentina/banfield-x-godoy-cruz-apostas-32492206'

futebol.get(link_home_futebol)
sleep(5)
pegar_dados = futebol.find_element(By.CSS_SELECTOR,'#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent').get_attribute('innerHTML')
lista.append(pegar_dados)
# print(pegar_dados)
futebol.quit()
print(lista)
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(2) > div > div > div > div.column-left > bf-mini-market-container:nth-child(4) > bf-mini-marketview > div > div > bf-marketview-runners-list > div > div > div > table > tbody > tr:nth-child(1)

#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(2) > div > div > div > div.column-left > bf-mini-market-container:nth-child(4) > bf-mini-marketview > div > div > bf-marketview-runners-list > div > div > div > table > tbody > tr:nth-child(2)
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(2) > div > div > div > div.column-left > bf-mini-market-container:nth-child(3) > bf-mini-marketview > div > div > bf-marketview-runners-list > div > div > div > table > tbody > tr:nth-child(2)
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(2) > div > div > div > div.column-right > bf-mini-market-container:nth-child(2) > bf-mini-marketview > div > div > bf-marketview-runners-list > div > div > div > table > tbody > tr:nth-child(9)
#main-wrapper > div > div.scrollable-panes-height-taker > div > ui-view > ui-view > div > div > div.bf-col-xxl-17-24.bf-col-xl-16-24.bf-col-lg-16-24.bf-col-md-15-24.bf-col-sm-14-24.bf-col-14-24.center-column.bfMarketSettingsSpace.bf-module-loading.nested-scrollable-pane-parent > div.scrollable-panes-height-taker.height-taker-helper > div > div:nth-child(2) > div > div > bf-other-markets > div > div > div > bf-tabs > section > div:nth-child(2) > div > div > div > div.column-left > bf-mini-market-container:nth-child(3)