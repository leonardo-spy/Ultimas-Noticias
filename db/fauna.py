from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = None


def init(vars_env):
    global client
    client = FaunaClient(secret='fnAEl9jw6MAAQPFRp1Q668GoCxhxT94StjwG-xpN', domain='db.us.fauna.com')
    create_collections()


def get_client():
    return client


def create_collections():
    g1_exist = client.query(q.exists(q.collection("g1")))
    if not g1_exist:
        g1_collection = client.query(q.create_collection({"name": "g1"}))
        result_g1 = client.query(q.create_index(
            {
                "name": "noticias_G1_by_link",
                "source": q.collection("g1"),
                "terms": [{"field": ["data", "link"]}]
            }
        )
        )

    oglobo_exist = client.query(q.exists(q.collection("oglobo")))
    if not oglobo_exist:
        oglobo_collection = client.query(q.create_collection({"name": "oglobo"}))
        result_oglobo = client.query(q.create_index(
            {
                "name": "noticias_Oglobo_by_link",
                "source": q.collection("oglobo"),
                "terms": [{"field": ["data", "link"]}]
            }
        )
        )

    extra_exist = client.query(q.exists(q.collection("extra")))
    if not extra_exist:
        extra_collection = client.query(q.create_collection({"name": "extra"}))
        result_extra = client.query(q.create_index(
            {
                "name": "noticias_Extra_by_link",
                "source": q.collection("extra"),
                "terms": [{"field": ["data", "link"]}]
            }
        )
        )

    estadao_exist = client.query(q.exists(q.collection("estadao")))
    if not estadao_exist:
        estadao_collection = client.query(q.create_collection({"name": "estadao"}))
        result_estadao = client.query(q.create_index(
            {
                "name": "noticias_Estadao_by_link",
                "source": q.collection("estadao"),
                "terms": [{"field": ["data", "link"]}]
            }
        )
    )

    folha_exist = client.query(q.exists(q.collection("folha")))
    if not folha_exist:
        folha_collection = client.query(q.create_collection({"name": "folha"}))
        result_folha = client.query(q.create_index(
            {
                "name": "noticias_Folha_by_link",
                "source": q.collection("folha"),
                "terms": [{"field": ["data", "link"]}]
            }
        )
        )

    uol_exist = client.query(q.exists(q.collection("uol")))
    if not uol_exist:
        uol_collection = client.query(q.create_collection({"name": "uol"}))
        result_folha = client.query(q.create_index(
            {
                "name": "noticias_Uol_by_link",
                "source": q.collection("uol"),
                "terms": [{"field": ["data", "link"]}]
            }
        )
        )
