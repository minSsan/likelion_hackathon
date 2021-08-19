# 멋쟁이 사자처럼 9기 해커톤 (2021.07.19 - 2021.08.13)

<img src="./hackathon/static/img/logo.png" width="200px" height="67px">

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

<br>
<br>

## 페이지 및 기능 소개 & 팀원 별 구현 부분
**1. 메인페이지** - 서비스 소개, 로그인 / 회원가입
  > **박민선**   
  > 메인페이지, 로그인, 회원가입 프론트<br>
  > <br>
  > **양재호**   
  > 로그인, 회원가입 기능<br>
  > <br>
  > **김송하**   
  > 로그인 프론트<br>
  > <br>
  > **최은선**  
  > 회원가입 프론트
<br>

**2. 팀빌딩 페이지** - 팀원 모집 게시글 열람 및 작성, 게시글 필터링 및 검색, 게시글 찜하기 기능
  > **박민선**   
  > 팀빌딩 페이지 프론트, 게시글 필터링 및 검색 기능, 게시글 찜 기능 <br>
  > >   _(필터링 버튼 누른 상태에서 검색기능을 이용할 시 기능이 작동되지 않는 버그가 있음<br>
  > >     -> 필터링은 POST 방식, 검색기능은 GET 방식을 사용하기 때문에 발생하는 버그임. 추후 수정 )_<br>
  > 
  > <br>
  > 
  > **양재호**   
  > 게시글 작성/수정 페이지 프론트, 게시글 작성/수정/삭제 기능
<br>

**3. 팀빌딩 상세 페이지** - 게시글 상세보기, 게시글 댓글 기능
  > **양재호**   
  > 게시글 상세페이지 프론트, 댓글 작성/수정/삭제 기능, 답글 작성/수정/삭제 기능
<br>

**4. 스카우트 페이지** - 유저 정보 열람, 유저 필터링 및 검색, 유저 채팅 기능, 유저 찜하기 기능
  > >   _paginator 버그(페이지 버튼을 클릭해도 넘어가지 않는 문제) 존재_
  > 
  > **박민선**
  > 스카우트 페이지 프론트, 유저 필터링 기능, 유저 찜 기능<br>
  > <br>
  > **양재호**
  > 유저 필터링 및 검색 기능, 유저 채팅 기능
<br>

**5. 마이 포트폴리오 페이지(= 스카우트 상세 페이지)** - 유저 프로필 정보, 포트폴리오 관리 기능
  > **박민선**   
  > 포트폴리오 페이지 프론트, 포트폴리오 작성/수정/삭제 기능, 포트폴리오 작성/수정 페이지 프론트
<br>

**6. 마이페이지** - My프로필, 작성 글/댓글 리스트, 찜한 글/유저 리스트 열람
  > **박민선**   
  > 작성 글/댓글 및 찜한 글/유저 리스트 불러오기<br>
  > <br>
  > **양재호**   
  > 마이페이지 프론트
