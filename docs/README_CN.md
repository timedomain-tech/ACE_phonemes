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

## 使用

`main.py` 中包含了基本的用例:
1. 检查音素是否包含在系统中
2. 中文，日语，英语的音素转换

## 贡献

欢迎补充内容和讨论修改建议，可以提issue或者发邮件到 sean.z@timedomain.ai

## 许可

本项目采用 MIT 许可证授权 - 详情请查看 [LICENSE](LICENSE) 文件。
