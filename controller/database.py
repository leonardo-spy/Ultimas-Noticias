from faunadb import query as q
from db.fauna import get_client

def get_noticias(portal_noticia):
    noticias = []
    client = get_client()
    if portal_noticia == 'todos':
        result_raw = client.query(q.map_(q.lambda_("ref", q.get(q.var("ref"))),
            q.paginate(q.reverse(
                q.union(
                    q.join(q.documents(q.collection("estadao")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
                    q.join(q.documents(q.collection("extra")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
                    q.join(q.documents(q.collection("folha")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
                    q.join(q.documents(q.collection("g1")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
                    q.join(q.documents(q.collection("oglobo")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
                    q.join(q.documents(q.collection("uol")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
            )),size=50 )
            )
            )
    elif portal_noticia == 'estadao':
        result_raw = client.query(q.map_(q.lambda_("ref", q.get(q.var("ref"))),
            q.paginate(q.reverse(
                q.union(
                    q.join(q.documents(q.collection("estadao")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
            )),size=50 )
            )
            )
    elif portal_noticia == 'extra':
        result_raw = client.query(q.map_(q.lambda_("ref", q.get(q.var("ref"))),
            q.paginate(q.reverse(
                q.union(
                    q.join(q.documents(q.collection("extra")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
            )),size=50 )
            )
            )
    elif portal_noticia == 'folha':
        result_raw = client.query(q.map_(q.lambda_("ref", q.get(q.var("ref"))),
            q.paginate(q.reverse(
                q.union(
                    q.join(q.documents(q.collection("folha")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
            )),size=50 )
            )
            )
    elif portal_noticia == 'g1':
        result_raw = client.query(q.map_(q.lambda_("ref", q.get(q.var("ref"))),
            q.paginate(q.reverse(
                q.union(
                    q.join(q.documents(q.collection("g1")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
            )),size=50 )
            )
            )
    elif portal_noticia == 'oglobo':
        result_raw = client.query(q.map_(q.lambda_("ref", q.get(q.var("ref"))),
            q.paginate(q.reverse(
                q.union(
                    q.join(q.documents(q.collection("oglobo")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
            )),size=50 )
            )
            )
    elif portal_noticia == 'uol':
        result_raw = client.query(q.map_(q.lambda_("ref", q.get(q.var("ref"))),
            q.paginate(q.reverse(
                q.union(
                    q.join(q.documents(q.collection("uol")),
                    q.lambda_("ref", q.singleton(q.var("ref")))
                    ),
            )),size=50 )
            )
            )
    else:
        return noticias
    
    for noticia in result_raw['data']:
        portal = noticia['ref'].value['collection'].value['id']
        if portal == 'estadao':
            link = titulo = body_text = credito = data = imagem_link = None
            if 'link' in noticia['data']:
                link = noticia['data']['link']
            if 'titulo' in noticia['data']:
                titulo = noticia['data']['titulo']
            if 'body_text' in noticia['data']:
                body_text = noticia['data']['body_text']
            if 'credito' in noticia['data']:
                credito = noticia['data']['credito']
            if 'data' in noticia['data']:
                data = noticia['data']['data']
            if 'imagem_link' in noticia['data']:
                imagem_link = noticia['data']['imagem_link']
            noticias.append({'portal':portal,'link':link,'titulo':titulo,'body_text':body_text,'credito':credito,'data':data,'imagem_link':imagem_link})
        elif portal == 'extra':
            imagem_link = link = body_title = tipo_materia = horario = None
            if 'imagem_link' in noticia['data']:
                imagem_link = noticia['data']['imagem_link']
            if 'link' in noticia['data']:
                link = noticia['data']['link']
            if 'body_title' in noticia['data']:
                body_title = noticia['data']['body_title']
            if 'tipo_materia' in noticia['data']:
                tipo_materia = noticia['data']['tipo_materia']
            if 'horario' in noticia['data']:
                horario = noticia['data']['horario']
            noticias.append({'portal':portal,'imagem_link':imagem_link,'link':link,'body_title':body_title,'tipo_materia':tipo_materia,'horario':horario})
        elif portal == 'folha':
            imagem_link = credito = link = titulo = body_text = data = None
            if 'imagem_link' in noticia['data']:
                imagem_link = noticia['data']['imagem_link']
            if 'credito' in noticia['data']:
                credito = noticia['data']['credito']
            if 'link' in noticia['data']:
                link = noticia['data']['link']
            if 'titulo' in noticia['data']:
                titulo = noticia['data']['titulo']
            if 'body_text' in noticia['data']:
                body_text = noticia['data']['body_text']
            if 'data' in noticia['data']:
                data = noticia['data']['data']
            noticias.append({'portal':portal,'imagem_link':imagem_link,'credito':credito,'link':link,'titulo':titulo,'body_text':body_text,'data':data})
        elif portal == 'g1':
            titulo = link = body_text = imagem_link = horario = local = None
            if 'titulo' in noticia['data']:
                titulo = noticia['data']['titulo']
            if 'link' in noticia['data']:
                link = noticia['data']['link']
            if 'body_text' in noticia['data']:
                body_text = noticia['data']['body_text']
            if 'imagem_link' in noticia['data']:
                imagem_link = noticia['data']['imagem_link']
            if 'horario' in noticia['data']:
                horario = noticia['data']['horario']
            if 'local' in noticia['data']:
                local = noticia['data']['local']
            noticias.append({'portal':portal,'titulo':titulo,'link':link,'body_text':body_text,'imagem_link':imagem_link,'horario':horario,'local':local})
        elif portal == 'oglobo':
            imagem_link = tipo_materia = body_text = link = None
            if 'imagem_link' in noticia['data']:
                imagem_link = noticia['data']['imagem_link']
            if 'tipo_materia' in noticia['data']:
                tipo_materia = noticia['data']['tipo_materia']
            if 'body_text' in noticia['data']:
                body_text = noticia['data']['body_text']
            if 'link' in noticia['data']:
                link = noticia['data']['link']
            noticias.append({'portal':portal,'imagem_link':imagem_link,'tipo_materia':tipo_materia,'body_text':body_text,'link':link})
        elif portal == 'uol':
            link = imagem_link = tipo_materia = body_text = data = None
            if 'link' in noticia['data']:
                link = noticia['data']['link']
            if 'imagem_link' in noticia['data']:
                imagem_link = noticia['data']['imagem_link']
            if 'tipo_materia' in noticia['data']:
                tipo_materia = noticia['data']['tipo_materia']
            if 'body_text' in noticia['data']:
                body_text = noticia['data']['body_text']
            if 'data' in noticia['data']:
                data = noticia['data']['data']
            noticias.append({'portal':portal,'link':link,'imagem_link':imagem_link,'tipo_materia':tipo_materia,'body_text':body_text,'data':data})
            

    return noticias