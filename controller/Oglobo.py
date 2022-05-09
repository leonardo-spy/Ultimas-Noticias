
import requests
from bs4 import BeautifulSoup

from models.Oglobo_noticia import Oglobo_noticia

OGLOBO_URL = "https://oglobo.globo.com/ultimas-noticias/"


class Oglobo():
    def __init__(self):
        pass

    def run(self):
        session = requests.Session()
        response = session.get(OGLOBO_URL)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.find("div", {'class': 'block__container'}).find_all("div", {'class': 'block__module'}, recursive=False)
        for bloco in divs:
            bloco_painel = bloco.find_all("div", {'class': 'block__pane'}, recursive=False)
            for painel in bloco_painel:
                Extra_banner = painel.find("div", {'class': 'block__space'}, recursive=False)
                if Extra_banner:
                    content = Extra_banner.find("teaser-ultimas", recursive=False).find("div", recursive=False)
                    body_figure = content.find("figure", recursive=False)
                    if body_figure:
                        body_img = body_figure.find("img", recursive=True)
                        if body_img:
                            imagem_link = body_img['src'].strip()
                        else:
                            imagem_link = None   
                    else:
                        imagem_link = None                                
                    tipo_materia = content.find("div", recursive=False).text.strip()
                    body_title = content.find("h1", recursive=False).find("a", recursive=False, href=True)
                    body_text = body_title.text.strip()
                    link = body_title['href'].strip()

                    template = Oglobo_noticia(imagem_link,tipo_materia,body_text,link)
                    template.insert()

                sub_blocos = painel.find_all("div", {'class': 'block__submodule'}, recursive=False)
                if sub_blocos:
                    for sub_bloco in sub_blocos:
                        sub_paineis = sub_bloco.find_all("div", {'class': 'block__subpane'}, recursive=False)
                        for sub_painel in sub_paineis:
                            body = sub_painel.find("div", recursive=False)
                            if body.find("div", {'class': 'block__advertising block__advertising-module'}, recursive=False):
                                continue#publicidade
                            else:
                                content = body.find("teaser-ultimas", recursive=False).find("div", recursive=False)
                                body_figure = content.find("figure", recursive=False)
                                if body_figure:
                                    body_img = body_figure.find("img", recursive=True)
                                    imagem_link = body_img['data-src'].strip()
                                else:
                                    imagem_link = None                                
                                tipo_materia = content.find("div", recursive=False).text.strip()
                                body_title = content.find("h1", recursive=False).find("a", recursive=False, href=True)
                                body_text = body_title.text.strip()
                                link = body_title['href'].strip()

                                template = Oglobo_noticia(imagem_link, tipo_materia,body_text,link)
                                template.insert()
