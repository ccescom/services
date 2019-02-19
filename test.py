from translate import yandex_translate , g_ajax_translate
from sms import send_sms

result = yandex_translate("en", "hi", "Hello, world! Welcome to India")

print(result)

result = g_ajax_translate("en", "hi", "Hi, Shravan! How are you ?")

send_sms(None, ['9108287991'], result, useDefault = True)

