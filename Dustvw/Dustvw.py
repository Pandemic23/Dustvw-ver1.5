import folium
import pandas as pd
import os
import io
import urllib.request
from folium import utilities
from folium import plugins
import webbrowser
def Dustvw():
    if os.path.isfile('encoding.csv'):
        print("\a 데이터.csv가 존재합니다")
    
    else:
        #데이터 텍스 파일 경로 입력
        data= str(input('데이터텍스트 경로 입력:'))
        new_text_content = '' #텍스트 자료값 초기화
        with open(data,'r') as f:
            lines = f.readlines()
        for i, l in enumerate(lines):
            new_string=l.strip().replace("PM 1.0 : ","").replace(" PM 2.5 : ","").replace(" PM 10 : ","").replace("Temperature = ","").replace(" Humidity = ","").replace("speed: ","").replace(" Latitude: ","").replace("Longitude: ","")
            if new_string:
                    new_text_content += new_string + '\n'
            else:
                    new_text_content += '\n'   
        with open(data,'w') as f:
            f.write('time,PM 1.0,PM2.5,PM 10,Temperature,Humidity,speed,Latitude,Longitude\n')
            f.write(new_text_content)
        file = pd.read_csv(data)
        new_csv_file = file.to_csv(os.getcwd()+'\\encoding.csv')
    #현재 가상환경 경로 데이터 수집
    dir=os.getcwd()+'\\'
    #데이터csv파일 경로를 따라 인식
    df = pd.read_csv(str(os.getcwd()+'\\encoding.csv'))
    #위치 정보 리스트 변형
    location= df['Latitude']
    #미세먼지 농도를 리스트 변형
    pm= df['PM2.5'].tolist()
    #첫 지점이 좌표가 0일 경우 다른 좌표로 변경
    for n in df.index:
            if location[n] !=0.0:
                Start=[df['Latitude'][n],df['Longitude'][n]]
                break
            else:
                continue
    #시작지점 좌표 출력 
    print('\n 시작지점')
    print(Start)
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
    
    #HTML에 사용될 미세먼지농도지표.jpg다운로드
    if os.path.isfile('지표.jpg'):
        print("\a 지표.jpg가 존재합니다")
    else:
        url='https://raw.githubusercontent.com/Pandemic23/FCV-ver1.3/main/%EC%A7%80%ED%91%9C.jpg'
        urllib.request.urlretrieve(url, '지표.jpg')
        print('\n 미세먼지농도지표.jpg 다운로드 완료')

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

    print('\n HTML파일생성이 완료 되었습니다')  
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
