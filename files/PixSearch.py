#TODO pixnovel搜索
#TODO pixnovelid定向
import webbrowser
import time
import re

print("PixSearch\n版本号:v0.1.1\n请在出现[>>>]后再键入相关命令.\n---")

while True:
    print('选择你所需要的图床')
    print('[P]Pixiv.net')
    print('[J]JMComic')
    #https://18comic.vip/album/523565
    print('[Q]退出')
    print('===')
    insert = input('图床选择>>>')
    if 'P' in insert or 'p' in insert:
        print('选择你需要的功能(Pixiv.net)')
        print('[1]Tag标签搜索')
        print('[2]PID定向跳转')
        #print('[2X]PID第一张原图')
        print('[2H]PID混淆跳转 /*比如文字内包含神秘数字')
        print('[3]用户UID定向跳转')
        #print('[4]Pixiv小说搜索')
        #print('[5]Pixiv小说定向')
        print('[Q]返回\n===')
        choice = input('功能选择>>>')

        while True:
            if choice == '1':#Tag
                search_word = input('关键词>>>')
                if search_word == 'QUIT':
                    break
                url = f'https://www.pixiv.net/tags/{search_word}/artworks?s_mode=s_tag&ai_type=1'
                webbrowser.open_new_tab(url)
                print('正在打开:' + url)   
            
            elif choice == '2':#PID
                search_word = input('PID>>>')
                if search_word == 'QUIT':
                    break
                url = f'https://www.pixiv.net/artworks/{search_word}'
                webbrowser.open_new_tab(url)
                print('正在打开:' + url) 
            
            elif '2H' in choice or '2h' in choice:#PID混淆
                user_input = input('输入文字>>>')
                if user_input == 'QUIT':
                    break
                only_numbers = re.findall(r'\d+', user_input)
                search_word = ''.join(only_numbers)
                url = f'https://www.pixiv.net/artworks/{search_word}'
                webbrowser.open_new_tab(url)
                print('正在打开:' + url)
            
            elif choice == '3':#UID
                search_word = input('UID>>>')
                if search_word == 'QUIT':
                    break
                url = f'https://www.pixiv.net/users/{search_word}'
                webbrowser.open_new_tab(url)
                print('正在打开:' + url)
            
            elif 'Q' in choice or 'q' in choice:
                break

            else:
                continue
                             
    elif 'Q' in insert or 'q' in insert:
        print('即将在2秒后退出')
        time.sleep(2)
        break

    else:
        print('错误的')