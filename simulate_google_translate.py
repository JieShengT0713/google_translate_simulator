import time
from selenium import webdriver
import pprint
import json
import sys
from selenium.webdriver.common.keys import Keys

pp = pprint.PrettyPrinter()
driver = webdriver.Firefox()
ori = 'en'
translate_text_list = {}
# allLang = ['id', 'zh-TW', 'zh-CN']
allLang = ['id']
json_text = '''{
    "lang":["id","zh-TW","zh-CN"],
    "words":{"length_menu":"Display MENU records per page","zero_records":"Nothing found","info_table":"Showing page PAGE to PAGES of MAX records","info_empty":"No records available","info_filtered":"(filtered from MAX total records)","loading_records":"Loading...","processing..":"Processing...","search":"Search:","first":"First","last":"Last","next":"Next","previous":"Previous","index":"No.","conversion":"Conversion","dashboard":"Dashboard","rates":"Rates","set_rates":"Set Rates","currencies":"Currencies","pending_orders":"Pending Orders","orders":"Orders","order_or_transaction_id":"Order ID \/ Transaction ID","from_currency":"Currency From","to_currency":"Currency To","datetime":"Datetime","order_id":"Order ID","user":"User","status":"Status","action":"Action","new_order":"New Order","upload_doc":"Upload Document","complete":"Complete","cancelled":"Cancelled","description":"Description","change":"Change","rate":"Rate","total":"Total","view_receipt":"View Receipt","print":"Print","user_settings":"User Settings","profile":"Profile","admin_list":"Admin List","agent_list":"Agent List","user_list":"User List","enter_amount":"Enter your amount","not_setting_yet":"Not set yet","reset_password":"Reset Password","logout":"Logout","username":"Username","email":"Email","current_password":"Current Password","new_password":"New Password","cnew_password":"Confirm New Password","cancel":"Cancel","confirm":"Confirm","edit_admin":"Edit Admin","add_admin":"Add Admin","submit":"Submit","name":"Name","phone":"Phone"}
}
'''
text = json.loads(json_text)
pp.pprint(text)



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
    print(json.dumps(cur_translation))
    translate_text_list[cur_lang] = json.dumps(cur_translation)
driver.close()
translate_text_list = json.dumps(translate_text_list)
print(translate_text_list)

# formatted_string = pprint.pformat(translate_text_list, indent=4)
# formatted_string = formatted_string.replace(':', ' => ')
# print(formatted_string)
