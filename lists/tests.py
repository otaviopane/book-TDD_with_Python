from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    """Criamos um objeto HttpRequest, que é o que o Django verá quando o
    navegador de um usuário requisitar uma página."""
    """Ele é passado para a nossa view home_page, que nos dará uma resposta.
    Você não ficará surpreso ao saber que esse objeto é uma instância de uma
    classe chamada HttpResponse."""
    """Em seguida extraímos .content da resposta. Esses são os bytes brutos, isto
    é, os uns e zeros que seriam enviados para o navegador do usuário.
    Chamamos .decode() para convertê-los na string HTML enviada ao
    usuário."""
    """Queremos que ela comece com uma tag <html> que será fechada no final."""
    """Além disso, queremos uma tag <title> em algum lugar no meio, contendo
    as palavras “To-Do lists” – pois é isso que especificamos em nosso teste
    funcional."""
