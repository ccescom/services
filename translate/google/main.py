from googletrans import Translator

class Translate():

    def __init__(self, source_ln, dest_ln) :
        self.source_ln = source_ln
        self.dest_ln = dest_ln

        self.translator = Translator(
            #we will add parameters here, if proxy is required    
            service_urls=[
            'translate.google.com',
            'translate.google.co.kr',
            ]
        )

    def translate(self, text):

        return self.translator.translate(text, src = self.source_ln, dest = self.dest_ln)


def translate_text(src, dst, text):

    return Translate(src, dst).translate(text).text
