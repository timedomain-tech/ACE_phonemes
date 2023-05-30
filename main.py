import src.cmudict_reader as cmudict_reader
import src.plan_reader as plan_reader


def is_valid_phoneme(phoneme):

    return False


# 拼音到音素
def pinyin_to_phoneme(pinyin):
    pass


# 日本語変換音素
def jp_word_to_phoneme(jp_word):
    pass


# english word to phoneme
def eng_word_to_phoneme(en_word):

    eng_dict = cmudict_reader.get_dict()

    word_key = en_word.upper()
    phonemes = eng_dict[word_key]






