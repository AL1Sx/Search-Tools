#TODO pixid定向查找
#TODO pixtag搜索
#TODO pix搜索
#TODO pixuid搜索
#TODO pixnovel搜索
#TODO pixnovelid定向
import webbrowser
import time

print("PixSearch\n版本号:Beta3\n请在出现[>>>]后再键入相关命令.\n---")

while True:
    print('选择你所需要的图床')
    print('[P]Pixiv.net')
    print('[Q]退出')
    print('===')
    insert = input('图床选择>>>')
    if 'P' in insert or 'p' in insert:
        print('选择你需要的功能(Pixiv.net)')
        print('[1]Tag标签搜索')
        print('[2]PID定向跳转')
        #print('[2X]PID第一张原图')
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
                print('正在打开' + url)   
            elif choice == '2':#PID
                search_word = input('PID>>>')
                if search_word == 'QUIT':
                    break
                url = f'https://www.pixiv.net/artworks/{search_word}'
                webbrowser.open_new_tab(url)
            elif choice == '3':#UID
                search_word = input('UID>>>')
                if search_word == 'QUIT':
                    break
                url = f'https://www.pixiv.net/users/{search_word}'
                webbrowser.open_new_tab(url)
                print('正在打开' + url)
            elif 'Q' in choice or 'q' in choice:
                break
                             
    elif 'Q' in insert or 'q' in insert:
        print('即将在2秒后退出')
        time.sleep(2)
        break

    else:
        print('错误的')