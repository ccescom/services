from translate import yandex_translate , g_ajax_translate
from sms import send_sms

result = yandex_translate("en", "hi", "Hello, world! Welcome to India")

print(result)

#using shravan for test!! :p
result2 = g_ajax_translate("en", "hi", "Hi Shravan! How are you ?")

print(result2)

send_sms(None, ['9611818690'], result, useDefault = True)

