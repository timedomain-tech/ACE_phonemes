# ACE_phonemes  
[简体中文](docs/README_CN.md)

## Introduction

We introduce our grapheme-to-phoneme (G2P) conversion dictionary and phoneme lists for the ACE SVS(singing voice synthesis) engine.

Currently, we support three languages: Chinese, Japanese, and English.

## Resources

Here is a brief description of each file:

- ***all_plans.json***: this file contains several dictionaries, and the meaning of each dictionary is as follows: 
    - **jp_word2romaji**: Japanese Kana to Romaji dictionary
    - **plans**: each language has a plan. 
        - **syllable_alias** means each syllable can have multiple spellings. 
        - **dict** contains syllable to phoneme dictionary. 
        - **phon_class** contains all phonemes, **head** is consonant and **tail** is vowel
- ***cmudict.rep***: This file contains English pronouncing dictionary, ref: http://www.speech.cs.cmu.edu/cgi-bin/cmudict

## Usage

The `main.py` file contains basic use cases:
1. Checking whether a phoneme is included in the system.
2. Converting phonemes for Chinese, Japanese, and English.

## Contributing

Contributions and suggestions for modification are welcome. You can open an issue or send an email to sean.z@timedomain.ai.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.