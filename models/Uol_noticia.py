from threading import Thread
from faunadb import query as q

from db.fauna import get_client


class Uol_noticia:
    def __init__(self, link, imagem_link, tipo_materia, body_text, data):
        self.link = link
        self.imagem_link = imagem_link
        self.tipo_materia = tipo_materia
        self.body_text = body_text
        self.data = data

    def upload(self):
        client = get_client()

        exist = client.query(q.let({'ref': q.match(q.index("noticias_Uol_by_link"), self.link)},
                                   q.if_(
            q.exists(q.var('ref')),
            q.get(q.var('ref')),
            False
        )
        ))

        if exist and exist['data'] != {**self.formatting(keys=True)}:
            result = client.query(q.update(q.ref(q.collection("uol"), exist['ref'].value['id']), {
                                  "data": {**self.formatting(keys=True)}}))
        elif not exist:
            result = client.query(q.create(q.collection(
                "uol"), {"data": {**self.formatting(keys=True)}}))

    def insert(self):
        Thread(target=self.upload).start()

    def formatting(self, keys=False):
        if keys:
            if self.imagem_link:
                return {'link' : self.link, 'imagem_link' : self.imagem_link, 'tipo_materia' : self.tipo_materia, 'body_text' : self.body_text, 'data' : self.data}
            else:
                return {'link' : self.link, 'tipo_materia' : self.tipo_materia, 'body_text' : self.body_text, 'data' : self.data}
        else:
            return {self.link, self.imagem_link, self.tipo_materia, self.body_text, self.data}
