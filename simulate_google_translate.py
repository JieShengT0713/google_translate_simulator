import time
from selenium import webdriver
import pprint
from selenium.webdriver.common.keys import Keys

pp = pprint.PrettyPrinter()
driver = webdriver.Firefox()
ori = 'en'
translate_text_list = {}
allLang = ['id', 'zh-TW', 'zh-CN']
text = {
    }
for cur_lang in allLang:
    cur_translation = {}
    for word in text:
        ori_text = text[word]
        print(text[word])
        driver.get('https://translate.google.com/#view=home&op=translate&sl='+ ori +'&tl='+ cur_lang +'&text=' + ori_text)
        time.sleep(1)
        translate_text = driver.find_element_by_class_name('tlid-translation')
        # print(translate_text)
        print(translate_text.text)
        cur_translation[word] = translate_text.text

        # driver.close()
    translate_text_list[cur_lang] = cur_translation
driver.close()
pp.pprint(translate_text_list)