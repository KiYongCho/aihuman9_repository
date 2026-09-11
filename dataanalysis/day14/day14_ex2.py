# day14_ex2.py
# plotly 인터렉티브 시각화, folium 지도 시각화

'''
* plotly
- 웹기반 인터렉티브 데이터 시각화 라이브러리
- 마우스를 올리면 데이터 값을 확인할 수 있음
- 확대, 축소, 이동, 범례 선택, 이미지 저장 ... 기능 제공
- plotly.express를 주로 사용

* folium
- 위도/경도를 이용한 지도 시각화 라이브러리
- Marker를 이용하여 지도에 데이터 위치 표시
- 결과를 HTML 파일로 저장하여 웹브라우져에서 확인하거나 웹서비스 가능
'''

# 설치 : Alt + F12 > pip install plotly folium

import pandas as pd
import plotly.express as px
import folium
import webbrowser
from pathlib import Path

# 결과 저장 폴더
output_dir = Path('day14_output')
output_dir.mkdir(exist_ok=True)

# 실습용 데이터프레임
df = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "광고비": [100, 120, 130, 150, 170, 200],
    "방문자수": [3000, 3500, 3800, 4200, 4700, 5300],
    "매출": [250, 290, 310, 360, 410, 480]
})
# df.info()

# plotly 선그래프
# fig = px.line(
#     df,
#     x = '월',
#     y = '매출',
#     markers = True, # 데이터 위치에 마커 표시
#     title = '월별 매출 추세'
# )
# fig.show()

# plotly 막대그래프
# fig = px.bar(
#     df,
#     x = '월',
#     y = '매출',
#     text = '매출', # 막대에 값 표시
#     title = '월별 매출'
# )
# fig.show()

# plotly 산점도
# fig = px.scatter(
#     df,
#     x = '광고비',
#     y = '매출',
#     size = '방문자수', # 점 크기 기준
#     hover_data = ['월'], # 마우스 오버시 표시할 컬럼
#     title = '광고비와 매출 관계'
# )
# fig.show()

# folium 지도 시각화

# folium Map 생성
# m = folium.Map(
#     location = [37.5665, 126.9780], # 맵의 중심위경도 (서울시청 위/경도)
#     zoom_start = 12 # 최초 로딩시 줌의 확대 레벨
# )
#
# map_file = output_dir/'map.html' # 맵을 HTML로 저장할 때 파일명
#
# m.save(map_file) # 맵을 HTML로 저장
#
# # 맵파일의 절대경로를 URI변환해서 웹브라우져에서 오픈
# webbrowser.open(map_file.resolve().as_uri())

# folium Marker : 맵에 마커 표시

m = folium.Map(
    location = [37.55, 126.98],
    zoom_start = 11
)

# 지명, 위도, 경도 리스트
location = [
    ['서울시청', 37.5665, 126.9780],
    ['강남역', 37.4979, 127.0276],
    ['홍대입구', 37.5572, 126.9254]
]

for name, lat, lon in location:
    folium.Marker( # Marker 생성
        location = [lat, lon], # 마커 위경도
        tooltip = name, # 마우스 올렸을때 보여줄 텍스트
        popup = name + ' 클릭함!' # 마우스 클릭했을때 보여줄 텍스트
    ).add_to(m) # 마커를 맵에 추가

map_file = output_dir/'marker_map.html'
m.save(map_file)

webbrowser.open(map_file.resolve().as_uri())



































