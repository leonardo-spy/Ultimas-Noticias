
import requests
from bs4 import BeautifulSoup

from models.Extra_noticia import Extra_noticia

EXTRA_URL = "https://extra.globo.com/plantao.html"


class Extra():
    def __init__(self):
        pass

    def run(self):
        session = requests.Session()
        response = session.get(EXTRA_URL)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.find("div", {'class': 'content'}).find("section", {'class': 'breaking_news box'}, recursive=False).find("ol", recursive=False).find_all("li", recursive=False)
        for noticia in divs:
            content = noticia.find("a", recursive=False)
            imagem_link = None
            if content:
                body_img = content.find("img", recursive=True)
                if body_img:
                    imagem_link = body_img['src'].strip()
                    
            noticia_base = noticia.find("div", recursive=False)
            if noticia_base:
                body_text = noticia_base.find("a", recursive=False, href=True)
                if not body_text:
                    continue
                link = body_text['href'].strip()
                body_title = body_text.text.strip()

                info = noticia_base.find("div", recursive=False)
                if info:
                    tipo_materia = info.find("a", recursive=False).text.strip()
                    horario = info.find("time", recursive=False)['datetime']
                else:
                    tipo_materia = noticia_base.find("a", recursive=False).text.strip()
                    horario = noticia_base.find("time", recursive=False)['datetime']
                template = Extra_noticia(imagem_link,link,body_title,tipo_materia,horario)
                template.insert()
            else:
                continue