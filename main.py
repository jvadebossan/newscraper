#import urllib.request
from urllib import request
import requests as req
from bs4 import BeautifulSoup
from time import sleep as wait
from colorama import init
from termcolor import colored
from link_generator import main as link_gen
from emailer import main as send_email

types = {'1': 'tecnologia', '2': 'política', '3': 'saúde', '4': 'educação'}
links = {'1': 'https://g1.globo.com/economia/tecnologia/', '2': 'https://g1.globo.com/politica/', '3': 'https://g1.globo.com/ciencia-e-saude/', '4': 'https://g1.globo.com/educacao/'}
notices = {'titles':[], 'contents':[], 'links':[]}

print(colored('''
                                                        
 _ __   _____      _____  ___ _ __ __ _ _ __   ___ _ __ 
| '_ \ / _ \ \ /\ / / __|/ __| '__/ _` | '_ \ / _ \ '__|
| | | |  __/\ V  V /\__ \ (__| | | (_| | |_) |  __/ |   
|_| |_|\___| \_/\_/ |___/\___|_|  \__,_| .__/ \___|_|   
                                       |_|              
                                                        
''', 'blue'))


def send_notice(send):
    global msg
    msg = ''
    for i in range(0, 5):
        msg += f'{notices["titles"][i]}\n'
        msg += f'{notices["contents"][i]}\n\n'
    if send == '1':
        for i in range(0, 5):
            print(colored(notices['titles'][i], 'green'))
            print(colored(notices['contents'][i], 'yellow'))
            print('\n')
            print(colored('Essas foram as notícias.', 'blue'))
    elif send == '2':
        txt = open('notícias.txt', 'w', encoding='utf-8')
        for i in range(0, 5):
            txt.write(f'{notices["titles"][i]}\n')
            txt.write(f'{notices["contents"][i]}\n\n')
            print(colored('As notícias foram salvas em "notícias.txt".', 'blue'))
    elif send == '3':
        email = input('Informe seu e-mail: ')
        send_email(email, msg, types[type_notice])
        print(colored('As notícias foram enviadas.', 'blue'))
    elif send == '4': 
        link = link_gen('Notícias', msg)
        print('\nLink para acessar as notícias: ', end='')
        print(colored(link, 'blue'))


def ver_send_notice():
    print('[1 = vê-las, 2 = salvar localmente, 3 = enviar no email, 4 = gerar link]\nForam encontradas 5 notícias. Deseja vê-las, salva-las, gerar um link ou envia-las em seu email? ', end="")
    send = str(input())
    if send not in ['1', '2', '3', '4']:
        print(colored('Escolha uma categoria corretamente (1, 2, 3 ou 4)', 'red'))
        wait(2)
        ver_send_notice()
    else:
        send_notice(send)


def get_notice(type_num):
    print(colored(f'coletando as notícias mais recentes sobre {types[type_num]}...\n', 'green'))
    res = req.get(links[type_num])
    content = res.content
    site = BeautifulSoup(content, 'html.parser')
    cards = site.find_all('a', 'feed-post-link')
    conts = []
    try:
        for i in range(0, 5):
            title = cards[i].text
            notices['titles'].append(title)
            content_link = cards[i].get('href')
            res_ntc = req.get(content_link)
            content_ntc = res_ntc.content
            site_ntc = BeautifulSoup(content_ntc, 'html.parser')
            card_ntc = site_ntc.find_all('p', 'content-text__container')
            for i in range(0, 2):
                p = card_ntc[i].text
                conts.append(p)
                notices['links'].append(content_link)

        for i in range(0, 10, 2):
            notices['contents'].append(conts[i] + conts[i+1])
    except:
        print('houve um problema ao coletar suas notícias')
    ver_send_notice()

def setup():
    global type_notice
    type_num = str(input('[1 = tecnologia, 2 = política, 3 = saúde, 4 = educação]\nEscolha uma categoria de notícia: '))
    type_notice = type_num
    if type_num not in ['1', '2', '3', '4']:
        print(colored('Escolha uma categoria corretamente (1, 2, 3 ou 4)', 'red'))
        wait(2)
        setup()
    else:
        get_notice(type_num)


setup()
