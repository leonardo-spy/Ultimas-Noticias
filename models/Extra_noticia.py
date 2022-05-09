from threading import Thread
from faunadb import query as q

from db.fauna import get_client


class Extra_noticia:
    def __init__(self, imagem_link,link,body_title,tipo_materia,horario):
        self.imagem_link = imagem_link
        self.link = link
        self.body_title = body_title
        self.tipo_materia = tipo_materia
        self.horario = horario        

    def upload(self):
        client = get_client()

        exist = client.query(q.let({'ref': q.match(q.index("noticias_Extra_by_link"), self.link)},
                                   q.if_(
            q.exists(q.var('ref')),
            q.get(q.var('ref')),
            False
        )
        ))

        if exist and exist['data'] != {**self.formatting(keys=True)}:
            result = client.query(q.update(q.ref(q.collection("extra"), exist['ref'].value['id']), {
                                  "data": {**self.formatting(keys=True)}}))
        elif not exist:
            result = client.query(q.create(q.collection(
                "extra"), {"data": {**self.formatting(keys=True)}}))

    def insert(self):
        Thread(target=self.upload).start()

    def formatting(self, keys=False):
        if keys:
            if self.imagem_link:
                return {'imagem_link': self.imagem_link,'link': self.link, 'body_title':self.body_title,'tipo_materia': self.tipo_materia, 'horario': self.horario}
            else:
                return {'link': self.link, 'body_title':self.body_title,'tipo_materia': self.tipo_materia, 'horario': self.horario}
        else:
            return {self.imagem_link,self.link,self.body_title,self.tipo_materia,self.horario}
