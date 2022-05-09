from distutils.util import strtobool
from time import sleep

from controller.G1 import G1
from controller.Oglobo import Oglobo
from controller.Extra import Extra
from controller.Estadao import Estadao
from controller.Folha import Folha
from controller.Uol import Uol


def app_temp(vars_env):
    time_loop = 10#eval(vars_env['TEMPO_VERIFICACAO'])
    while True:
        
        print('iniciando serviço para G1')
        g1_news = G1()
        g1_news.run()
    
    
        print('iniciando serviço para O Globo')
        oglobo = Oglobo()
        oglobo.run()
    
    
        print('iniciando serviço para Extra')
        extra = Extra()
        extra.run()
    
    
        print('iniciando serviço para Estadão')
        estadao = Estadao()
        estadao.run()
    
    
        print('iniciando serviço para Folha')
        folha = Folha()
        folha.run()
    
    
        print('iniciando serviço para Uol')
        uol = Uol()
        uol.run()
        
        print('Aguardando {} segundos...'.format(time_loop))
        break
        sleep(time_loop)
