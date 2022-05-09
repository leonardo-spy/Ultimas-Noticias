from distutils.util import strtobool
from time import sleep

from controller.G1 import G1
from controller.Oglobo import Oglobo
from controller.Extra import Extra
from controller.Estadao import Estadao
from controller.Folha import Folha
from controller.Uol import Uol


def app(vars_env):
    time_loop = eval(vars_env['TEMPO_VERIFICACAO'])
    while True:
        if strtobool(vars_env['G1']):
            print('iniciando serviço para G1')
            g1_news = G1()
            g1_news.run()
        
        if strtobool(vars_env['OGLOBO']):
            print('iniciando serviço para O Globo')
            oglobo = Oglobo()
            oglobo.run()
        
        if strtobool(vars_env['EXTRA']):
            print('iniciando serviço para Extra')
            extra = Extra()
            extra.run()
        
        if strtobool(vars_env['ESTADAO']):
            print('iniciando serviço para Estadão')
            estadao = Estadao()
            estadao.run()
        
        if strtobool(vars_env['FOLHA']):
            print('iniciando serviço para Folha')
            folha = Folha()
            folha.run()
        
        if strtobool(vars_env['UOL']):
            print('iniciando serviço para Uol')
            uol = Uol()
            uol.run()
        
        print('Aguardando {} segundos...'.format(time_loop))
        sleep(time_loop)
