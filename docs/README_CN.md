# ACE音素

## 简介

我们介绍了ACE SVS（歌声合成）引擎的字素到音素（G2P）转换字典和音素列表。

目前，我们支持三种语言：中文、日文和英文。

## 资源

以下是每个文件的简要说明：

- ***all_plans.json***：该文件包含多个字典，每个字典的含义如下：
    - **jp_word2romaji**：日语假名到罗马音的转换字典。
    - **plans**：每种语言都有自己的音素构成
        - **syllable_alias** 表示每个音节可以有多种拼写。
        - **dict** 包含音节到音素的字典。
        - **phon_class** 包含所有音素，**head** 表示辅音，**tail** 表示元音。
- ***cmudict.rep***：该文件包含英语发音词典，参考网址：http://www.speech.cs.cmu.edu/cgi-bin/cmudict