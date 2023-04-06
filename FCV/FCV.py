import folium
import pandas as pd
import os
import io
from folium import utilities
from folium import plugins
import webbrowser


#문제점: 
#   1.글꼴 크기가 작다.
#   2.오토 스케일 좀더 보기 편하게 자동적으로 경로 전체가 보이게 하기
#   3.*패키징 라이브러리화 Folium처럼 함수같이 사용 가능하게 만들기*
#해결방안:  
#   1.folium 맵 스타일 기능에서 변경 가능
#   2.Foliunm 내부 오토 스케일 기능 여부 확인
#   3.setup.py 패키징 이용

#현재 가상환경 경로 데이터 수집
dir=os.getcwd()+'\\'
#미세먼지 측정 데이터파일(.csv) 경로 입력
a=str(input('데이터 파일의 경로를 입력해주세요:'))

#데이터파일 경로를 따라 인식
df = pd.read_csv(a,encoding='cp949')

#처음 시작 지점 위치 값 추출
Start=df.loc[[1],['Latitude','Longitude']]

#시작지점 좌표 출력 
print('\n 시작지점')
print(Start)

#미세먼지 농도를 리스트 변형
pm= df['PM2.5'].tolist()

#미세먼지 농도에 따른 좌표 및 농도 지수 배열 생성

over_PM= []
over_gps = []
over_PM15= []
over_gps15 = []
over_PM35= []
over_gps35 = []
over_PM75= []
over_gps75 = []

#맵 생성 초기 관측 좌표 설정 및 스타일 설정
m=folium_map=folium.Map(Start,zoom_start=15)

#마우스 위치에 따른 위도 경도를 오른쪽 및에 표기
plugins.MousePosition().add_to(m)


#미세먼지농도에 따른 분류

#좋음
for n in df.index:
    if pm[n] <= 15:
        over_gps.append([df['Latitude'][n],df['Longitude'][n]])
        over_PM.append(pm[n])

#보통
for n in df.index:
        if pm[n] > 15 and pm[n] <= 35:
            over_gps15.append([df['Latitude'][n],df['Longitude'][n]])
            over_PM15.append(pm[n])
#나쁨       
for n in df.index:
    if pm[n] > 35 and pm[n] <= 75:
        over_gps35.append([df['Latitude'][n],df['Longitude'][n]])
        over_PM35.append(pm[n])

#매우 나쁨
for n in df.index:
    if pm[n] > 75:
        over_gps75.append([df['Latitude'][n],df['Longitude'][n]])
        over_PM75.append(pm[n])

#미세먼지농도에 따라 색상을 달리 표시한다.

#좋음
for i in range(len(over_gps)):
    folium.CircleMarker(over_gps[i],
    tooltip= str(over_PM[i])+"pm",radius=5,fill=True,color='none',fill_opacity=1, fill_color='#3498db').add_to(m)

#보통
for i in range(len(over_gps15)):
    folium.CircleMarker(over_gps15[i],
    tooltip= str(over_PM15[i])+"pm",radius=5,fill=True,color='none',fill_opacity=0.7, fill_color='GREEN').add_to(m)

#나쁨
for i in range(len(over_gps35)):
    folium.CircleMarker(over_gps35[i],
    tooltip= str(over_PM35[i])+"pm",radius=5,fill=True,color='none',fill_opacity=0.5, fill_color='#f1c40f').add_to(m)

#매우 나쁨
for i in range(len(over_gps75)):
    folium.CircleMarker(over_gps75[i],
    tooltip= str(over_PM75[i])+"pm",radius=5,fill=True,color='none',fill_opacity=0.7, fill_color='#c0392b').add_to(m)

#HTML 맵 저장 시 미세먼지 농도 지표 이미지 파일 구성요소 추가
m.get_root().html.add_child(folium.Element("""
<div style="position: fixed; 
     top: 50px; right: 70px; width: 117px; height: 525px; 
     background-color:white; border:2px solid grey;z-index: 900;">
    <img src="지표.jpg" alt="미세먼지농도지표"></img>
</div>
"""))


#저장할 Html파일 이름 지정
Name=str(input('저장할 HTML 이름을 입력해주세요:'))
m.save(Name+'.html')  

print('\n HTML파일생성이 완료 되었습니다!')  
print('\n 저장 경로는'+dir+Name+'.html입니다')


#생성된 HTML 파일 자동실행
with open(dir+Name+'.html', 'r') as f:
    f.close()
webbrowser.open_new_tab(dir+Name+'.html')


#png파일로 저장하는 라이브러리 (추가예정)
#async def map_to_png(target, m):
    #html = m.get_root().render()
    #browser = await launch(headless=True)

    #page = await browser.newPage()
    #with utilities.temp_html_filepath(html) as fname:
        #await page.goto('file://{path}'.format(path=fname))
#해당 코드로 html 페이지를 열어서 스크린샷으로 찍어 png 파일로 저장할 수 있습니다.
# path 옵션을 이용해서 경로를 지정할 수 있습니다. 지금 같은 경우는 output 폴더 안에 저장이 됩니다.

    #img_data = await page.screenshot({'path': f'output/out_{target}.png', 'fullPage': 'true', })
    #await browser.close()

# 함수 test 허리둘레 지도 시각화
#target = '허리둘레'
#waste_m = load_map(target) # folium 으로 맵 만들기
#await map_to_png(target, waste_m)

