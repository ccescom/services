from translate import yandex_translate , g_ajax_translate
from sms import send_sms
from voice import make_call
#from voice import make_call
result = yandex_translate("en", "hi", "Hello, world! Welcome to India")

print(result)

result = g_ajax_translate("en", "hi", "Hi, Prasanna, Today we cannot provide you the subsidy becuase of the shortage of power. So, your subsidy has been scheduled to 21st, March 2019")

PRADEEP_SIR = '9980469010'

send_sms(None, [PRADEEP_SIR], result, useDefault = True)

make_call('creds.json', text = result, lang = 'hi-IN', to = ['91'+PRADEEP_SIR])
