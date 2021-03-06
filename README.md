# 집단감염지 출신 확진자 정보 시각화 서비스

## 프로젝트 개요
<p> 본 서비스를 이용하면, 집단감염지 출신 확진자 정보를 지도를 통해 한 눈에 확인할 수 있으며, 코로나 시작 시점부터 6월까지의 집단감염지 출신 확진자 발생 추이를 확인할 수 있다.</p>

## 프로젝트 의의
<p>  본 서비스는 집단감염지 출신 확진자 정보를 효율적으로 보여줌과 동시에 코로나 바이러스 집단감염에 대한 경각심을 심어줄 수 있다. </p>

## 주요 기능
<ul>
  <li>현재 위치의 위도와 경도를 입력하면, 현재 위치 주변의 집단감염지 출신 확진자 정보를 표시해준다.</li>
  <li>발생추이맵을 히트맵으로 구현해서, 집단감염지 출신 확진자 발생 추이를 한 눈에 쉽게 확인할 수 있다.</li>
</ul> 

## 기술 스택
<ul>
  <li>백엔드 -> Django</li>
  <li>지도제작 -> Folium, Numpy, Pandas, GeoPandas</li>
  <li>프론트엔드 -> HTML, JavaScript, CSS</li>
</ul> 

## 프로젝트 프로세스
Folium, Numpy, Pandas, GeoPandas 라이브러리를 적극 활용해서, 집단감염지 출신 확진자 맵과 발생추이 히트맵을 제작했다.
이후, django project 생성 후, views에서 Template에서 form으로 받아온 위도, 경도 정보를 바탕으로 자신의 위치를 zoom-in시켜 주변 확진자 정보를 볼 수 있게 구성했다.
초기 화면에서 오른쪽 버튼을 클릭하면, 발생추이 히트맵을 출력할 수 있게끔 views에서 template를 Render했다.

## 프로젝트 평가
<ul>
  <li>실시간으로 데이터를 가져올 수 있는 API가 없어서, 사용자에게 최신정보까지 제공할 수 없었다.</li>
  <li>디자인 문제 : 템플릿 디자인이 썩 좋지 않았다. </li>
  <li>SQlite3와 views를 더 잘 활용했다면, 동적으로 서비스를 구성할 수 있었는데 그 부분이 부족했다. </li>
</ul> 
