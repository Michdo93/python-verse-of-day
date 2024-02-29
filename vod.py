import requests
from bs4 import BeautifulSoup
from datetime import datetime

class VerseOfDay(object):
    def __init__(self, year=datetime.now().year, month=datetime.now().strftime("%m"), day=datetime.now().strftime("%d")):
        self.year = year
        self.month = month
        self.day = day

        url = "https://www.losungen.de/fileadmin/media-losungen/heute/{}/{}{}.html".format(year, self.__add_leading_zero(month), day)

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.contents = soup.find_all('font')
        else:
            print("Error accessing the verse of day {}".format(response.status_code))

    def __add_leading_zero(self, month):
        return "%02d" % month

    def get_verse_of_day(self):
        verse_of_day_content = self.contents[2]

        verse_of_day = verse_of_day_content.find('b').text.strip()
        verse_of_day_bible_passage = verse_of_day_content.find('br').next_sibling.strip()

        return "{} ({})".format(verse_of_day, verse_of_day_bible_passage)

    def get_teaching_text(self):
        teaching_text_content = self.contents[3]

        teaching_text = teaching_text_content.find('b').text.strip()
        teaching_text_bible_passage = teaching_text_content.find('br').next_sibling.strip()

        return "{} ({})".format(teaching_text, teaching_text_bible_passage)

if __name__ == "__main__":
    vod = VerseOfDay()
    print(vod.get_verse_of_day())

    print("\n")
    
    print(vod.get_teaching_text())
