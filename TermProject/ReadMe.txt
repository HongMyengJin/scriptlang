Data변수 - openApi에 가져온 값을 지역별로 저장해두는 용도
Lat, Lon, IsPublic, Name, Address, Manage, Number, OpenTime, indexData, GB_Check, G_Closet, B_Closet은 저장할 정보들을 저장할 리스트

[함수]
ImageLabel - 이미지를 그려주는 라벨
InitScreen - 처음 Screen을 실행할때 프레임을 만드는 초기값
SearchCity - openapi를 이용하여 url에 접속해 데이터를 가져와 해당 시/군 데이터만 가져오게 하는 함수
Check_Public - 공용 제작 체크 함수
Combox
MailButton - 메일 보내는 버튼 이벤트 처리
sendMail - 메일을 보내주는 함수
SearchListBox  - 시/군을 선택하기 위한 콤보 박스
Pressed - 지도를 출력해주는 함수

   (1)ComboChange
        콤보에 이벤트가 생겼을때 실행시켜주는 함수 - 해당 시/군으로 리스트 넣어주기

SearchButton - 검색 버튼
    (1)Search_Name
         이름을 검색했을때 실행시켜주는 함수 - 검색 필터링 실행

Checkbutton - 체크 버튼
Check_Public - 공용으로 쓰는지에 대한 

오류처리, 추가 구현: 즐겨찾기를 하였습니다.