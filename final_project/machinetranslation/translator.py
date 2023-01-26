import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    if (len(english_text) > 0):
        """ Translating the input from English to French"""
        translation = language_translator.translate(english_text, model_id='en-fr').get_result()
        return translation['translations'][0]['translation']
    else:
        return "Please enter a valid English word"

def french_to_english(french_text):
    if(len(french_text) >0):
        """ Translating the input from French to English"""
        translation = language_translator.translate(french_text, model_id='fr-en').get_result()
        return translation['translations'][0]['translation']
    else:
        return "Entrez un mot français valide"