#TODO pixid定向查找
#TODO pixtag搜索
#TODO pix搜索
#TODO pixuid搜索
#TODO pixnovel搜索
#TODO pixnovelid定向
import webbrowser
import time
from googletrans import Translator

# 创建一个 Translator 对象
translator = Translator()

print("PixSearch\n版本号:Beta1\n请在出现[>>>]后再键入相关命令.\n---")

while True:
    print('选择你所需要的图床')
    print('[P]Pixiv.net')
    print('===')
    insert = input('图床选择>>>')
    if 'P' in insert or 'p' in insert:
        print('选择你需要的功能(Pixiv.net)')
        print('[1]Pixiv基础Tag搜索')
        print('[Q]返回')
        print('===')
        choice = input('功能选择>>>')

        while True:
            if choice == '1':
                search_word = input('关键词>>>')
                if search_word == 'QUIT':
                    break
                if search_word.endswith('/jp'):
                    # 如果是，去掉 "/jp" 并翻译为日文
                    search_word = search_word[:-3]
                try:
                    translated = translator.translate(search_word, dest='ja')
                    search_word = translated.text
                except AttributeError:
                    print("翻译失败，将使用原词")
                url = ('https://www.pixiv.net/tags/' + search_word + '/artworks?s_mode=s_tag&ai_type=1')
                webbrowser.open_new_tab(url)
                print('正在打开' + url)
            elif 'Q' in choice or 'q' in choice:
                break

            elif 'Q' in insert or 'q' in insert:
                print('即将在2秒后退出,[Enter]取消退出(暂时禁用)')
                #if input().strip() == '':
                #    print('已取消退出\n---')
                #    continue
            #else:
                time.sleep(2)
                break

    else:
        print('错误的')