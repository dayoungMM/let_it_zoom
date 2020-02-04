# github 사용법

- repository 공유하기

  1. 1 사람이 repository를 만들고 collaborator를 추가한다.

  2. 추가된 사람들은 github에 가입한 이메일로 전송된 이메일을 누른다.

     그러면 이제 repository 공유됨!



- branch 만들기
  1. `git switch -c [내이름]` 으로 나만의 branch 만들고 이동하기



- 매일 아침에 할 일
  1. `git pull origin master`로 master의 내용을 pull 받는다.
  2. 작업 시작! 작업 중/ 작업 후에는 아래 코스를 따른다.



-  작업 중

  1. 항상! 기존의 틀은 만지지 말고, [내이름]_[파일명]으로 나만 건드릴 파일을 만들어서 사용한다.

     ex) minjung_views, minjung_url, minjung_setting

     *내가 만든 파일이 기존 파일과 겹쳐서 충돌이 일어날 수 있습니다. 그럴 땐 기존 파일(틀)을 배경화면에 빼놓고 작업한 다음 최종 push전에 다시 넣어서 push 합니다.

  2. 언제나 구글 독스에 내가 만진 파일의 명 ([내이름]_[파일명]) 을 공유한다.

     *사소하게 고친 것도 전부 공유해주세요!



-  작업 후

  1. 하루동안 코딩을 하면서 `git push origin [내이름]` 으로 내 branch에만 push 한다.

     *master에 push하지 말기!

  2. 하루 작업이 끝나면 2번을 해서 push 하고 구글 독스에 작업한 내용을 정리해서 공유까지 한다.

  3. 마지막으로 github에서 merge 요청까지 하면 하루 일과 끝!



- github 관리자

  1. github 관리자 (고민정)만 master branch를 사용합니다.

  2. 모두가 push를 끝내면 merge와 코드 합병을 진행합니다.

     다음날 모두가 pull 받아서 사용할 수 있는 형태로 완성해둡니다.



- Django 틀 만드는 사람

  1. Django의 틀을 만듭니다.
  2. `git clone [repository 주소]`로 clone 합니다.

  3. `git push origin master`로 틀을 master에 넣습니다.