from pyaspeller import YandexSpeller

_speller = YandexSpeller()


def edit_word(command):
    if not isinstance(command, str):
        return
    return _speller.spelled(command)
