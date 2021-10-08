from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    """resolve é a função que Django utiliza internamente para resolver URLs e
    descobrir para qual função de view eles devem ser mapeados. Estamos
    verificando se resolve, quando é chamado com “/”, que é a raiz do site,
    encontra uma função chamada home_page."""
    """ Que função é essa? É a função de view que escreveremos a seguir, a
    qual, na verdade, devolverá o HTML que queremos. Com base no import,
    podemos ver que estamos planejando armazená-la em lists/views.py."""

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

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
