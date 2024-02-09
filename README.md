# Simple English Dictionary
A Simple English Dictionary in JSON format - a list of words, with meanings, synonyms and antonyms.

**_Note:_**

This project is not mine 🙅‍♂️, here is the [author](https://github.com/nightblade9/simple-english-dictionary) ⭐.

## Usage

You can consume the data in a variety of formats:

- `data` contains the individual, raw files from tusharlock - they are broken out by letter.
- `processed/merged.json` contains a single JSON file with all the words in it.
- `processed/filtered.json` contains a version with filtered-out words, meanings, synonyms, and antonyms; you can see the list of filtered words in `data/filter_words.txt`

## My adjustment:

- `text` contains text file includes `20k_words.txt` ([source](https://github.com/first20hours/google-10000-english/blob/master/20k.txt)), `bad-words.txt` ([source](https://www.cs.cmu.edu/~biglou/resources/bad-words.txt)) and `selected.txt` which is the result of filtering words that does not contain bad words.

- `filter_swear.py` to remove bad words from `20k_words.txt`.

- `selected.py` to export `processed/selected.json` file.

## Creating your own Filtered List

You will need Python 3.x. Simply update `filter_Words.txt` and run `python3 filter.py`. Consider opening a PR, too!

## Run

To create a new selected words `text` file in `text/selected.txt`, run:

```
python filter_swear.py
```

To create a new selected words `json` file in `processed/selected.json`, run:

```
python selected.py
```

## Result

Both of them have no swear words.

`processed/filtered.json` contains `121297` words.

`processed/selected.json` contains `10595` words.
