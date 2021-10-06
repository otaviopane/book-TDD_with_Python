'''Esse é o nosso primeiro FT (Functional Test, ou Teste Funcional);
Por enquanto, é suficiente garantir que compreendemos o que esse teste faz:
• inicia um “webdriver” Selenium para apresentar uma verdadeira janela do 
navegador Firefox;
• usa essa janela para abrir uma página web que esperamos que vá ser
servida pelo microcomputador local;
• verifica (fazendo uma asserção de teste) se a página tem a palavra
“Django” no título.'''

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
