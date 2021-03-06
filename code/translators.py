from google.cloud import translate
import google.cloud
from code.helpers import get_key_path

def GoogleTranslate(input_text, out_language, dir_path, in_language='en'):
    # Get Google Key path
    key_path = get_key_path(dir_path=dir_path)
    # Initialize Translation Client
    translate_client = translate.Client.from_service_account_json(key_path)
    # Translate text
    translation = translate_client.translate(input_text, target_language=out_language)
    return translation
