# ssafy-final-pjt
## 나의 Play-list Selecting 파트너

- 최신 유행 영화 추천
- 유저가 리뷰한 영화를 기준으로 유사한 장르의 영화를 추천
- TMDB API로 영화 정보 실시간 업데이트

## 팀원
- 이승희 (프론트엔드 담당)
    - 백엔드 데이터를 받아와 프론트 엔드 기능 구현
    - 프론트엔드 컴포넌트 설계, 디자인

- 조재경 (백엔드 담당)
    - 백엔드 데이터베이스 모델링
    - API 설계, 개발

## 데이터베이스 모델링

![](./image/ERD.png)

## 컴포넌트 구조

![](./image/Component.png)

## 영화 추천 알고리즘

- 최신 유행 영화 추천
    - TMDB 기준 오늘 유행하는 영화 20개 추천

- 사용자 맞춤 영화 추천
    - 사용자가 많이 본 영화 장르에 기반해 추천
    1. 리뷰 작성한 영화를 기준으로 상위 장르들을 선정
    2. DB 내에서 유사 장르들의 영화를 선정
    3. 선정한 영화들의 평점을 기준으로 상위 20개 영화 추천

## 서비스 기능


## 느낀점
-이승희 : 항상 수업시간에 진행하던 관통 프로젝트와는 달리 주제만 주어지고, 원하는대로 개발하는 미션이 주어지니 어디에서부터 손을 대야할지 몰랐다. 다행히도 내가 아직 미숙한 분야인 백엔드를 같은 팀원이 맡아주었고, 서비스를 어떻게 구성할지에 대한 기획을 먼저 시작했다.
전체적으로 틀이 잡혀진 뒤에, 팀원은 필요한 DB 설계를 바로 시작했고, 나는 컴포넌트들을 구성하기 시작했다. 처음 다루는 GitHub Desktop 앱에 당황하는것도 잠시, 서로 작업하며 필요한 부분에대한 요청을 주고받다보니 DB설계가 어느정도 틀이 잡혔고, API를 받아와서 기능을 구현하고 필요한 기능을 추가로 API로 작성하는 과정을 거쳤다.
컴포넌트 구조와 기능 구현이 마무리되어갈 때 쯤, Vuetify를 사용하여 디자인을 시작했다.
CSS를 다루는 기술이 부족하여 처음에는 상당히 헤매었다. 가장 어려운 점은 Vuetify같은 프레임워크는 스타일들이 이미 매겨져있는 경우가 많았고, 그 스타일이 겉으로 보이지 않아 무엇이 문제여서 원하는대로 그려지지 않는지 알 수 없었다는 것이다. 다만 수많은 시도를 거쳐 하나, 둘 모습을 갖추어가는 프론트를 보며 박차를 가할 수 있었고, 마무리지어갈 때 쯤에는 어느정도 능숙하게 수정을 할 수 있게 되었다.
많은 개발자들이 개발 공부를 할 때, 문법 공부만 하는것 보다는 간단한 서비스라도 무작정 만들어보는게 도움이 된다는 말을 한다. 하지만 이전에는 그것도 어느정도 알아야 만들 수 있는것 아닌가? 라는 생각에 시도하지 않았었다.
하지만 이번 프로젝트 경험을 통해서 시작할때는 아무것도 모르는듯 했지만 끝날때는 다음 프로젝트를 어떻게 하면 좋을지 고민하고 있는 나를 발견할 수 있었다.
좋은 팀원과 함께 열정적으로 임할 수 있었기에 보람찬 프로젝트였다고 생각한다.
