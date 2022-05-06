import requests

IAM_TOKEN = 't1.9euelZrIk5HKi8iTy5qVlpWOnZPPy-3rnpWakIuJjMaPmpGVl5mNkpXKnZbl8_cSdC9s-e8SaV5t_t3z91IiLWz57xJpXm3' \
            '-.lnBmzsqrTNq1m26p7EXkf9Q1lj2i4q4SxnqB0E10qGoFuWLBuYWVR0rcZb9T5DfOlSdMbXVh9Bps46Xk5bP1CQ '
folder_id = 'b1g83nu3ghg9j3hciugr'
target_language_ru = 'ru'
target_language_tt = 'tt'
sourceLanguage_tat = 'tt'
sourceLanguage_rus = 'ru'
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {0}".format(IAM_TOKEN)
}


def tat_to_rus_translate(word_tat):
    symbols = '.,?!@#$%^&*()_+-=":;[]{}<>~`№'
    for i in symbols:
        word_tat = word_tat.replace(i, '')
    body = {
        "targetLanguageCode": target_language_ru,
        "texts": word_tat,
        "folderId": folder_id,
        "sourceLanguageCode": sourceLanguage_tat
    }
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    return response.json()['translations'][0]['text']


def rus_to_tat_translate(word_rus):
    symbols = '.,?!@#$%^&*()_+-=":;[]{}<>~`№'
    for i in symbols:
        word_rus = word_rus.replace(i, '')
    body = {
        "targetLanguageCode": target_language_tt,
        "texts": word_rus,
        "folderId": folder_id,
        "sourceLanguageCode": sourceLanguage_rus
    }
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    return response.json()['translations'][0]['text']


# print(rus_to_tat_translate('папа!"№;%:?*'))
# print(tat_to_rus_translate('әти!"№;%:?*'))
