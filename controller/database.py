from faunadb import query as q
from db.fauna import get_client

def get_noticias(portal_noticia):
    noticias = []
    client = get_client()

    try:
        if portal_noticia == 'todos':
            colecoes = ['estadao', 'extra', 'folha', 'g1', 'oglobo', 'uol']
            union_list = [q.documents(q.collection(c)) for c in colecoes]

            result_raw = client.query(
                q.map_(
                    q.lambda_("ref", q.get(q.var("ref"))),
                    q.paginate(q.reverse(q.union(*union_list)), size=50)
                )
            )
        elif portal_noticia in ['estadao', 'extra', 'folha', 'g1', 'oglobo', 'uol']:
            result_raw = client.query(
                q.map_(
                    q.lambda_("ref", q.get(q.var("ref"))),
                    q.paginate(q.reverse(q.documents(q.collection(portal_noticia))), size=50)
                )
            )
        else:
            return noticias
    except Exception as e:
        print(f"Erro ao consultar FaunaDB: {e}")
        return noticias

    for noticia in result_raw['data']:
        portal = noticia['ref'].value['collection'].value['id']
        data_fields = noticia.get('data', {})

        if portal == 'estadao':
            noticias.append({
                'portal': portal,
                'link': data_fields.get('link'),
                'titulo': data_fields.get('titulo'),
                'body_text': data_fields.get('body_text'),
                'credito': data_fields.get('credito'),
                'data': data_fields.get('data'),
                'imagem_link': data_fields.get('imagem_link')
            })
        elif portal == 'extra':
            noticias.append({
                'portal': portal,
                'imagem_link': data_fields.get('imagem_link'),
                'link': data_fields.get('link'),
                'body_title': data_fields.get('body_title'),
                'tipo_materia': data_fields.get('tipo_materia'),
                'horario': data_fields.get('horario')
            })
        elif portal == 'folha':
            noticias.append({
                'portal': portal,
                'imagem_link': data_fields.get('imagem_link'),
                'credito': data_fields.get('credito'),
                'link': data_fields.get('link'),
                'titulo': data_fields.get('titulo'),
                'body_text': data_fields.get('body_text'),
                'data': data_fields.get('data')
            })
        elif portal == 'g1':
            noticias.append({
                'portal': portal,
                'titulo': data_fields.get('titulo'),
                'link': data_fields.get('link'),
                'body_text': data_fields.get('body_text'),
                'imagem_link': data_fields.get('imagem_link'),
                'horario': data_fields.get('horario'),
                'local': data_fields.get('local')
            })
        elif portal == 'oglobo':
            noticias.append({
                'portal': portal,
                'imagem_link': data_fields.get('imagem_link'),
                'tipo_materia': data_fields.get('tipo_materia'),
                'body_text': data_fields.get('body_text'),
                'link': data_fields.get('link')
            })
        elif portal == 'uol':
            noticias.append({
                'portal': portal,
                'link': data_fields.get('link'),
                'imagem_link': data_fields.get('imagem_link'),
                'tipo_materia': data_fields.get('tipo_materia'),
                'body_text': data_fields.get('body_text'),
                'data': data_fields.get('data')
            })

    return noticias