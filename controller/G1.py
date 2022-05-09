
import requests
from bs4 import BeautifulSoup

from models.G1_noticia import G1_noticia

G1_URL = "https://g1.globo.com/ultimas-noticias/"


class G1():
    def __init__(self):
        pass

    def run(self):
        session = requests.Session()
        response = session.get(G1_URL)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.find("div", {'class': 'bastian-page'}).find(
            "div", {'class': '_evg'}, recursive=False).find_all("div", recursive=False)
        for noticia in divs:
            noticia_base = noticia.find("div", recursive=False).find(
                "div", recursive=False).find("div", recursive=False)
            body_title = noticia_base.select('div[class*="feed-post-body-title"]')[0].find(
                "div", recursive=False).find("a", recursive=False, href=True)
            titulo = body_title.text.strip()
            link = body_title['href'].strip()
            body_text = noticia_base.select(
                'div[class*="feed-post-body-resumo"]')[0].text.strip()
            body_picture = noticia_base.select('div[class*="feed-media-wrapper"]')
            if body_picture:
                body_img = body_picture[0].find("a", recursive=False).find("div", recursive=False).find("picture", recursive=False).find("img", recursive=True)
                imagem_link = body_img['src'].strip()
            else:
                imagem_link = None            
            footer = noticia_base.select('div[class*="feed-post-metadata"]')[0]
            horario = footer.find(
                "span", {'class': 'feed-post-datetime'}, recursive=False).text.strip()
            local = footer.find(
                "span", {'class': 'feed-post-metadata-section'}, recursive=False).text.strip()
            template = G1_noticia(titulo, link, body_text,
                                  imagem_link, horario, local)
            template.insert()
