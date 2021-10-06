'''Esse é o nosso primeiro FT (Functional Test, ou Teste Funcional);
Por enquanto, é suficiente garantir que compreendemos o que esse teste faz:
• inicia um “webdriver” Selenium para apresentar uma verdadeira janela do 
navegador Firefox;
• usa essa janela para abrir uma página web que esperamos que vá ser
servida pelo microcomputador local;
• verifica (fazendo uma asserção de teste) se a página tem a palavra
“Django” no título.'''

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Jorge ouviu falar de uma nova aplicação online interessante para
        # lista de tarefas. Ele decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ele percebe que o título da página e o cabeçalho mencionam
        # listas de tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

    # Ele é convidado a inserir um item de tarefa imediatamente

    # Ele digita "Buy peacock feathers" (Comprar penas de pavão) em uma caixa
    # de texto (o hobby de Jorge é fazer iscas para pesca com fly)

    # Quando ela tecla enter, a página é atualizada, e agora a página lista
    # "1: Buy peacock feathers" como um item em uma lista de tarefas

    # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item.
    # Ele insere "Use peacock feathers to make a fly"(Usar penas de pavão
    # para fazer uum fly - Jorge é bem metódico)

    # A página é atualizada novamente e agora mostra os dois itens em sua lista

    # Jorge se pergunta se o site lembrará de sua lista.
    # Então ele nota que o site gerou um URL único para ele
    # -- há um pequeno texto explicativo para isso.

    # Ele acessa esse URL - sua lista de tarefas continua lá

    # Satisfeito, ele volta a dormir


if __name__ == '__main__':
    unittest.main(warnings='ignore')
