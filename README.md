# 멋쟁이 사자처럼 9기 해커톤 (2021.07.19 - 2021.08.13)

**기획** 
> 임연수[(깃허브)](https://github.com/ylim2548)<br>
> 최은선[(깃허브)](https://github.com/thisissilverline)

**UI/UX 디자인**
> 김송하[(깃허브)](https://github.com/kimsongha)

**로고 디자인**
> 임연수

**개발**
> 박민선[(깃허브)](https://github.com/minSsan) <br>
> 양재호[(깃허브)](https://github.com/Jae12ho)

<hr>

* 반응형 App View 는 지원하지 않습니다. 되도록 큰 화면에서 이용해주세요. <br>
원만한 CSS 적용을 위해 Chrome 사용을 권장합니다.

* ### 배포 페이지: http://themoa.kro.kr:8000/ 
  > <strong>(체험판 ID: cu | PASSWORD: cucucucu)</strong> <br>
  > 비로그인시 몇몇 서비스 이용에 제약이 있기 때문에, 모든 서비스 이용을 위해서는 로그인 접속을 권장합니다.

* ### 로컬 서버에서 실행하는 경우

  실행 전 터미널 창에서 아래 명령어들을 입력하여 설치를 진행해야 합니다. (장고 설치 과정은 생략) <br>
  프로젝트 폴더 내에 myvenv 라는 가상환경이 이미 존재하기 때문에, 클론하시면 가상환경은 별도로 설치하지 않으셔도 됩니다.
  
  ```
  pip install channels
  ```
  ```
  pip install django-multiselectfield
  ```
  ```
  pip install Pillow
  ```

> Intro
> -----
>  안녕하세요. 저희는 멋쟁이 사자처럼 9기 한양대학교 ERICA 캠퍼스 **'더 모아'** 입니다. <br>
>  이번 멋쟁이 사자처럼 9기 해커톤에서 **팀빌딩 서비스**로 대회에 참가하게 되었습니다. <br>
>  총 5명의 팀원끼리 약 한 달간 기획부터 디자인, 개발, 배포까지 진행했으며, 단기간에 작업이 이루어져 **몇몇 버그나 불안정한 부분이 있을 수 있음**을 알립니다. 
>  
> ## 서비스 소개 (더 모아 - The Moa)
> 
> 1. 사용자 니즈에 충실한 서비스
> 프로젝트를 함께할 팀원을 구하는 사람들에게 안성맞춤인 **팀빌딩 서비스**
> 
> 2. 깔끔한 디자인
> The Moa는 **Figma**와 **Adobe Photoshop**을 활용하여 **감각적인 로고와 기능들**이 한눈에 들어오는 UI 디자인을 선보입니다
> > UI/UX 디자인(Figma) <br>
> > https://www.figma.com/file/US0twIL0eeR6oRxeGc2XvD/%EB%A9%8B%EC%82%AC_%ED%95%B4%EC%BB%A4%ED%86%A4
> 
> 3. 이용 간편한 기능들
> > <strong>마이 포트폴리오</strong> <br>
>   개인 정보와 스마트 에디터를 활용한 포트폴리오 게시물을 관리하고 이를 다른 사용자에게 홍보할 수 있습니다
> >
> > <strong>팀빌딩</strong><br>
> >   당신이 프로젝트를 함께하고 싶은 팀원(개발자, 기획자, 디자니어, 편집자 등)을 구한다는 공고를 손쉽게 업로드하여 홍보 가능합니다
> >
> > <strong>스카우트</strong><br>
> >   더모아 사용자 프로필을 둘러보고 그 사람의 포트폴리오까지 확인할 수 있습니다<br>
> >   찜하기와 채팅 기능을 활용해 당신이 원하는 팀원을 스카우트할 수 있습니다
> >
> > <strong>채팅</strong><br>
> >   더모아에서 설정한 프로필을 통해 채팅으로 원하는 팀원과 연락을 이어갈 수 있습니다
> > 
> > <strong>검색 및 필터</strong><br>
> >   게시물과 팀원을 탐색하는 데 편리한 검색 기능과 필터 기능(지역, 포지션, 상태 등)이 구현됩니다
>
> ## 페이지 및 기능 소개
> **1. 메인페이지** - 서비스 소개, 로그인 / 회원가입
