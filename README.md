# python-verse-of-day
The daily verse of day and teaching text in German.

## Pre-Installation

The code works in Python `2.7` and `Python 3.x` so you have to install following:

### Python 2.7

```
python -m pip install requests
python -m pip install beautifulsoup4
```

### Python 3.x

```
python3 -m pip install requests
python3 -m pip install beautifulsoup4
```

## Usage

### Python 2.7

```
python vod.py
```

### Python 3

```
python3 vod.py
```

## Customization

You can change the current day

```
if __name__ == "__main__":
    vod = VerseOfDay()
    print(vod.get_verse_of_day())

    print("\n")
    
    print(vod.get_teaching_text())
```

to a specific date

```
if __name__ == "__main__":
    vod = VerseOfDay("2024","02","20")
    print(vod.get_verse_of_day())

    print("\n")
    
    print(vod.get_teaching_text())
```

Please notice that integers could be parsed to strings, so it would also work with:

```
if __name__ == "__main__":
    vod = VerseOfDay(2024,02,20)
    print(vod.get_verse_of_day())

    print("\n")
    
    print(vod.get_teaching_text())
```
