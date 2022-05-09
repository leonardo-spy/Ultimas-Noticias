from threading import Thread
from faunadb import query as q

from db.fauna import get_client


class Estadao_noticia:
    def __init__(self, link, titulo, body_text, credito, data, imagem_link):
        self.link = link
        self.titulo = titulo
        self.body_text = body_text
        self.credito = credito
        self.data = data
        self.imagem_link = imagem_link    

    def upload(self):
        client = get_client()

        exist = client.query(q.let({'ref': q.match(q.index("noticias_Estadao_by_link"), self.link)},
                                   q.if_(
            q.exists(q.var('ref')),
            q.get(q.var('ref')),
            False
        )
        ))

        if exist and exist['data'] != {**self.formatting(keys=True)}:
            result = client.query(q.update(q.ref(q.collection("estadao"), exist['ref'].value['id']), {
                                  "data": {**self.formatting(keys=True)}}))
        elif not exist:
            result = client.query(q.create(q.collection(
                "estadao"), {"data": {**self.formatting(keys=True)}}))

    def insert(self):
        #Thread(target=self.upload).start()
        self.upload()

    def formatting(self, keys=False):
        if keys:
            if self.imagem_link and self.body_text and self.credito:
                return {'imagem_link': self.imagem_link,'link': self.link, 'titulo':self.titulo,'body_text': self.body_text, 'credito': self.credito, 'data': self.data}
            if self.imagem_link and self.body_text:
                return {'imagem_link': self.imagem_link,'link': self.link, 'titulo':self.titulo,'body_text': self.body_text, 'data': self.data}
            elif self.imagem_link and self.credito:
                return {'imagem_link': self.imagem_link,'link': self.link, 'titulo':self.titulo, 'credito': self.credito, 'data': self.data}
            elif self.body_text and self.credito:
                return {'link': self.link, 'titulo':self.titulo,'body_text': self.body_text, 'credito': self.credito, 'data': self.data}
            elif self.imagem_link:
                return {'imagem_link': self.imagem_link,'link': self.link, 'titulo':self.titulo,  'data': self.data}
            elif self.body_text:
                return {'link': self.link, 'titulo':self.titulo,'body_text': self.body_text, 'data': self.data}
            elif self.credito:
                return {'link': self.link, 'titulo':self.titulo,'credito': self.credito, 'data': self.data}
            else:
                return {'link': self.link, 'titulo':self.titulo, 'data': self.data}
        else:
            return {self.link,self.titulo,self.body_text,self.credito,self.data,self.imagem_link}
