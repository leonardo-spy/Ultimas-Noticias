from threading import Thread
from faunadb import query as q

from db.fauna import get_client


class Folha_noticia:
    def __init__(self, imagem_link,credito,link,titulo,body_text,data):
        self.imagem_link = imagem_link
        self.credito = credito
        self.link = link
        self.titulo = titulo
        self.body_text = body_text
        self.data = data        

    def upload(self):
        client = get_client()

        exist = client.query(q.let({'ref': q.match(q.index("noticias_Folha_by_link"), self.link)},
                                   q.if_(
            q.exists(q.var('ref')),
            q.get(q.var('ref')),
            False
        )
        ))

        if exist and exist['data'] != {**self.formatting(keys=True)}:
            result = client.query(q.update(q.ref(q.collection("folha"), exist['ref'].value['id']), {
                                  "data": {**self.formatting(keys=True)}}))
        elif not exist:
            result = client.query(q.create(q.collection(
                "folha"), {"data": {**self.formatting(keys=True)}}))

    def insert(self):
        #Thread(target=self.upload).start()
        self.upload()

    def formatting(self, keys=False):
        if keys:
            if self.imagem_link:
                return {'imagem_link': self.imagem_link,'credito' : self.credito,'link' : self.link,'titulo' : self.titulo,'body_text' : self.body_text,'data' : self.data}
            else:
                return {'credito' : self.credito,'link' : self.link,'titulo' : self.titulo,'body_text' : self.body_text,'data' : self.data}
        else:
            return {self.imagem_link,self.credito,self.link,self.titulo,self.body_text,self.data}
