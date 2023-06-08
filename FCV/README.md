# FCV-ver1.5
Name: Fine dust Concentration Visualization

이 프로그램은 파이썬 map 시각화 라이브러리 Folium을 응용했습니다.
차량으로 측정한 미세먼지 농도 측정 데이터(.csv)를 통해 각 지점의 미세먼지 농도에 따라
색상을 달리하여 전라남도 미세 먼지 농도 측정에 도움을 주는 것을 지향하고 있습니다.

# packages

folium
pandas 
os
io
webbrowser
urllib.request

# 필요 데이터 파일


1.data.txt (미세먼지 측정데이터)
#텍스트 파일을 입력받아 자동으로 encoding.csv로 변환

2.지표.jpg
#이 파일은 꼭 F.C.V 생성된 html과 같은 경로에 위치하게 해야한다.

3.encoding.csv
#data.txt를 csv로 변환한 파일 folium 적용에 가능

# 1 사용법(첫 실행으로 encoding.csv 파일이 존재하지 않을때)

1. 실행시 data.txt 경로를 정확히 입력해줍니다.
-txt는 자동적으로csv로 변환되어 encoding.csv저장됩니다
저장된 encoding.csv 파일 경로를 입력받아 첫번째 측정 지점을 자동적으로 찾아 시작지점으로 지정되며 출력됩니다.

2. 데이터 분류 및 시각화가 끝난 파일의 이름을 입력합니다.
-저장된 경로와 파일 이름이 다시 출력되며 자동실행합니다.
# 2 사용법(새로운 데이터로 실행하고 싶을 때 이전 encoding.csv 파일이 존재할 경우)

1. 이전 encoding.csv를 삭제하거나 이름을 변경합니다.
-새로운 데이터와의 충돌을 피하기 위해서 encoding.csv 같은 이름의 파일이 존재하면 안됨
2. # 1 사용법과 같다 

*PATH(1.4->1.5)*

ver 1.2
-사용자가 직접 데이터 파일의 경로를 입력하여 고른 데이터 파일에 따른 
관측 시작지점(제일 먼저 측정된 좌표 기준)자동 설정,데이터 시각화 파일(*html)의 저장경로 확인 
이름 변경이 가능해졌다.  
ver 1.3
-미세먼지 농도 지표 이미지 객체 자동 생성
-마우스 위치에 따른 위도 경도 실시간 표츌
ver 1.3
-지표.jpg 파일 유무에 따라 다운로드 실행
ver 1.4
-데이터 csv 변환에 난관
-데이터 파일의 형식이 csv에 한해서만이 아닌 txt 파일도 가능하게 연구
ver 1.5
-txt_to_csv 알고리즘 추가
-encoding.csv 파일 유무에 따라 txt파일 경로 입력을 받습니다.