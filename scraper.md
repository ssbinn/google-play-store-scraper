#### 웹 크롤러와 스크래퍼
웹 크롤러는 자동화된 방법으로 여러 사이트를 직접 돌아다니면서 데이터를 가지고 오는 봇 <br>
웹 스크래퍼는 특정 웹 사이트 또는 페이지에서 특정 데이터를 추출하여 새로운 것을 만드는 작업을 말한다. (ex. 어플의 **앱 이름, 앱 정보, 별점, 다운로드 수**와 같은 원하는 정보를 가져오는 작업)

#### 플레이스토어 분석
분석하려는 [플레이스토어](https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=ko&gl=US)는 처음 웹사이트를 새로고침 했을 때 모든 정보를 보여주지 않고, 아래로 스크롤 하면 로딩 후에 어플을 보여준다.
또한 javascript 코드가 들어간 동적 웹이라서 beautifulSoup, selenium 모두 사용해야 하고, 플레이 스토어에서 일부 어플만 노출시켰기 때문에 최종적으로 스크래핑할 어플의 갯수는 얼마 되지 않는다.

#### header
header를 작성했는데 구글은 접속하는 유저의 header 정보에 따라 다른 정보를 보여주기 때문에 꼭 작성해주어야 한다. <br>
만약 작성하지 않는다면 requests를 통해서 플레이스토어에 접근할 때, 미국에서 접속한 것을 디폴트로 해서 보여주기 때문에 원하지 않는 정보가 출력될 수 있다. <br>
header를 잘 작성하여 원하는 사이트에 맞게 접속했는 지 확인하기 위해 아래의 코드로 확인해보았다.

```python
with open("app.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify()) 
```

#### webdriver 설치 방법 (크롬 드라이버 설치 방법)
- [크롬 버전 확인](chrome://version/)
- [크롬 드라이버 설치](https://chromedriver.chromium.org/downloads )
  - 크롬 버전과 맞춰서 설치해야 하고, exe 파일을 작업하고 있는 파일과 같은 경로에 압축을 풀어야 한다. 

#### user agent 정보 확인 방법
- user agent string 검색하면, `what is my user agent?` 사이트에서 자신의 user agent 정보 확인 가능 
- 접속하는 브라우저에 따라 다르게 나오기 때문에 주의 (크롬 사용)
