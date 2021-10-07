from django.urls import resolve
from django.test import TestCase
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
