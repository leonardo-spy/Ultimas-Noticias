from threading import Thread
from faunadb import query as q

from db.fauna import get_client


class G1_noticia:
    def __init__(self, titulo, link, body_text, imagem_link, horario, local):
        self.titulo = titulo
        self.link = link
        self.body_text = body_text
        self.imagem_link = imagem_link
        self.horario = horario
        self.local = local

    def upload(self):
        client = get_client()

        exist = client.query(q.let({'ref': q.match(q.index("noticias_G1_by_link"), self.link)},
                                   q.if_(
            q.exists(q.var('ref')),
            q.get(q.var('ref')),
            False
        )
        ))

        if exist and exist['data'] != {**self.formatting(keys=True)}:
            result = client.query(q.update(q.ref(q.collection("g1"), exist['ref'].value['id']), {
                                  "data": {**self.formatting(keys=True)}}))
        elif not exist:
            result = client.query(q.create(q.collection(
                "g1"), {"data": {**self.formatting(keys=True)}}))

    def insert(self):
        Thread(target=self.upload).start()

    def formatting(self, keys=False):
        if keys:
            if self.imagem_link:
                return {'titulo': self.titulo, 'link': self.link, 'body_text': self.body_text, 'imagem_link': self.imagem_link, 'horario': self.horario, 'local': self.local}
            else:
                return {'titulo': self.titulo, 'link': self.link, 'body_text': self.body_text, 'horario': self.horario, 'local': self.local}
        else:
            return {self.titulo, self.link, self.body_text, self.imagem_link, self.horario, self.local}
