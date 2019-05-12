import jieba
import wordcloud
import PIL.Image as image
import numpy as np
from pprint import pprint


def get_word_list():
    with open('D:\python\play\word.txt', encoding='utf-8') as f:
        text_my = f.read().split()
        my_str = ''
        for text_str in text_my:
            my_str += text_str
        # pprint(my_str)
        return(my_str)


def split_word(my_str):
    jieba.suggest_freq('中美', True)
    jieba.add_word('中美')
    word_list = jieba.cut(my_str, cut_all=False)
    my_list = " ".join(word_list).split(' ')
    # pprint(my_list)
    return(my_list)


def quit_stop_word(my_list):
    with open('D:\python\play\stopwords.txt', encoding='utf-8') as f:
        stop_word = f.read().split()
        # print(stop_word)
        result = ''
    # pprint(my_list)
    for word in my_list:
        if word not in stop_word:
            # pprint(word)
            result += word
            result += ' '
    # print(my_word)
    return result


def creat_image(result):
    jieba.load_userdict("D:\python\play\dict.txt")
    image_4 = image.open("D:\python\play\\1.png")
    mask = np.array(image.open("D:\python\play\\1.png"))
    font_path = "C:\Windows\Fonts\STXINGKA.TTF"
    image_4.show()
    imgcolor = wordcloud.ImageColorGenerator(mask)
    wd = wordcloud.WordCloud(
        mask=mask,
        font_path=font_path,  # 设置字体
        background_color="white",  # 背景颜色
        max_words=20000,  # 词云显示的最大词数
        max_font_size=200,  # 字体最大值
        min_font_size = 20,
        # random_state=42,
        color_func=imgcolor,

    ).generate(result)
    image_produce = wd.to_image()
    image_produce.show()


def main():
    my_str = get_word_list()
    my_list = split_word(my_str)
    result = quit_stop_word(my_list)
    creat_image(result)

if __name__ == '__main__':
    main()