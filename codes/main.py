from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from openpyxl import Workbook
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# openpyxl을 이용해 엑셀 파일로 저장하기 위한 준비 과정
excell = Workbook(write_only=True)
ws = excell.create_sheet()
ws.append(['score', 'title', 'writer', 'date', 'review', 'senti_score'])
list2 = []
# 웹 페이지 불러오기
url = 'https://www.imdb.com/title/tt4154796/reviews?ref_=tt_ql_3'
print(url)
webpage = urlopen(url)
source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')

review_list = source.findAll('div', {'class': 'imdb-user-review'})

sid = SentimentIntensityAnalyzer()  # VADER 감정분석기 미리 준비

sum_review = ''  # wordcloud 띄워줄때 쓸 모든 리뷰 텍스트 다 합친 문자열

# 각 리뷰마다...
for review in review_list:
    # 리뷰 내에서 태그, 클래스 이용해서 정보 뽑아내는 부분
    list1 = []
    score = review.find('span').get_text()
    title = review.find('a').get_text().replace('\n', '')
    writer = review.find('span', {'class': 'display-name-link'}).get_text()
    date = review.find('span', {'class': 'review-date'}).get_text()
    content = review.find('div', {'class': 'text show-more__control'}).get_text()

    # 엑셀 파일에 저장하기 위해 list에 각 정보를 추가
    list1.append(score)
    list1.append(title)
    list1.append(writer)
    list1.append(date)
    list1.append(content)
    sum_review = sum_review + content
    list2.append(content)
    lines_list = tokenize.sent_tokenize(content)  # 리뷰 텍스트를 문장별로 쪼개는 전처리 함수

    sum = 0
    for sent in lines_list:  # 한 리뷰의 각 문장마다 감정 점수 계산
        ss = sid.polarity_scores(sent)
        print(ss['compound'])
        sum = sum + ss['compound']
    sum1 = str(sum / len(lines_list))  # 문장들의 평균점수가 그 리뷰의 감정 점수
    list1.append(sum1)
    ws.append(list1)  # 지금까지 뽑아냈던 내용들을 openpyxl worksheet에 저장

excell.save('imdb_.xlsx')  # imdb_.xlsx라는 파일명으로 엑셀파일 저장
