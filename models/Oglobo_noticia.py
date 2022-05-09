from threading import Thread
from faunadb import query as q

from db.fauna import get_client


class Oglobo_noticia:
    def __init__(self, imagem_link,tipo_materia,body_text,link):
        self.imagem_link = imagem_link
        self.tipo_materia = tipo_materia
        self.body_text = body_text
        self.link = link

    def upload(self):
        client = get_client()

        exist = client.query(q.let({'ref': q.match(q.index("noticias_Oglobo_by_link"), self.link)},
                                   q.if_(
            q.exists(q.var('ref')),
            q.get(q.var('ref')),
            False
        )
        ))

        if exist and exist['data'] != {**self.formatting(keys=True)}:
            result = client.query(q.update(q.ref(q.collection("oglobo"), exist['ref'].value['id']), {
                                  "data": {**self.formatting(keys=True)}}))
        elif not exist:
            result = client.query(q.create(q.collection(
                "oglobo"), {"data": {**self.formatting(keys=True)}}))

    def insert(self):
        #Thread(target=self.upload).start()
        self.upload()

    def formatting(self, keys=False):
        if keys:
            if self.imagem_link:
                return {'imagem_link': self.imagem_link, 'tipo_materia': self.tipo_materia, 'body_text': self.body_text,'link': self.link}
            else:
                return {'tipo_materia': self.tipo_materia, 'body_text': self.body_text,'link': self.link}
        else:
            return {self.imagem_link,self.tipo_materia,self.body_text,self.link}
