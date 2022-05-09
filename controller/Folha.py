
import requests
from bs4 import BeautifulSoup

from models.Folha_noticia import Folha_noticia

FOLHA_URL = "https://www.folha.uol.com.br/ultimas-noticias/"


class Folha():
    def __init__(self):
        pass

    def run(self):
        session = requests.Session()
        response = session.get(FOLHA_URL)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
        page = soup.find("div", {'class': 'page'})
        body_noticias = page.find_all("div", {'class': 'block'}, recursive=False)
        if len(body_noticias)>1:
            noticia_main_base = body_noticias[0].find("div", {'class': 'container'}, recursive=False).select('div[class*="flex"]')[0].find("div", {'class': 'flex-cell'}, recursive=False).find("div", {'class': 'row'}, recursive=False).select('div[class*="col"]')[0].find("ol", recursive=False).find("li", recursive=False)
            body_main = noticia_main_base.find_all("div", recursive=False)
            if len(body_main)>1:
                body_main_img = body_main[0].find("div", recursive=False).find("a", recursive=False).find("img", recursive=True)
                imagem_link = body_main_img['data-src'].strip()

                credito = body_main[1].find("div", recursive=False).find("h3", recursive=False).text.strip()
                noticia_main_base = body_main[1].find("a", recursive=False, href=True)
                link = noticia_main_base['href'].strip()
                titulo = noticia_main_base.find("h2", recursive=False).text.strip()
                body_text = noticia_main_base.find("p", recursive=False).text.strip()
                data= noticia_main_base.find("time", recursive=False)['datetime'].strip()
            else:
                imagem_link = None
                credito = body_main[0].find("div", recursive=False).find("h3", recursive=False).text.strip()
                noticia_main_base = body_main[0].find("a", recursive=False, href=True)
                link = noticia_main_base['href'].strip()
                titulo = noticia_main_base.find("h2", recursive=False).text.strip()
                body_text = noticia_main_base.find("p", recursive=False).text.strip()
                data= noticia_main_base.find("time", recursive=False)['datetime'].strip()
            template = Folha_noticia(imagem_link,credito,link,titulo,body_text,data)
            template.insert()

        if len(body_noticias)>1:
            noticias_loop = body_noticias[1]
        else:
            noticias_loop = body_noticias[0]
        noticias_base = noticias_loop.find("div", {'class': 'container'}, recursive=False).select('div[class*="flex"]')[0].find("div", {'class': 'flex-cell'}, recursive=False).find("div", {'class': 'row'}, recursive=False).select('div[class*="col"]')[0].find("div", {'class': 'c-newslist'}, recursive=False).find("ol", recursive=False).find_all("li", recursive=False)
        
        for noticia in noticias_base:
            if  noticia.find("div", {'class': 'OUTBRAIN'}, recursive=False):
                continue
            body = noticia.find_all("div", recursive=False)
            if len(body)>1:
                body_img = body[0].find("div", recursive=False).find("a", recursive=False).find("img", recursive=True)
                imagem_link = body_img['data-src'].strip()
                noticia_div = body[1].find_all("div", recursive=False)
                credito = noticia_div[0].find("h3", recursive=False).text.strip()
                noticia_base = noticia_div[1].find("a", recursive=False, href=True)
                link = noticia_base['href'].strip()
                titulo = noticia_base.find("h2", recursive=False).text.strip()
                body_text = noticia_base.find("p", recursive=False).text.strip()
                data= noticia_base.find("time", recursive=False)['datetime'].strip()
            else:
                imagem_link = None
                credito = body[0].find("div", recursive=False).find("h3", recursive=False).text.strip()
                noticia_base = body[0].find("a", recursive=False, href=True)
                link = noticia_base['href'].strip()
                titulo = noticia_base.find("h2", recursive=False).text.strip()
                body_text = noticia_base.find("p", recursive=False).text.strip()
                data= noticia_base.find("time", recursive=False)['datetime'].strip()
            template = Folha_noticia(imagem_link,credito,link,titulo,body_text,data)
            template.insert()