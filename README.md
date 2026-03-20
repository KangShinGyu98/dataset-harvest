# Dataset Harvester

여러 공개 데이터 소스에서 데이터셋 목록을 자동으로 수집해 `domain, dataset_name, link, source` 형식의 CSV로 저장하는 도구이자 결과물입니다.

---

## 문제 정의

데이터셋을 찾는 과정에는 두 가지 불편함이 있습니다.

1. **사이트가 너무 많고 UI가 제각각이다** — 처음 보는 사이트는 어디서부터 봐야 할지 감이 잡히지 않는다.
2. **대부분의 추천 글은 링크 나열에 그친다** — "이 사이트 가봐라"는 정보만 있고, 실제로 어떤 데이터가 있는지, 얼마나 되는지는 직접 들어가야 알 수 있다.

이 프로젝트는 주요 소스를 자동으로 크롤링해서 데이터셋 목록을 한 곳에 모아줍니다.

---

## 목차

- [문제 정의](#문제-정의)
- [파일 구조](#파일-구조)
- [데이터 소스](#데이터-소스)
- [빠른 시작](#빠른-시작)
- [.env 설정](#env-설정)
- [결과물 Domain별 총3341개](#결과물-domain별-총3341개)

---

## 파일 구조

```
dataset-harvester/
├── scripts/
│   └── harvest.py          # 메인 수집 스크립트
├── config/
│   ├── targets.yaml         # 수집 대상 소스 목록
│   └── domain_overrides.csv # 도메인 레이블 수동 보정
├── output/
│   ├── datasets_by_source.csv
│   └── datasets_by_domain.csv
├── logs/
│   └── harvest.jsonl
├── requirements.txt
├── .env.example
└── README.md
```

---

## 데이터 소스

수집 대상 사이트 목록입니다.

- [Our World in Data — Explorers](https://ourworldindata.org/explorers)
- [Our World in Data — All Topics](https://ourworldindata.org/#all-topics)
- [FiveThirtyEight — index.csv](https://github.com/fivethirtyeight/data/blob/master/index.csv)
- **Kaggle** — [투표순 상위 100페이지 (약 2,000개)](https://www.kaggle.com/datasets?sort=votes)
- [UCI ML Repository](https://archive.ics.uci.edu/datasets?skip=25&take=25&sort=desc&orderBy=NumHits&search=)
- [OpenML](https://www.openml.org/search?type=data&sort=runs&status=active)
- [AWS Open Data Registry](https://registry.opendata.aws/)
- [World Bank Data360](https://data360.worldbank.org/en/search)
- [WSDM 2026 Competition](https://wsdm-conference.org/2026/)

---

## 빠른 시작

```bash
# 직접 실행하지 마시고 output 폴더에 csv 파일을 다운로드 받으시기를 권장드립니다.
# 1. 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate          # Windows Git Bash: source .venv/Scripts/activate

# 2. 의존성 설치
pip install -r requirements.txt

# 3. .env 파일 설정 (아래 섹션 참고)
cp .env.example .env

# 4. 수집 실행
python scripts/harvest.py --targets config/targets.yaml --out output/datasets_by_source.csv
```

일부 소스가 실패해도 나머지는 계속 수집하려면 `--allow-partial` 옵션을 추가하세요.

```bash
python scripts/harvest.py --targets config/targets.yaml --out output/datasets_by_source.csv --allow-partial
```

---

## .env 설정

`.env.example`을 복사해 `.env`로 만든 뒤, 아래 항목을 채워넣으세요.

```bash
cp .env.example .env
```

| 변수 | 필수 여부 | 설명 |
|------|-----------|------|
| `KAGGLE_USERNAME` | **필수** | Kaggle 계정 아이디 |
| `KAGGLE_KEY` | **필수** | Kaggle API 키 ([발급 방법](https://www.kaggle.com/settings/account)) |
| `OPENAI_API_KEY` | 선택 | 자동화 보조 기능 사용 시 필요 |
| `HARVEST_INTERVAL_SECONDS` | 선택 | 반복 실행 간격 (기본값: 300초) |
| `HARVEST_KAGGLE_PAGES` | 선택 | Kaggle 수집 페이지 수 (기본값: 100) |

Kaggle 키는 환경변수 대신 `~/.kaggle/kaggle.json`에 넣어도 됩니다.

```json
{"username": "your_username", "key": "your_key"}
```

Kaggle 인증 정보가 없으면 수집이 오류와 함께 종료됩니다. `--allow-partial`을 사용하면 Kaggle만 건너뛰고 나머지 소스는 계속 수집합니다.

---
## 결과물 Domain별 총3341개

### others (총 911개)

| dataset_name | source | link |
|---|---|---|
| avengers | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/avengers) |
| bachelorette | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/bachelorette) |
| bob-ross | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/bob-ross) |
| classic-rock | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/classic-rock) |
| fifa | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/fifa) |
| fight-songs | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/fight-songs) |
| food-world-cup | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/food-world-cup) |
| love-actually | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/love-actually) |
| march-madness-predictions | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/march-madness-predictions) |
| march-madness-predictions-2015 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/march-madness-predictions-2015) |
| march-madness-predictions-2018 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/march-madness-predictions-2018) |
| mlb-allstar-teams | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/mlb-allstar-teams) |
| mlb-elo | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/mlb-elo) |
| mlb-quasi-win-shares | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/mlb-quasi-win-shares) |
| nba-draft-2015 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nba-draft-2015) |
| nba-draymond | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nba-draymond) |
| nba-elo | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nba-elo) |
| nba-forecasts | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nba-forecasts) |
| nba-raptor | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nba-raptor) |
| nba-tattoos | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nba-tattoos) |
| nba-winprobs | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nba-winprobs) |
| ncaa-womens-basketball-tournament | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/ncaa-womens-basketball-tournament) |
| nfl-elo | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nfl-elo) |
| nfl-fandom | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nfl-fandom) |
| nfl-favorite-team | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nfl-favorite-team) |
| nfl-suspensions | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nfl-suspensions) |
| nfl-ticket-prices | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nfl-ticket-prices) |
| nfl-wide-receivers | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nfl-wide-receivers) |
| nhl-forecasts | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nhl-forecasts) |
| star-wars-survey | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/star-wars-survey) |
| tarantino | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/tarantino) |
| tennis-time | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/tennis-time) |
| womens-world-cup-2019 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/womens-world-cup-2019) |
| womens-world-cup-predictions | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/womens-world-cup-predictions) |
| world-cup-2018 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/world-cup-2018) |
| world-cup-2022 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/world-cup-2022) |
| world-cup-comparisons | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/world-cup-comparisons) |
| world-cup-predictions | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/world-cup-predictions) |
| (LoL) League of Legends Ranked Games | kaggle | [바로가기](https://www.kaggle.com/datasets/datasnaek/league-of-legends) |
| (MBTI) Myers-Briggs Personality Type Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/datasnaek/mbti-type) |
| 1 million Sudoku games | kaggle | [바로가기](https://www.kaggle.com/datasets/bryanpark/sudoku) |
| 10 Monkey Species | kaggle | [바로가기](https://www.kaggle.com/datasets/slothkong/10-monkey-species) |
| 100,000 UK Used Car Data set | kaggle | [바로가기](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes) |
| 1000 Netflix Shows | kaggle | [바로가기](https://www.kaggle.com/datasets/chasewillden/netflix-shows) |
| 120 years of Olympic history: athletes and results | kaggle | [바로가기](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) |
| 17K Mobile Strategy Games | kaggle | [바로가기](https://www.kaggle.com/datasets/tristan581/17k-apple-app-store-strategy-games) |
| 2015 Flight Delays and Cancellations | kaggle | [바로가기](https://www.kaggle.com/datasets/usdot/flight-delays) |
| 2016 Parties in New York | kaggle | [바로가기](https://www.kaggle.com/datasets/somesnm/partynyc) |
| 2021 Olympics in Tokyo | kaggle | [바로가기](https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo) |
| 2021-2022 Football Player Stats | kaggle | [바로가기](https://www.kaggle.com/datasets/vivovinco/20212022-football-player-stats) |
| 2021-2022 NBA Player Stats | kaggle | [바로가기](https://www.kaggle.com/datasets/vivovinco/nba-player-stats) |
| 2022-2023 Football Player Stats | kaggle | [바로가기](https://www.kaggle.com/datasets/vivovinco/20222023-football-player-stats) |
| 2024 Amazon Best Sellers: Top Valentine Gifts | kaggle | [바로가기](https://www.kaggle.com/datasets/kanchana1990/2024-amazon-best-sellers-top-valentine-gifts) |
| 20M Rows Fake Turkish Names and Address Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/omercolakoglu/10m-rows-fake-turkish-names-and-address-dataset) |
| 30000 Spotify Songs | kaggle | [바로가기](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs) |
| 350 000+ movies from themoviedb.org | kaggle | [바로가기](https://www.kaggle.com/datasets/stephanerappeneau/350-000-movies-from-themoviedborg) |
| 60k-data-with-context-v2 | kaggle | [바로가기](https://www.kaggle.com/datasets/cdeotte/60k-data-with-context-v2) |
| 7,000 Labeled Pokemon | kaggle | [바로가기](https://www.kaggle.com/datasets/lantian773030/pokemonclassification) |
| 80 Cereals | kaggle | [바로가기](https://www.kaggle.com/datasets/crawford/80-cereals) |
| A/B test data | kaggle | [바로가기](https://www.kaggle.com/datasets/sergylog/ab-test-data) |
| Abalone Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) |
| Abstract Art Gallery | kaggle | [바로가기](https://www.kaggle.com/datasets/bryanb/abstract-art-gallery) |
| Advertising Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ashydv/advertising-dataset) |
| Age dataset: life, work, and death of 1.22M people | kaggle | [바로가기](https://www.kaggle.com/datasets/imoore/age-dataset) |
| AI Developer Productivity Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/atharvasoundankar/ai-developer-productivity-dataset) |
| Air pressure system failures in Scania trucks | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/aps-failure-at-scania-trucks-data-set) |
| Airline Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/airline-dataset) |
| Airline Delay and Cancellation Data, 2009 - 2018 | kaggle | [바로가기](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018) |
| Airline Delays | kaggle | [바로가기](https://www.kaggle.com/datasets/eugeniyosetrov/airline-delays) |
| Airline Passenger Satisfaction | kaggle | [바로가기](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction) |
| Airlines Dataset to predict a delay | kaggle | [바로가기](https://www.kaggle.com/datasets/jimschacko/airlines-dataset-to-predict-a-delay) |
| Airlines Delay | kaggle | [바로가기](https://www.kaggle.com/datasets/giovamata/airlinedelaycauses) |
| Airlines Flights Data | kaggle | [바로가기](https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data) |
| Airplane Crash Data Since 1908 | kaggle | [바로가기](https://www.kaggle.com/datasets/cgurkan/airplane-crash-data-since-1908) |
| Airplane Crashes Since 1908 | kaggle | [바로가기](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908) |
| AISegment.com - Matting Human Datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/laurentmih/aisegmentcom-matting-human-datasets) |
| Alcohol Effects On Study | kaggle | [바로가기](https://www.kaggle.com/datasets/whenamancodes/alcohol-effects-on-study) |
| Amazon - Ratings (Beauty Products) | kaggle | [바로가기](https://www.kaggle.com/datasets/skillsmuggler/amazon-ratings) |
| Amazon Kindle Books Dataset 2023 (130K Books) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/amazon-kindle-books-dataset-2023-130k-books) |
| Amazon Prime Movies and TV Shows | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows) |
| Amazon Products Dataset 2023 (1.4M Products) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products) |
| Amazon Seller - Order Status Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/pranalibose/amazon-seller-order-status-prediction) |
| Amazon Top 50 Bestselling Books 2009 - 2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019) |
| Amazon UK Products Dataset 2023 (2.2M Products) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/amazon-uk-products-dataset-2023) |
| AMEX data - integer dtypes - parquet format | kaggle | [바로가기](https://www.kaggle.com/datasets/raddar/amex-data-integer-dtypes-parquet-format) |
| An Open Dataset for Human Activity Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/sasanj/human-activity-smart-devices) |
| Analytical Base Table Churn | kaggle | [바로가기](https://www.kaggle.com/datasets/teocalvo/analytical-base-table-churn) |
| Androgen Receptor ChIP-seq Peaks | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/beneficiary-schemes-for-indian-women) |
| Android smartphones high accuracy GNSS datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/google/android-smartphones-high-accuracy-datasets) |
| Animal Care | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/animal-care) |
| Animal Crossing New Horizons Catalog | kaggle | [바로가기](https://www.kaggle.com/datasets/jessicali9530/animal-crossing-new-horizons-nookplaza-dataset) |
| Animals-10 | kaggle | [바로가기](https://www.kaggle.com/datasets/alessiocorrado99/animals10) |
| Anime Dataset 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset) |
| Anime Recommendations Database | kaggle | [바로가기](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database) |
| Anime Sketch Colorization Pair | kaggle | [바로가기](https://www.kaggle.com/datasets/ktaebum/anime-sketch-colorization-pair) |
| Anxiety and Depression Psychological Therapies | kaggle | [바로가기](https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadsanxietycsv) |
| Apartment rental offers in Germany | kaggle | [바로가기](https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany) |
| Apple Quality | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality) |
| Aq SolDB: A curated aqueous solubility dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sorkun/aqsoldb-a-curated-aqueous-solubility-dataset) |
| ar Xiv Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/Cornell-University/arxiv) |
| Articles sharing and reading from CI and T Desk Drop | kaggle | [바로가기](https://www.kaggle.com/datasets/gspmoreira/articles-sharing-reading-from-cit-deskdrop) |
| Artificial Lunar Landscape Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/romainpessia/artificial-lunar-rocky-landscape-dataset) |
| ASL Alphabet | kaggle | [바로가기](https://www.kaggle.com/datasets/grassknoted/asl-alphabet) |
| Association of Tennis Professionals Matches | kaggle | [바로가기](https://www.kaggle.com/datasets/gmadevs/atp-matches-dataset) |
| Asteroid Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset) |
| ATP Men's Tour | kaggle | [바로가기](https://www.kaggle.com/datasets/jordangoblet/atp-tour-20002016) |
| Audio Cats and Dogs | kaggle | [바로가기](https://www.kaggle.com/datasets/mmoreaux/audio-cats-and-dogs) |
| Austin Animal Center Shelter Outcomes | kaggle | [바로가기](https://www.kaggle.com/datasets/aaronschlegel/austin-animal-center-shelter-outcomes-and) |
| Australian Football League (AFL) Database | kaggle | [바로가기](https://www.kaggle.com/datasets/stoney71/aflstats) |
| Autism Screening | kaggle | [바로가기](https://www.kaggle.com/datasets/faizunnabi/autism-screening) |
| Autism screening data for toddlers | kaggle | [바로가기](https://www.kaggle.com/datasets/fabdelja/autism-screening-for-toddlers) |
| Auto-mpg dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/autompg-dataset) |
| autodownloaded | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/autodownloaded) |
| Automobile Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/toramky/automobile-dataset) |
| AutoXGB | kaggle | [바로가기](https://www.kaggle.com/datasets/abhishek/autoxgb) |
| Barcelona data sets | kaggle | [바로가기](https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets) |
| Baseball Databank | kaggle | [바로가기](https://www.kaggle.com/datasets/open-source-sports/baseball-databank) |
| Beat The Bookie: Odds Series Football Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/austro/beat-the-bookie-worldwide-football-dataset) |
| Bee or wasp? | kaggle | [바로가기](https://www.kaggle.com/datasets/jerzydziewierz/bee-vs-wasp) |
| Beer Consumption - Sao Paulo | kaggle | [바로가기](https://www.kaggle.com/datasets/dongeorge/beer-consumption-sao-paulo) |
| beginner_datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/ahmettezcantekin/beginner-datasets) |
| Behavioral Risk Factor Surveillance System | kaggle | [바로가기](https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system) |
| bert base uncased | kaggle | [바로가기](https://www.kaggle.com/datasets/abhishek/bert-base-uncased) |
| Best Artworks of All Time | kaggle | [바로가기](https://www.kaggle.com/datasets/ikarus777/best-artworks-of-all-time) |
| best-selling-books | kaggle | [바로가기](https://www.kaggle.com/datasets/drahulsingh/best-selling-books) |
| Big Basket Entire Product List (28K datapoints) | kaggle | [바로가기](https://www.kaggle.com/datasets/surajjha101/bigbasket-entire-product-list-28k-datapoints) |
| Big Data Certification KR | kaggle | [바로가기](https://www.kaggle.com/datasets/agileteam/bigdatacertificationkr) |
| Big Five Personality Test | kaggle | [바로가기](https://www.kaggle.com/datasets/tunguz/big-five-personality-test) |
| Bike Sharing in Washington D.C. Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/marklvl/bike-sharing-dataset) |
| Bike Store Relational Database SQL | kaggle | [바로가기](https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database) |
| Billboard "The Hot 100" Songs | kaggle | [바로가기](https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs) |
| Binance Full History | kaggle | [바로가기](https://www.kaggle.com/datasets/jorijnsmit/binance-full-history) |
| Biomechanical features of orthopedic patients | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/biomechanical-features-of-orthopedic-patients) |
| Black Friday | kaggle | [바로가기](https://www.kaggle.com/datasets/sdolezel/black-friday) |
| Board Game Data | kaggle | [바로가기](https://www.kaggle.com/datasets/mrpantherson/board-game-data) |
| Board Games | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/board-games) |
| Board Games Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/gabrio/board-games-dataset) |
| Boat types recognition | kaggle | [바로가기](https://www.kaggle.com/datasets/clorichel/boat-types-recognition) |
| Body Fat Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset) |
| Body performance Data | kaggle | [바로가기](https://www.kaggle.com/datasets/kukuroo3/body-performance-data) |
| Books Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset) |
| Border Crossing Entry Data | kaggle | [바로가기](https://www.kaggle.com/datasets/akhilv11/border-crossing-entry-data) |
| BRaTS 2021 Task 1 Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1) |
| BraTS2020 Dataset (Training + Validation) | kaggle | [바로가기](https://www.kaggle.com/datasets/awsaf49/brats20-dataset-training-validation) |
| Brazilian Cities | kaggle | [바로가기](https://www.kaggle.com/datasets/crisparada/brazilian-cities) |
| Brazilian E-Commerce Public Dataset by Olist | kaggle | [바로가기](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| Break His | kaggle | [바로가기](https://www.kaggle.com/datasets/ambarish/breakhis) |
| Brewer's Friend Beer Recipes | kaggle | [바로가기](https://www.kaggle.com/datasets/jtrofe/beer-recipes) |
| Brian Tumor Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/preetviradiya/brian-tumor-dataset) |
| British Birdsong Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/british-birdsong-dataset) |
| CalCOFI | kaggle | [바로가기](https://www.kaggle.com/datasets/sohier/calcofi) |
| California Traffic Collision Data from SWITRS | kaggle | [바로가기](https://www.kaggle.com/datasets/alexgude/california-traffic-collision-data-from-switrs) |
| Campeonato Brasileiro de futebol | kaggle | [바로가기](https://www.kaggle.com/datasets/adaoduque/campeonato-brasileiro-de-futebol) |
| Campus Recruitment | kaggle | [바로가기](https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement) |
| Cannabis Strains | kaggle | [바로가기](https://www.kaggle.com/datasets/kingburrito666/cannabis-strains) |
| Car Evaluation Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/elikplim/car-evaluation-data-set) |
| Car Features and MSRP | kaggle | [바로가기](https://www.kaggle.com/datasets/CooperUnion/cardataset) |
| Car information dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tawfikelmetwally/automobile-dataset) |
| Car Sale Advertisements | kaggle | [바로가기](https://www.kaggle.com/datasets/antfarol/car-sale-advertisements) |
| Cardio Good Fitness | kaggle | [바로가기](https://www.kaggle.com/datasets/saurav9786/cardiogoodfitness) |
| Cars Datasets (2025) | kaggle | [바로가기](https://www.kaggle.com/datasets/abdulmalik1518/cars-datasets-2025) |
| casia dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sophatvathana/casia-dataset) |
| Cat and Dog | kaggle | [바로가기](https://www.kaggle.com/datasets/tongpython/cat-and-dog) |
| Cat and Dogs | kaggle | [바로가기](https://www.kaggle.com/datasets/d4rklucif3r/cat-and-dogs) |
| Cat Breeds Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ma7555/cat-breeds-dataset) |
| Cat Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/crawford/cat-dataset) |
| cataract dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jr2ngb/cataractdataset) |
| Cats and Dogs | kaggle | [바로가기](https://www.kaggle.com/datasets/marquis03/cats-and-dogs) |
| Cats-vs-Dogs | kaggle | [바로가기](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset) |
| Cause of Deaths around the World (Historical Data) | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/cause-of-deaths-around-the-world) |
| Causes of Death in Indonesia | kaggle | [바로가기](https://www.kaggle.com/datasets/hendratno/cause-of-death-in-indonesia) |
| CDC Data: Nutrition, Physical Activity, and Obesity | kaggle | [바로가기](https://www.kaggle.com/datasets/spittman1248/cdc-data-nutrition-physical-activity-obesity) |
| CERN Electron Collision Data | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/cern-electron-collision-data) |
| Chai Time Data Science CTDS.Show | kaggle | [바로가기](https://www.kaggle.com/datasets/rohanrao/chai-time-data-science) |
| Chatbot dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/niraliivaghani/chatbot-dataset) |
| Chatbots: Intent Recognition Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/elvinagammed/chatbots-intent-recognition-dataset) |
| Chess Game Dataset (Lichess) | kaggle | [바로가기](https://www.kaggle.com/datasets/datasnaek/chess) |
| Chess Positions | kaggle | [바로가기](https://www.kaggle.com/datasets/koryakinp/chess-positions) |
| Chest X-rays (Indiana University) | kaggle | [바로가기](https://www.kaggle.com/datasets/raddar/chest-xrays-indiana-university) |
| Chicago Divvy Bicycle Sharing Data | kaggle | [바로가기](https://www.kaggle.com/datasets/yingwurenjian/chicago-divvy-bicycle-sharing-data) |
| Chicago Taxi Trips | kaggle | [바로가기](https://www.kaggle.com/datasets/chicago/chicago-taxi-trips-bq) |
| Child Malnutrition - UNICEF Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/child-malnutrition-unicef-dataset) |
| ChIP-seq data for the histone H3 - H3K27ac | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/corruption-in-india) |
| Chocolate Bar Ratings | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/chocolate-bar-ratings) |
| Chronic illness: symptoms, treatments and triggers | kaggle | [바로가기](https://www.kaggle.com/datasets/flaredown/flaredown-autoimmune-symptom-tracker) |
| Churn in Telecom's dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/becksddf/churn-in-telecoms-dataset) |
| Churn Modelling | kaggle | [바로가기](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling) |
| Churn Modelling | kaggle | [바로가기](https://www.kaggle.com/datasets/shubh0799/churn-modelling) |
| CIFAR-10 Python | kaggle | [바로가기](https://www.kaggle.com/datasets/pankrzysiu/cifar10-python) |
| CIFAR-100 Python | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/cifar100) |
| Cirrhosis Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/cirrhosis-prediction-dataset) |
| CKPLUS | kaggle | [바로가기](https://www.kaggle.com/datasets/shawon10/ckplus) |
| Classified Ads for Cars | kaggle | [바로가기](https://www.kaggle.com/datasets/mirosval/personal-cars-classifieds) |
| Classify gestures by reading muscle activity | kaggle | [바로가기](https://www.kaggle.com/datasets/kyr7plus/emg-4) |
| Clothing dataset (full, high resolution) | kaggle | [바로가기](https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full) |
| Clubhouse Dataset 9.7M | kaggle | [바로가기](https://www.kaggle.com/datasets/johntukey/clubhouse-dataset) |
| COCO 2017 Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/awsaf49/coco-2017-dataset) |
| coco128 | kaggle | [바로가기](https://www.kaggle.com/datasets/ultralytics/coco128) |
| Coffee dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/michals22/coffee-dataset) |
| Coffee Quality Data (CQI May-2023) | kaggle | [바로가기](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi) |
| Coffee Quality database from CQI | kaggle | [바로가기](https://www.kaggle.com/datasets/volpatto/coffee-quality-database-from-cqi) |
| Coffee shop sample data (11.1.3+) | kaggle | [바로가기](https://www.kaggle.com/datasets/ylchang/coffee-shop-sample-data-1113) |
| College Basketball Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewsundberg/college-basketball-dataset) |
| College Football Team Stats Seasons 2013 to 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/jeffgallini/college-football-team-stats-2019) |
| Common Password List (rockyou.txt) | kaggle | [바로가기](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt) |
| Common Voice | kaggle | [바로가기](https://www.kaggle.com/datasets/mozillaorg/common-voice) |
| Complete Cryptocurrency Market History | kaggle | [바로가기](https://www.kaggle.com/datasets/taniaj/cryptocurrency-market-history-coinmarketcap) |
| Complete FIFA 2017 Player dataset (Global) | kaggle | [바로가기](https://www.kaggle.com/datasets/artimous/complete-fifa-2017-player-dataset-global) |
| Complete Kaggle Datasets Collection | kaggle | [바로가기](https://www.kaggle.com/datasets/jessevent/all-kaggle-datasets) |
| Complete Pokemon Dataset (Updated 16.04.21) | kaggle | [바로가기](https://www.kaggle.com/datasets/mariotormo/complete-pokemon-dataset-updated-090420) |
| Computer Network Traffic | kaggle | [바로가기](https://www.kaggle.com/datasets/crawford/computer-network-traffic) |
| Computer Parts (CPUs and GPUs) | kaggle | [바로가기](https://www.kaggle.com/datasets/iliassekkaf/computerparts) |
| Cosmetics datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets) |
| Cost of Living | kaggle | [바로가기](https://www.kaggle.com/datasets/stephenofarrell/cost-of-living) |
| Cost of Living Index by Country | kaggle | [바로가기](https://www.kaggle.com/datasets/myrios/cost-of-living-index-by-country-by-number-2024) |
| Cost Prediction on acquiring Customers | kaggle | [바로가기](https://www.kaggle.com/datasets/ramjasmaurya/medias-cost-prediction-in-foodmart) |
| Countries of the World | kaggle | [바로가기](https://www.kaggle.com/datasets/fernandol/countries-of-the-world) |
| Coursera Course Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/siddharthm1698/coursera-course-dataset) |
| COVIDx CT | kaggle | [바로가기](https://www.kaggle.com/datasets/hgunraj/covidxct) |
| COVIDx CXR-4 | kaggle | [바로가기](https://www.kaggle.com/datasets/andyczhao/covidx-cxr2) |
| Crab Age Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/sidhus/crab-age-prediction) |
| Craft Beers Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/nickhould/craft-cans) |
| CREMA-D | kaggle | [바로가기](https://www.kaggle.com/datasets/ejlok1/cremad) |
| Cricket data | kaggle | [바로가기](https://www.kaggle.com/datasets/mahendran1/icc-cricket) |
| Crimes in Boston | kaggle | [바로가기](https://www.kaggle.com/datasets/AnalyzeBoston/crimes-in-boston) |
| Crimes in Chicago | kaggle | [바로가기](https://www.kaggle.com/datasets/currie32/crimes-in-chicago) |
| Cristiano Ronaldo All Club Goals | kaggle | [바로가기](https://www.kaggle.com/datasets/azminetoushikwasi/cr7-cristiano-ronaldo-all-club-goals-stats) |
| Crowd Counting | kaggle | [바로가기](https://www.kaggle.com/datasets/fmena14/crowd-counting) |
| CS:GO Competitive Matchmaking Data | kaggle | [바로가기](https://www.kaggle.com/datasets/skihikingkevin/csgo-matchmaking-damage) |
| CT KIDNEY DATASET: Normal-Cyst-Tumor and Stone | kaggle | [바로가기](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone) |
| Cuff-Less Blood Pressure Estimation | kaggle | [바로가기](https://www.kaggle.com/datasets/mkachuee/BloodPressureDataset) |
| Cyber Security Attacks | kaggle | [바로가기](https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks) |
| DAIGT External Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/alejopaullier/daigt-external-dataset) |
| DAIGT Proper Train Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/thedrcat/daigt-proper-train-dataset) |
| DAIGT V2 Train Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/thedrcat/daigt-v2-train-dataset) |
| Dark Net Marketplace Data (Agora 2014-2015) | kaggle | [바로가기](https://www.kaggle.com/datasets/philipjames11/dark-net-marketplace-drug-data-agora-20142015) |
| Dark Triad Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/dark-triad-data-csv) |
| DARPA TIMIT Acoustic-Phonetic Continuous Speech | kaggle | [바로가기](https://www.kaggle.com/datasets/mfekadu/darpa-timit-acousticphonetic-continuous-speech) |
| Data Co SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS | kaggle | [바로가기](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis) |
| Data for Admission in the University | kaggle | [바로가기](https://www.kaggle.com/datasets/akshaydattatraykhare/data-for-admission-in-the-university) |
| Data Police shootings | kaggle | [바로가기](https://www.kaggle.com/datasets/mrmorj/data-police-shootings) |
| Data Professionals Salary - 2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/analytics-industry-salaries-2022-india) |
| Data Science Cheat Sheets | kaggle | [바로가기](https://www.kaggle.com/datasets/timoboz/data-science-cheat-sheets) |
| Data Science for Good: Center for Policing Equity | kaggle | [바로가기](https://www.kaggle.com/datasets/center-for-policing-equity/data-science-for-good) |
| Data Science for Good: Kiva Crowdfunding | kaggle | [바로가기](https://www.kaggle.com/datasets/kiva/data-science-for-good-kiva-crowdfunding) |
| Data Science for Good: PASSNYC | kaggle | [바로가기](https://www.kaggle.com/datasets/passnyc/data-science-for-good) |
| Data Science Salaries 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023) |
| Data Science Workshop | kaggle | [바로가기](https://www.kaggle.com/datasets/shivavashishtha/data-science-workshop) |
| Data scientist salary | kaggle | [바로가기](https://www.kaggle.com/datasets/nikhilbhathi/data-scientist-salary-us-glassdoor) |
| Data Visualization Cheat sheets and Resources | kaggle | [바로가기](https://www.kaggle.com/datasets/kaushiksuresh147/data-visualization-cheat-cheats-and-resources) |
| Data Without Drift | kaggle | [바로가기](https://www.kaggle.com/datasets/cdeotte/data-without-drift) |
| Dataset for chatbot | kaggle | [바로가기](https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot) |
| Dataset of songs in Spotify | kaggle | [바로가기](https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify) |
| Dataset Tanaman Padi Sumatera, Indonesia | kaggle | [바로가기](https://www.kaggle.com/datasets/ardikasatria/datasettanamanpadisumatera) |
| Date Fruit Datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/date-fruit-datasets) |
| DDoS Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/devendra416/ddos-datasets) |
| DDSM Mammography | kaggle | [바로가기](https://www.kaggle.com/datasets/skooch/ddsm-mammography) |
| Deep Globe Road Extraction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/balraj98/deepglobe-road-extraction-dataset) |
| Deforestation in Federal Conservation Units | kaggle | [바로가기](https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadstserofcsv) |
| Dental Radiography | kaggle | [바로가기](https://www.kaggle.com/datasets/imtkaggleteam/dental-radiography) |
| Depression Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/anthonytherrien/depression-dataset) |
| Dermnet | kaggle | [바로가기](https://www.kaggle.com/datasets/shubhamgoel27/dermnet) |
| Detailed NFL Play-by-Play Data 2009-2018 | kaggle | [바로가기](https://www.kaggle.com/datasets/maxhorowitz/nflplaybyplay2009to2016) |
| Diabetic Retinopathy (resized) | kaggle | [바로가기](https://www.kaggle.com/datasets/tanlikesmath/diabetic-retinopathy-resized) |
| Diabetic Retinopathy 224x224 Gaussian Filtered | kaggle | [바로가기](https://www.kaggle.com/datasets/sovitrath/diabetic-retinopathy-224x224-gaussian-filtered) |
| Diamonds | kaggle | [바로가기](https://www.kaggle.com/datasets/shivam2503/diamonds) |
| Dirty Excel Data | kaggle | [바로가기](https://www.kaggle.com/datasets/shivavashishtha/dirty-excel-data) |
| Discover Perfect ride:OLXScooty and Scooters | kaggle | [바로가기](https://www.kaggle.com/datasets/marianadeem755/discover-perfect-rideolxscooty-and-scooters) |
| Disney+ Movies and TV Shows | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows) |
| Divorce Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/divorce-prediction) |
| DL Course Data | kaggle | [바로가기](https://www.kaggle.com/datasets/ryanholbrook/dl-course-data) |
| Dog vs Cat | kaggle | [바로가기](https://www.kaggle.com/datasets/anthonytherrien/dog-vs-cat) |
| Dog vs Cat (fastai) | kaggle | [바로가기](https://www.kaggle.com/datasets/arpitjain007/dog-vs-cat-fastai) |
| Dogs vs Cats | kaggle | [바로가기](https://www.kaggle.com/datasets/biaiscience/dogs-vs-cats) |
| Dollar Vs Asian Currencies | kaggle | [바로가기](https://www.kaggle.com/datasets/imtkaggleteam/dollar-vs-asian-currencies) |
| Donald Trump Rally Speeches | kaggle | [바로가기](https://www.kaggle.com/datasets/christianlillelund/donald-trumps-rallies) |
| Dota 2 Matches | kaggle | [바로가기](https://www.kaggle.com/datasets/devinanzelmo/dota-2-matches) |
| Drone Dataset (UAV) | kaggle | [바로가기](https://www.kaggle.com/datasets/dasmehdixtr/drone-dataset-uav) |
| Drug overdose deaths | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/drug-overdose-deaths) |
| Drugs A, B, C, X, Y for Decision Trees | kaggle | [바로가기](https://www.kaggle.com/datasets/pablomgomez21/drugs-a-b-c-x-y-for-decision-trees) |
| Dry Bean Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/dry-bean-dataset) |
| Dunnhumby - The Complete Journey | kaggle | [바로가기](https://www.kaggle.com/datasets/frtgnn/dunnhumby-the-complete-journey) |
| Durum Wheat Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/durum-wheat-dataset) |
| e Commerce Events History in Cosmetics Shop | kaggle | [바로가기](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop) |
| e Commerce Item Data | kaggle | [바로가기](https://www.kaggle.com/datasets/cclark/product-item-data) |
| E-Commerce Data | kaggle | [바로가기](https://www.kaggle.com/datasets/benroshan/ecommerce-data) |
| E-Commerce Data | kaggle | [바로가기](https://www.kaggle.com/datasets/carrie1/ecommerce-data) |
| E-Commerce Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/steve1215rogg/e-commerce-dataset) |
| E-commerce Public Dataset by Alibaba | kaggle | [바로가기](https://www.kaggle.com/datasets/AppleEcomerceInfo/ecommerce-information) |
| Earnings of females and males employees | kaggle | [바로가기](https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadsearningcsv) |
| Ebola 2014-2016 Western Africa Ebola Outbreak | kaggle | [바로가기](https://www.kaggle.com/datasets/imdevskp/ebola-outbreak-20142016-complete-dataset) |
| Edge-IIo Tset Cyber Security Dataset of IoT and IIoT | kaggle | [바로가기](https://www.kaggle.com/datasets/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot) |
| Efficient Net Py Torch | kaggle | [바로가기](https://www.kaggle.com/datasets/hmendonca/efficientnet-pytorch) |
| Electric Power Consumption | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/electric-power-consumption) |
| Electric Vehicle Charging Patterns | kaggle | [바로가기](https://www.kaggle.com/datasets/valakhorasani/electric-vehicle-charging-patterns) |
| Electric Vehicle Specs Dataset (2025) | kaggle | [바로가기](https://www.kaggle.com/datasets/urvishahir/electric-vehicle-specifications-dataset-2025) |
| Elliptic Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set) |
| Emergency - 911 Calls | kaggle | [바로가기](https://www.kaggle.com/datasets/mchirico/montcoalert) |
| Emotion Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/abdallahwagih/emotion-dataset) |
| Emotions | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/emotions) |
| Employee Analysis Attrition Report | kaggle | [바로가기](https://www.kaggle.com/datasets/whenamancodes/hr-employee-attrition) |
| Employee Attrition | kaggle | [바로가기](https://www.kaggle.com/datasets/HRAnalyticRepository/employee-attrition-data) |
| Employee Attrition | kaggle | [바로가기](https://www.kaggle.com/datasets/patelprashant/employee-attrition) |
| Employee dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset) |
| Employee Salaries Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/sahirmaharajj/employee-salaries-analysis) |
| Employee/HR Dataset (All in One) | kaggle | [바로가기](https://www.kaggle.com/datasets/ravindrasinghrana/employeedataset) |
| Engineering Placements Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/tejashvi14/engineering-placements-prediction) |
| English Premier League | kaggle | [바로가기](https://www.kaggle.com/datasets/saife245/english-premier-league) |
| English Premier League (EPL) Results | kaggle | [바로가기](https://www.kaggle.com/datasets/irkaal/english-premier-league-results) |
| English Premier League stats 2019-2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/idoyo92/epl-stats-20192020) |
| English Premier League(2020-21) | kaggle | [바로가기](https://www.kaggle.com/datasets/rajatrc1705/english-premier-league202021) |
| English Word Frequency | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/english-word-frequency) |
| Environment Impact of Food Production | kaggle | [바로가기](https://www.kaggle.com/datasets/selfvivek/environment-impact-of-food-production) |
| Epicurious - Recipes with Rating and Nutrition | kaggle | [바로가기](https://www.kaggle.com/datasets/hugodarwood/epirecipes) |
| Epileptic Seizure Recognition | kaggle | [바로가기](https://www.kaggle.com/datasets/harunshimanto/epileptic-seizure-recognition) |
| EPL Results 1993-2018 | kaggle | [바로가기](https://www.kaggle.com/datasets/thefc17/epl-results-19932018) |
| Ethereum Blockchain | kaggle | [바로가기](https://www.kaggle.com/datasets/bigquery/ethereum-blockchain) |
| Ethereum Historical Data | kaggle | [바로가기](https://www.kaggle.com/datasets/kingburrito666/ethereum-historical-data) |
| European Soccer Database | kaggle | [바로가기](https://www.kaggle.com/datasets/hugomathien/soccer) |
| European Soccer Score Card Database | kaggle | [바로가기](https://www.kaggle.com/datasets/omercolakoglu/european-soccer-score-card-database) |
| EVs - One Electric Vehicle Dataset - Smaller | kaggle | [바로가기](https://www.kaggle.com/datasets/geoffnel/evs-one-electric-vehicle-dataset) |
| Exam Score Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kundanbedmutha/exam-score-prediction-dataset) |
| Excel data file | kaggle | [바로가기](https://www.kaggle.com/datasets/rbansalasr/excel-data-file) |
| Eye Gaze | kaggle | [바로가기](https://www.kaggle.com/datasets/4quant/eye-gaze) |
| Facebook Ad Campaign | kaggle | [바로가기](https://www.kaggle.com/datasets/madislemsalu/facebook-ad-campaign) |
| Facebook Data | kaggle | [바로가기](https://www.kaggle.com/datasets/sheenabatra/facebook-data) |
| Facebook V Results: Predicting Check Ins | kaggle | [바로가기](https://www.kaggle.com/datasets/facebook/facebook-v-results) |
| Famous Iconic Women | kaggle | [바로가기](https://www.kaggle.com/datasets/fatiimaezzahra/famous-iconic-women) |
| Fashion Clothing Products Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/fashion-clothing-products-catalog) |
| Fast Food Nutrition | kaggle | [바로가기](https://www.kaggle.com/datasets/joebeachcapital/fast-food) |
| Fast Food Restaurants Across America | kaggle | [바로가기](https://www.kaggle.com/datasets/datafiniti/fast-food-restaurants) |
| Fastfood Nutrition | kaggle | [바로가기](https://www.kaggle.com/datasets/ulrikthygepedersen/fastfood-nutrition) |
| Fatal Police Shootings in the US | kaggle | [바로가기](https://www.kaggle.com/datasets/kwullum/fatal-police-shootings-in-the-us) |
| Fatalities in the Israeli-Palestinian | kaggle | [바로가기](https://www.kaggle.com/datasets/willianoliveiragibin/fatalities-in-the-israeli-palestinian) |
| Faulty Steel Plates | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/faulty-steel-plates) |
| Feather and Parquet Files: AMEX-Default Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/parquet-files-amexdefault-prediction) |
| Federal Reserve Interest Rates, 1954-Present | kaggle | [바로가기](https://www.kaggle.com/datasets/federalreserve/interest-rates) |
| FER-2013 | kaggle | [바로가기](https://www.kaggle.com/datasets/msambare/fer2013) |
| fer2013 | kaggle | [바로가기](https://www.kaggle.com/datasets/deadskull7/fer2013) |
| FIFA 18 Complete Player Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/thec03u5/fifa-18-demo-player-dataset) |
| Fifa 18 More Complete Player Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kevinmh/fifa-18-more-complete-player-dataset) |
| FIFA 19 complete player dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/javagarm/fifa-19-complete-player-dataset) |
| FIFA 20 complete player dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/stefanoleone992/fifa-20-complete-player-dataset) |
| FIFA 21 complete player dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset) |
| FIFA 21 messy, raw dataset for cleaning/exploring | kaggle | [바로가기](https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring) |
| FIFA 22 complete player dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset) |
| FIFA 23 complete player dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset) |
| FIFA Soccer Rankings | kaggle | [바로가기](https://www.kaggle.com/datasets/tadhgfitzgerald/fifa-international-soccer-mens-ranking-1993now) |
| Finding and Measuring Lungs in CT Data | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/finding-lungs-in-ct-data) |
| Fingers | kaggle | [바로가기](https://www.kaggle.com/datasets/koryakinp/fingers) |
| Fit Bit Fitness Tracker Data | kaggle | [바로가기](https://www.kaggle.com/datasets/arashnic/fitbit) |
| Five Thirty Eight | kaggle | [바로가기](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight) |
| Five Thirty Eight Comic Characters Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-comic-characters-dataset) |
| Five Thirty Eight Comic Characters Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/idrisbenmahdjoub/fivethirtyeight-comic-characters-dataset) |
| Flickr 8k Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/adityajn105/flickr8k) |
| Flickr8K | kaggle | [바로가기](https://www.kaggle.com/datasets/shadabhussain/flickr8k) |
| Flight Fare Prediction MH | kaggle | [바로가기](https://www.kaggle.com/datasets/nikhilmittal/flight-fare-prediction-mh) |
| Flight Route Database | kaggle | [바로가기](https://www.kaggle.com/datasets/open-flights/flight-route-database) |
| Flight Status Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022) |
| Flipkart Products | kaggle | [바로가기](https://www.kaggle.com/datasets/PromptCloudHQ/flipkart-products) |
| Flowers Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/imsparsh/flowers-dataset) |
| Flowers Recognition | kaggle | [바로가기](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition) |
| Food 101 | kaggle | [바로가기](https://www.kaggle.com/datasets/dansbecker/food-101) |
| Food App Business | kaggle | [바로가기](https://www.kaggle.com/datasets/ybifoundation/food-app-business) |
| Food choices | kaggle | [바로가기](https://www.kaggle.com/datasets/borapajo/food-choices) |
| Food Delivery Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset) |
| Food Nutrition Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/utsavdey1410/food-nutrition-dataset) |
| Food.com Recipes and Interactions | kaggle | [바로가기](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions) |
| Football Data from Transfermarkt | kaggle | [바로가기](https://www.kaggle.com/datasets/davidcariboo/player-scores) |
| Football Data: Expected Goals and Other Metrics | kaggle | [바로가기](https://www.kaggle.com/datasets/slehkyi/extended-football-stats-for-european-leagues-xg) |
| Football Events | kaggle | [바로가기](https://www.kaggle.com/datasets/secareanualin/football-events) |
| Football Players Stats (Premier League 2021-2022) | kaggle | [바로가기](https://www.kaggle.com/datasets/omkargowda/football-players-stats-premier-league-20212022) |
| Forbes 2022 Billionaires data [Pre-processed] | kaggle | [바로가기](https://www.kaggle.com/datasets/surajjha101/forbes-billionaires-data-preprocessed) |
| Forecasts for Product Demand | kaggle | [바로가기](https://www.kaggle.com/datasets/felixzhao/productdemandforecasting) |
| Foreign Exchange Rates 2000-2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/brunotly/foreign-exchange-rates-per-dollar-20002019) |
| Formula 1 Race Data | kaggle | [바로가기](https://www.kaggle.com/datasets/cjgdev/formula-1-race-data-19502017) |
| Formula 1 Racing (1950 - 2024) | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/formula-1) |
| Formula 1 World Championship (1950 - 2024) | kaggle | [바로가기](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020) |
| Four Shapes | kaggle | [바로가기](https://www.kaggle.com/datasets/smeschke/four-shapes) |
| Fraudulent Transactions Data | kaggle | [바로가기](https://www.kaggle.com/datasets/chitwanmanchanda/fraudulent-transactions-data) |
| Fruit Recognition | kaggle | [바로가기](https://www.kaggle.com/datasets/chrisfilo/fruit-recognition) |
| Fruits-262 | kaggle | [바로가기](https://www.kaggle.com/datasets/aelchimminut/fruits262) |
| Fruits-360 dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/moltean/fruits) |
| Full TMDB Movies Dataset 2024 (1M Movies) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) |
| Full TMDb TV Shows Dataset 2024 (150K Shows) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows) |
| Game of Thrones | kaggle | [바로가기](https://www.kaggle.com/datasets/mylesoneill/game-of-thrones) |
| Game of Thrones Subtitles | kaggle | [바로가기](https://www.kaggle.com/datasets/gunnvant/game-of-thrones-srt) |
| Game Recommendations on Steam | kaggle | [바로가기](https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam) |
| GDP per Country 2020-2025 | kaggle | [바로가기](https://www.kaggle.com/datasets/codebynadiia/gdp-per-country-20202025) |
| Gene expression dataset (Golub et al.) | kaggle | [바로가기](https://www.kaggle.com/datasets/crawford/gene-expression) |
| Genetic Variant Classifications | kaggle | [바로가기](https://www.kaggle.com/datasets/kevinarvai/clinvar-conflicting) |
| Genshin Impact Character Data | kaggle | [바로가기](https://www.kaggle.com/datasets/sophiahealy/genshin-impact-character-data) |
| Git Hub Code Snippets | kaggle | [바로가기](https://www.kaggle.com/datasets/simiotic/github-code-snippets) |
| Git Hub Repos | kaggle | [바로가기](https://www.kaggle.com/datasets/github/github-repos) |
| Glo Ve: Global Vectors for Word Representation | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/glove-global-vectors-for-word-representation) |
| Global Cost of Living | kaggle | [바로가기](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living) |
| Global Country Information Dataset 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023) |
| Global Crocodile Species Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset) |
| Global Cybersecurity Threats (2015-2024) | kaggle | [바로가기](https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024) |
| Global Economic Monitor | kaggle | [바로가기](https://www.kaggle.com/datasets/theworldbank/global-economic-monitor) |
| Global Internet users | kaggle | [바로가기](https://www.kaggle.com/datasets/ashishraut64/internet-users) |
| Global Shark Attacks | kaggle | [바로가기](https://www.kaggle.com/datasets/teajay/global-shark-attacks) |
| Global Super Store Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset) |
| Global Terrorism Database | kaggle | [바로가기](https://www.kaggle.com/datasets/START-UMD/gtd) |
| Global Terrorism Database (Turkish) | kaggle | [바로가기](https://www.kaggle.com/datasets/omercolakoglu/global-terrorism-database-turkish) |
| glove.840B.300d.txt | kaggle | [바로가기](https://www.kaggle.com/datasets/takuok/glove840b300dtxt) |
| goodbooks-10k | kaggle | [바로가기](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k) |
| Goodreads Book Datasets With User Rating 2M | kaggle | [바로가기](https://www.kaggle.com/datasets/bahramjannesarr/goodreads-book-datasets-10m) |
| Goodreads-books | kaggle | [바로가기](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks) |
| Google Analytics Sample | kaggle | [바로가기](https://www.kaggle.com/datasets/bigquery/google-analytics-sample) |
| Google Patents Public Data | kaggle | [바로가기](https://www.kaggle.com/datasets/bigquery/patents) |
| Google Play Store Apps | kaggle | [바로가기](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps) |
| Google Play Store Apps | kaggle | [바로가기](https://www.kaggle.com/datasets/lava18/google-play-store-apps) |
| Google Trends Data | kaggle | [바로가기](https://www.kaggle.com/datasets/timoboz/google-trends-data) |
| Google Workspace Marketplace Apps Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/marianadeem755/google-workspace-marketplace-apps-dataset) |
| Google-Landmarks Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/google/google-landmarks-dataset) |
| Graduate Admission 2 | kaggle | [바로가기](https://www.kaggle.com/datasets/mohansacharya/graduate-admissions) |
| Groceries dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset) |
| Groceries Market Basket Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/irfanasrullah/groceries) |
| Grocery Store Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/shazadudwadia/supermarket) |
| Gun Violence Data | kaggle | [바로가기](https://www.kaggle.com/datasets/jameslko/gun-violence-data) |
| Gym Exercise Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/niharika41298/gym-exercise-data) |
| Gym Members Exercise Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset) |
| H-1B Visa Petitions 2011-2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/nsharan/h-1b-visa) |
| Haberman's Survival Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/gilsousa/habermans-survival-data-set) |
| Hadith Project | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/hadithsahibukhari) |
| Hand Gesture Recognition Database | kaggle | [바로가기](https://www.kaggle.com/datasets/gti-upm/leapgestrecog) |
| Handwriting Recognition | kaggle | [바로가기](https://www.kaggle.com/datasets/landlord/handwriting-recognition) |
| Hate Crimes | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/hate-crimes) |
| Healthy Life Expectancy | kaggle | [바로가기](https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadslifeexpectancycsv) |
| Healthy Lifestyle Cities Report 2021 | kaggle | [바로가기](https://www.kaggle.com/datasets/prasertk/healthy-lifestyle-cities-report-2021) |
| Heartbeat Sounds | kaggle | [바로가기](https://www.kaggle.com/datasets/kinguistics/heartbeat-sounds) |
| Heights and Weights Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/burnoutminer/heights-and-weights-dataset) |
| Hepatitis C Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/hepatitis-c-dataset) |
| Hillary Clinton's Emails | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/hillary-clinton-emails) |
| HIV AIDS Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/imdevskp/hiv-aids-dataset) |
| Hollywood Theatrical Market Synopsis 1995 to 2021 | kaggle | [바로가기](https://www.kaggle.com/datasets/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021) |
| home data for ml course | kaggle | [바로가기](https://www.kaggle.com/datasets/dansbecker/home-data-for-ml-course) |
| Homicide Reports, 1980-2014 | kaggle | [바로가기](https://www.kaggle.com/datasets/murderaccountability/homicide-reports) |
| Honey Production in the USA (1998-2012) | kaggle | [바로가기](https://www.kaggle.com/datasets/jessicali9530/honey-production) |
| Horse Racing in HK | kaggle | [바로가기](https://www.kaggle.com/datasets/gdaley/hkracing) |
| Horses Or Humans Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sanikamal/horses-or-humans-dataset) |
| Hospitals and beds in India (Statewise) | kaggle | [바로가기](https://www.kaggle.com/datasets/dheerajmpai/hospitals-and-beds-in-india) |
| Hotel Booking | kaggle | [바로가기](https://www.kaggle.com/datasets/mojtaba142/hotel-booking) |
| Hotel booking demand | kaggle | [바로가기](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) |
| House Rent Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset) |
| Household Electric Power Consumption | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set) |
| HR Analytics | kaggle | [바로가기](https://www.kaggle.com/datasets/giripujar/hr-analytics) |
| HR Analytics | kaggle | [바로가기](https://www.kaggle.com/datasets/rishikeshkonapure/hr-analytics-prediction) |
| HR Analytics Case Study | kaggle | [바로가기](https://www.kaggle.com/datasets/vjchoudhary7/hr-analytics-case-study) |
| HR Analytics Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/anshika2301/hr-analytics-dataset) |
| Huggingface BERT | kaggle | [바로가기](https://www.kaggle.com/datasets/xhlulu/huggingface-bert) |
| Human Action Recognition (HAR) Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/meetnagadia/human-action-recognition-har-dataset) |
| Human Activity Recognition with Smartphones | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/human-activity-recognition-with-smartphones) |
| Human Resources Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/rhuebner/human-resources-data-set) |
| IAM Handwriting Top50 | kaggle | [바로가기](https://www.kaggle.com/datasets/tejasreddy/iam-handwriting-top50) |
| IBM HR Analytics Employee Attrition and Performance | kaggle | [바로가기](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) |
| IBM Transactions for Anti Money Laundering (AML) | kaggle | [바로가기](https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml) |
| ICR-integer-data | kaggle | [바로가기](https://www.kaggle.com/datasets/raddar/icr-integer-data) |
| IDS 2018 Intrusion CSVs (CSE-CIC-IDS2018) | kaggle | [바로가기](https://www.kaggle.com/datasets/solarmainframe/ids-intrusion-csv) |
| IMDB 5000 Movie Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset) |
| IMDB data from 2006 to 2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/PromptCloudHQ/imdb-data) |
| IMDb Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset) |
| IMDB movies dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset) |
| IMDB Movies Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows) |
| IMDB Top 250 Movies Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset) |
| Impact of AI on Digital Media (2020-2025) | kaggle | [바로가기](https://www.kaggle.com/datasets/atharvasoundankar/impact-of-ai-on-digital-media-2020-2025) |
| India - Trade Data | kaggle | [바로가기](https://www.kaggle.com/datasets/lakshyaag/india-trade-data) |
| India 2020 District Level Shape files | kaggle | [바로가기](https://www.kaggle.com/datasets/imdevskp/india-district-wise-shape-files) |
| Indian Food 101 | kaggle | [바로가기](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101) |
| Indian Kids Screentime 2025 | kaggle | [바로가기](https://www.kaggle.com/datasets/ankushpanday2/indian-kids-screentime-2025) |
| Indian License Plates | kaggle | [바로가기](https://www.kaggle.com/datasets/thamizhsterio/indian-license-plates) |
| Indian Premier League (Cricket) | kaggle | [바로가기](https://www.kaggle.com/datasets/manasgarg/ipl) |
| Indian Premier League 2008-2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/nowke9/ipldata) |
| Indian Premier League CSV dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/harsha547/indian-premier-league-csv-dataset) |
| Indian Startup Funding | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding) |
| Indicators of Anxiety or Depression | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/indicators-of-anxiety-or-depression) |
| Indonesia Tourism Destination | kaggle | [바로가기](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination) |
| Instacart Market Basket Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis) |
| Intelligent Monitor | kaggle | [바로가기](https://www.kaggle.com/datasets/ptdevsecops/intelligent-monitor) |
| Interesting Data to Visualize | kaggle | [바로가기](https://www.kaggle.com/datasets/alexisbcook/data-for-datavis) |
| International football results from 1872 to 2026 | kaggle | [바로가기](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) |
| International Greenhouse Gas Emissions | kaggle | [바로가기](https://www.kaggle.com/datasets/unitednations/international-greenhouse-gas-emissions) |
| Inventory Analysis Case Study | kaggle | [바로가기](https://www.kaggle.com/datasets/bhanupratapbiswas/inventory-analysis-case-study) |
| IP Network Traffic Flows Labeled with 75 Apps | kaggle | [바로가기](https://www.kaggle.com/datasets/jsrojas/ip-network-traffic-flows-labeled-with-87-apps) |
| IPL - Player Performance Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/ipl-player-performance-dataset) |
| IPL 2008 to 2022 All Match Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset) |
| IPL _Data_Set | kaggle | [바로가기](https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set) |
| IPL Complete Dataset (2008-2024) | kaggle | [바로가기](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020) |
| Iris dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/himanshunakrani/iris-dataset) |
| Iris Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vikrishnan/iris-dataset) |
| Iris Flower Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/arshid/iris-flower-dataset) |
| Iris Species | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/iris) |
| Iris.csv | kaggle | [바로가기](https://www.kaggle.com/datasets/saurabh00007/iriscsv) |
| January Flight Delay Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction) |
| Kaggle Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rajugc/kaggle-dataset) |
| Kaggle Datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/morriswongch/kaggle-datasets) |
| Kaggle: Cat VS Dog Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/karakaggle/kaggle-cat-vs-dog-dataset) |
| Ken Jee You Tube Data | kaggle | [바로가기](https://www.kaggle.com/datasets/kenjee/ken-jee-youtube-data) |
| Keras Pretrained models | kaggle | [바로가기](https://www.kaggle.com/datasets/gaborfodor/keras-pretrained-models) |
| Kickstarter Projects | kaggle | [바로가기](https://www.kaggle.com/datasets/kemical/kickstarter-projects) |
| Korean Single Speaker Speech Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/bryanpark/korean-single-speaker-speech-dataset) |
| Landscape Pictures | kaggle | [바로가기](https://www.kaggle.com/datasets/arnaud58/landscape-pictures) |
| Latest Data Science Salaries | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/data-science-salaries-2023) |
| Latest Netflix data with 26+ joined attributes | kaggle | [바로가기](https://www.kaggle.com/datasets/ashishgup/netflix-rotten-tomatoes-metacritic-imdb) |
| Latest Netflix TV shows and movies | kaggle | [바로가기](https://www.kaggle.com/datasets/senapatirajesh/netflix-tv-shows-and-movies) |
| Layoffs Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/swaptr/layoffs-2022) |
| League of Legends | kaggle | [바로가기](https://www.kaggle.com/datasets/chuckephron/leagueoflegends) |
| League of Legends Diamond Ranked Games (10 min) | kaggle | [바로가기](https://www.kaggle.com/datasets/bobbyscience/league-of-legends-diamond-ranked-games-10-min) |
| League of Legends Ranked Matches | kaggle | [바로가기](https://www.kaggle.com/datasets/paololol/league-of-legends-ranked-matches) |
| LEGO Database | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/lego-database) |
| Lettuce Growth Days Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/jurijsruko/lettuce) |
| Life Expectancy (WHO) | kaggle | [바로가기](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who) |
| Life Style Data | kaggle | [바로가기](https://www.kaggle.com/datasets/jockeroika/life-style-data) |
| Lionel Messi All Club Goals | kaggle | [바로가기](https://www.kaggle.com/datasets/azminetoushikwasi/-lionel-messi-all-club-goals) |
| LISA Traffic Light Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mbornoe/lisa-traffic-light-dataset) |
| List of PyPI Packages | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/list-of-pypi-packages) |
| Loans and Liability | kaggle | [바로가기](https://www.kaggle.com/datasets/matinmahmoudi/loans-and-liability) |
| Logos: BK KFC Mc Donald Starbucks Subway None | kaggle | [바로가기](https://www.kaggle.com/datasets/kmkarakaya/logos-bk-kfc-mcdonald-starbucks-subway-none) |
| London bike sharing dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset) |
| Los Angeles Metro Bike Share Trip Data | kaggle | [바로가기](https://www.kaggle.com/datasets/cityofLA/los-angeles-metro-bike-share-trip-data) |
| Los Angeles Parking Citations | kaggle | [바로가기](https://www.kaggle.com/datasets/cityofLA/los-angeles-parking-citations) |
| Lower Back Pain Symptoms Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sammy123/lower-back-pain-symptoms-dataset) |
| Magic The Gathering Cards | kaggle | [바로가기](https://www.kaggle.com/datasets/mylesoneill/magic-the-gathering-cards) |
| Malaria Bounding Boxes | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/malaria-bounding-boxes) |
| Malaria Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/imdevskp/malaria-dataset) |
| Malicious and Benign Websites | kaggle | [바로가기](https://www.kaggle.com/datasets/xwolf12/malicious-and-benign-websites) |
| Malicious URLs dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset) |
| Mall_Customers | kaggle | [바로가기](https://www.kaggle.com/datasets/shwetabh123/mall-customers) |
| Malnutrition across the globe | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/malnutrition-across-the-globe) |
| Mango Leaf | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/mangoleaf) |
| Market Basket Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis) |
| Marketing Analytics | kaggle | [바로가기](https://www.kaggle.com/datasets/jackdaoud/marketing-data) |
| Marketing Campaign | kaggle | [바로가기](https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign) |
| Marketing Funnel by Olist | kaggle | [바로가기](https://www.kaggle.com/datasets/olistbr/marketing-funnel-olist) |
| Marvel Comic Books Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/deepcontractor/marvel-comic-books) |
| Math Students | kaggle | [바로가기](https://www.kaggle.com/datasets/janiobachmann/math-students) |
| Mc Donald's India: Menu Nutrition Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/deepcontractor/mcdonalds-india-menu-nutrition-facts) |
| Medicare Data | kaggle | [바로가기](https://www.kaggle.com/datasets/cms/cms-medicare) |
| Medium articles dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/dorianlazar/medium-articles-dataset) |
| Melanoma TFRecords 256x256 | kaggle | [바로가기](https://www.kaggle.com/datasets/cdeotte/melanoma-256x256) |
| Memory Test on Drugged Islanders Data | kaggle | [바로가기](https://www.kaggle.com/datasets/steveahn/memory-test-on-drugged-islanders-data) |
| Meta Kaggle | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/meta-kaggle) |
| Meta Kaggle Code | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/meta-kaggle-code) |
| MIAS Mammography | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/mias-mammography) |
| Michelin Restaurants | kaggle | [바로가기](https://www.kaggle.com/datasets/jackywang529/michelin-restaurants) |
| Military Spending of Countries (1960-2019) | kaggle | [바로가기](https://www.kaggle.com/datasets/nitinsss/military-expenditure-of-countries-19602019) |
| Milk Quality Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/cpluzshrijayan/milkquality) |
| Missing Migrants Project | kaggle | [바로가기](https://www.kaggle.com/datasets/snocco/missing-migrants-project) |
| MIT-BIH Database | kaggle | [바로가기](https://www.kaggle.com/datasets/mondejar/mitbih-database) |
| MLB Pitch Data 2015-2018 | kaggle | [바로가기](https://www.kaggle.com/datasets/pschale/mlb-pitch-data-20152018) |
| mlcourse.ai | kaggle | [바로가기](https://www.kaggle.com/datasets/kashnitsky/mlcourse) |
| Mobile App Store (7200 apps) | kaggle | [바로가기](https://www.kaggle.com/datasets/ramamet4/app-store-apple-data-set-10k-apps) |
| Mobile phone activity in a city | kaggle | [바로가기](https://www.kaggle.com/datasets/marcodena/mobile-phone-activity) |
| Mobile Phones | kaggle | [바로가기](https://www.kaggle.com/datasets/muhammedtausif/best-selling-mobile-phones) |
| Mobiles Dataset (2025) | kaggle | [바로가기](https://www.kaggle.com/datasets/abdulmalik1518/mobiles-dataset-2025) |
| Mohs Hardness Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/hardikgarg03/mohs-hardness-dataset) |
| Monty Python Flying Circus | kaggle | [바로가기](https://www.kaggle.com/datasets/allank/monty-python-flying-circus) |
| Most Played Mobile Games (2008-2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/marianadeem755/most-played-mobile-games2008-2020) |
| Most Streamed Spotify Songs 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023) |
| Most Streamed Spotify Songs 2024 | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024) |
| Most Subscribed 1000 Youtube Channels | kaggle | [바로가기](https://www.kaggle.com/datasets/themrityunjaypathak/most-subscribed-1000-youtube-channels) |
| Most Subscribed You Tube Channels | kaggle | [바로가기](https://www.kaggle.com/datasets/surajjha101/top-youtube-channels-data) |
| Movie Genre from its Poster | kaggle | [바로가기](https://www.kaggle.com/datasets/neha1703/movie-genre-from-its-poster) |
| Movie Industry | kaggle | [바로가기](https://www.kaggle.com/datasets/danielgrijalvas/movies) |
| Movie Lens 20M Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset) |
| Movie Tweetings | kaggle | [바로가기](https://www.kaggle.com/datasets/tunguz/movietweetings) |
| MOVIES DATASET FOR FEATURE EXTRACION,PREDICTION | kaggle | [바로가기](https://www.kaggle.com/datasets/bharatnatrayn/movies-dataset-for-feature-extracion-prediction) |
| Multi-stage continuous-flow manufacturing process | kaggle | [바로가기](https://www.kaggle.com/datasets/supergus/multistage-continuousflow-manufacturing-process) |
| Museum of Modern Art Collection | kaggle | [바로가기](https://www.kaggle.com/datasets/momanyc/museum-collection) |
| Music Caps | kaggle | [바로가기](https://www.kaggle.com/datasets/googleai/musiccaps) |
| Music features | kaggle | [바로가기](https://www.kaggle.com/datasets/insiyeah/musicfeatures) |
| Music Net Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/imsparsh/musicnet-dataset) |
| My Anime List Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/azathoth42/myanimelist) |
| My Uber Drives | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/uberdrives) |
| NBA Database | kaggle | [바로가기](https://www.kaggle.com/datasets/wyattowalsh/basketball) |
| NBA Database (1947 - Present) | kaggle | [바로가기](https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores) |
| NBA Enhanced Box Score and Standings (2012 - 2018) | kaggle | [바로가기](https://www.kaggle.com/datasets/pablote/nba-enhanced-stats) |
| NBA games data | kaggle | [바로가기](https://www.kaggle.com/datasets/nathanlauga/nba-games) |
| NBA player of the week | kaggle | [바로가기](https://www.kaggle.com/datasets/jacobbaruch/nba-player-of-the-week) |
| NBA Players | kaggle | [바로가기](https://www.kaggle.com/datasets/justinas/nba-players-data) |
| NBA Players stats since 1950 | kaggle | [바로가기](https://www.kaggle.com/datasets/drgilermo/nba-players-stats) |
| NBA shot logs | kaggle | [바로가기](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs) |
| NBA Stats (1947-present) | kaggle | [바로가기](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats) |
| NCAA Basketball | kaggle | [바로가기](https://www.kaggle.com/datasets/ncaa/ncaa-basketball) |
| NCAA Men 538 team ratings | kaggle | [바로가기](https://www.kaggle.com/datasets/raddar/ncaa-men-538-team-ratings) |
| Netflix Data: Cleaning, Analysis and Visualization | kaggle | [바로가기](https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization) |
| Netflix IMDB Scores | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/netflix-imdb-scores) |
| Netflix Movies and TV Shows | kaggle | [바로가기](https://www.kaggle.com/datasets/anandshaw2001/netflix-movies-and-tv-shows) |
| Netflix Movies and TV Shows | kaggle | [바로가기](https://www.kaggle.com/datasets/rahulvyasm/netflix-movies-and-tv-shows) |
| Netflix Movies and TV Shows | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/netflix-shows) |
| Netflix Original Films and IMDB Scores | kaggle | [바로가기](https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores) |
| Netflix TV Shows and Movies | kaggle | [바로가기](https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies) |
| Network Intrusion dataset(CIC-IDS- 2017) | kaggle | [바로가기](https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset) |
| New Plant Diseases Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) |
| NFL Football Player Stats | kaggle | [바로가기](https://www.kaggle.com/datasets/zynicide/nfl-football-player-stats) |
| NFL scores and betting data | kaggle | [바로가기](https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data) |
| NFT Collections | kaggle | [바로가기](https://www.kaggle.com/datasets/hemil26/nft-collections-dataset) |
| NHL Game Data | kaggle | [바로가기](https://www.kaggle.com/datasets/martinellis/nhl-game-data) |
| Nifty Indices Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/nifty-indices-dataset) |
| NIH Chest X-rays | kaggle | [바로가기](https://www.kaggle.com/datasets/nih-chest-xrays/data) |
| NIPS Papers | kaggle | [바로가기](https://www.kaggle.com/datasets/benhamner/nips-papers) |
| No Data Sources | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/no-data-sources) |
| Notebooks of the Week - Hidden Gems | kaggle | [바로가기](https://www.kaggle.com/datasets/headsortails/notebooks-of-the-week-hidden-gems) |
| Novel Corona Virus 2019 Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset) |
| NSE - Nifty 50 Index Minute data (2015 to 2026) | kaggle | [바로가기](https://www.kaggle.com/datasets/debashis74017/nifty-50-minute-data) |
| NSL-KDD | kaggle | [바로가기](https://www.kaggle.com/datasets/hassan06/nslkdd) |
| Nutrition Facts for Mc Donald's Menu | kaggle | [바로가기](https://www.kaggle.com/datasets/mcdonalds/nutrition-facts) |
| Nutrition facts for Starbucks Menu | kaggle | [바로가기](https://www.kaggle.com/datasets/starbucks/starbucks-menu) |
| NYC Parking Tickets | kaggle | [바로가기](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets) |
| NYS Environmental Remediation Sites | kaggle | [바로가기](https://www.kaggle.com/datasets/new-york-state/nys-environmental-remediation-sites) |
| Obesity among adults by country, 1975-2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/amanarora/obesity-among-adults-by-country-19752016) |
| Obesity Levels | kaggle | [바로가기](https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels) |
| Obesity or CVD risk (Classify/Regressor/Cluster) | kaggle | [바로가기](https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster) |
| Olympic Data | kaggle | [바로가기](https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data) |
| Olympic Sports and Medals, 1896-2014 | kaggle | [바로가기](https://www.kaggle.com/datasets/the-guardian/olympic-games) |
| Olympic Summer and Winter Games, 1896-2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/piterfm/olympic-games-medals-19862018) |
| Online Courses from Harvard and MIT | kaggle | [바로가기](https://www.kaggle.com/datasets/edx/course-study) |
| Online Food Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset) |
| Online Gaming Anxiety Data | kaggle | [바로가기](https://www.kaggle.com/datasets/divyansh22/online-gaming-anxiety-data) |
| Online Retail Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/vijayuv/onlineretail) |
| Online Retail Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset) |
| Online Shoppers Purchasing Intention Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset) |
| Online Shopping Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jacksondivakarr/online-shopping-dataset) |
| Open Asteroid Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/basu369victor/prediction-of-asteroid-diameter) |
| Open Exoplanet Catalogue | kaggle | [바로가기](https://www.kaggle.com/datasets/mrisdal/open-exoplanet-catalogue) |
| Open Food Facts | kaggle | [바로가기](https://www.kaggle.com/datasets/openfoodfacts/world-food-facts) |
| Open University Learning Analytics Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rocki37/open-university-learning-analytics-dataset) |
| OpenAQ | kaggle | [바로가기](https://www.kaggle.com/datasets/open-aq/openaq) |
| Otto Full Optimized Memory Footprint | kaggle | [바로가기](https://www.kaggle.com/datasets/radek1/otto-full-optimized-memory-footprint) |
| Pakistan Drone Attacks | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/pakistandroneattacks) |
| Pakistan Intellectual Capital | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/pakistanintellectualcapitalcs) |
| Pakistan Suicide Bombing Attacks | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/pakistansuicideattacks) |
| Pakistan Tosha Khana Files | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/pakistan-toshakhana-files) |
| Pakistan's Largest E-Commerce Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/pakistans-largest-ecommerce-dataset) |
| Palestine Body Count | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/palestine-body-count) |
| Palmer Archipelago (Antarctica) penguin data | kaggle | [바로가기](https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data) |
| Panda Set Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/pandaset-dataset) |
| Paradise-Panama-Papers | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/paradisepanamapapers) |
| Paris 2024 Olympic Summer Games | kaggle | [바로가기](https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games) |
| PASCAL VOC 2007 | kaggle | [바로가기](https://www.kaggle.com/datasets/zaraks/pascal-voc-2007) |
| PASCAL VOC 2012 | kaggle | [바로가기](https://www.kaggle.com/datasets/huanghanchina/pascal-voc-2012) |
| Penguin Sizes Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/amulyas/penguin-size-dataset) |
| Perfume E-Commerce Dataset 2024 | kaggle | [바로가기](https://www.kaggle.com/datasets/kanchana1990/perfume-e-commerce-dataset-2024) |
| Phishing Site URLs | kaggle | [바로가기](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls) |
| Pistachio Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/pistachio-dataset) |
| Pizza Restaurants and the Pizza They Sell | kaggle | [바로가기](https://www.kaggle.com/datasets/datafiniti/pizza-restaurants-and-the-pizza-they-sell) |
| Planet Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/planet-dataset) |
| Plant Village | kaggle | [바로가기](https://www.kaggle.com/datasets/arjuntejaswi/plant-village) |
| Plant Village Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset) |
| Plant Village Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/emmarex/plantdisease) |
| PM2.5 Data of Five Chinese Cities | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/pm25-data-for-five-chinese-cities) |
| Pokemon Generation One | kaggle | [바로가기](https://www.kaggle.com/datasets/thedagger/pokemon-generation-one) |
| Pokemon with stats | kaggle | [바로가기](https://www.kaggle.com/datasets/abcsds/pokemon) |
| Police Violence and Racial Equity - Part 1 of 2 | kaggle | [바로가기](https://www.kaggle.com/datasets/jpmiller/police-violence-in-the-us) |
| Polycystic ovary syndrome (PCOS) | kaggle | [바로가기](https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos) |
| Popular Movies of IMDb | kaggle | [바로가기](https://www.kaggle.com/datasets/sankha1998/tmdb-top-10000-popular-movies-dataset) |
| Power consumption in India(2019-2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/twinkle0705/state-wise-power-consumption-in-india) |
| PowerBI Projects | kaggle | [바로가기](https://www.kaggle.com/datasets/jagadishkittu/powerbi-projects) |
| Powerlifting Database | kaggle | [바로가기](https://www.kaggle.com/datasets/open-powerlifting/powerlifting-database) |
| powerlifting-database | kaggle | [바로가기](https://www.kaggle.com/datasets/dansbecker/powerlifting-database) |
| Predict Pakistan Elections 2018 | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/predict-pakistan-elections-2018) |
| Predict Test Scores of students | kaggle | [바로가기](https://www.kaggle.com/datasets/kwadwoofosu/predict-test-scores-of-students) |
| Predict'em All | kaggle | [바로가기](https://www.kaggle.com/datasets/semioniy/predictemall) |
| Premier League | kaggle | [바로가기](https://www.kaggle.com/datasets/zaeemnalla/premier-league) |
| Pretrained Model Weights (Pytorch) | kaggle | [바로가기](https://www.kaggle.com/datasets/abhishek/pretrained-model-weights-pytorch) |
| Problem 2 | kaggle | [바로가기](https://www.kaggle.com/datasets/hardikgarg03/problem-2) |
| Pumpkin Leaf Diseases Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/pumpkin-leaf-diseases-dataset-from-bangladesh) |
| Pumpkin Seeds Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/pumpkin-seeds-dataset) |
| Python Data Science Handbook | kaggle | [바로가기](https://www.kaggle.com/datasets/timoboz/python-data-science-handbook) |
| Python Datatable | kaggle | [바로가기](https://www.kaggle.com/datasets/rohanrao/python-datatable) |
| QS World University Rankings 2025 | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/qs-world-university-rankings-2025) |
| Quality Prediction in a Mining Process | kaggle | [바로가기](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process) |
| Quick Draw Sketches | kaggle | [바로가기](https://www.kaggle.com/datasets/google/tinyquickdraw) |
| Rainfall in India | kaggle | [바로가기](https://www.kaggle.com/datasets/rajanand/rainfall-in-india) |
| Rainfall in Pakistan | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/rainfall-in-pakistan) |
| Raisin Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/raisin-dataset) |
| Ramen Ratings | kaggle | [바로가기](https://www.kaggle.com/datasets/residentmario/ramen-ratings) |
| RAPIDS | kaggle | [바로가기](https://www.kaggle.com/datasets/cdeotte/rapids) |
| RAVDESS Emotional speech audio | kaggle | [바로가기](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio) |
| Real Eastate | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/realeastate) |
| Real Estate Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/arslanali4343/real-estate-dataset) |
| Real Life Violence Situations Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mohamedmustafa/real-life-violence-situations-dataset) |
| Real World Smartphone's Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/abhijitdahatonde/real-world-smartphones-dataset) |
| Recipe Ingredients Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset) |
| Red Wine Quality | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) |
| Reddit - Data is Beautiful | kaggle | [바로가기](https://www.kaggle.com/datasets/unanimad/dataisbeautiful) |
| Reddit Vaccine Myths | kaggle | [바로가기](https://www.kaggle.com/datasets/gpreda/reddit-vaccine-myths) |
| Reddit Wall Street Bets Posts | kaggle | [바로가기](https://www.kaggle.com/datasets/gpreda/reddit-wallstreetsbets-posts) |
| Res Net-50 | kaggle | [바로가기](https://www.kaggle.com/datasets/crawford/resnet50) |
| Respiratory Sound Database | kaggle | [바로가기](https://www.kaggle.com/datasets/vbookshelf/respiratory-sound-database) |
| Restaurant Business Rankings 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/michau96/restaurant-business-rankings-2020) |
| Restaurant's cuisine ratings data (for EDA) | kaggle | [바로가기](https://www.kaggle.com/datasets/surajjha101/cuisine-rating) |
| Resume Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset) |
| Resume Entities for NER | kaggle | [바로가기](https://www.kaggle.com/datasets/dataturks/resume-entities-for-ner) |
| Retail Data Analytics | kaggle | [바로가기](https://www.kaggle.com/datasets/manjeetsingh/retaildataset) |
| Retail Product Checkout Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/diyer22/retail-product-checkout-dataset) |
| Retail Supermarket | kaggle | [바로가기](https://www.kaggle.com/datasets/roopacalistus/superstore) |
| Rice Dataset Commeo and Osmancik | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/rice-dataset-commeo-and-osmancik) |
| Rice Leaf Diseases Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases) |
| Rice Leafs | kaggle | [바로가기](https://www.kaggle.com/datasets/shayanriyaz/riceleafs) |
| Rice MSC Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/rice-msc-dataset) |
| roberta-base | kaggle | [바로가기](https://www.kaggle.com/datasets/abhishek/roberta-base) |
| Roller Coaster Database | kaggle | [바로가기](https://www.kaggle.com/datasets/robikscube/rollercoaster-database) |
| Rounds and Retention | kaggle | [바로가기](https://www.kaggle.com/datasets/matinmahmoudi/rounds-and-retention) |
| RSNA Bone Age | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/rsna-bone-age) |
| RSNA MICCAI PNG | kaggle | [바로가기](https://www.kaggle.com/datasets/jonathanbesomi/rsna-miccai-png) |
| Salary | kaggle | [바로가기](https://www.kaggle.com/datasets/rsadiq/salary) |
| Salary Prediction dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer) |
| Salary_Data | kaggle | [바로가기](https://www.kaggle.com/datasets/mohithsairamreddy/salary-data) |
| Sample Superstore Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/bravehart101/sample-supermarket-dataset) |
| San Francisco Building Permits | kaggle | [바로가기](https://www.kaggle.com/datasets/aparnashastry/building-permit-applications-data) |
| Sarcasm on Reddit | kaggle | [바로가기](https://www.kaggle.com/datasets/danofer/sarcasm) |
| SARS 2003 Outbreak Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/imdevskp/sars-outbreak-2003-complete-dataset) |
| Scrabble Games | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/scrabble-games) |
| Search Engine Results - Flights and Tickets Keywords | kaggle | [바로가기](https://www.kaggle.com/datasets/eliasdabbas/search-engine-results-flights-tickets-keywords) |
| Segmenting Soft Tissue Sarcomas | kaggle | [바로가기](https://www.kaggle.com/datasets/4quant/soft-tissue-sarcoma) |
| Seinfeld Chronicles | kaggle | [바로가기](https://www.kaggle.com/datasets/thec03u5/seinfeld-chronicles) |
| SF Bay Area Bike Share | kaggle | [바로가기](https://www.kaggle.com/datasets/benhamner/sf-bay-area-bike-share) |
| SF Salaries | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/sf-salaries) |
| Shopify app store | kaggle | [바로가기](https://www.kaggle.com/datasets/usernam3/shopify-app-store) |
| Short Jokes | kaggle | [바로가기](https://www.kaggle.com/datasets/abhinavmoudgil95/short-jokes) |
| Smart meters in London | kaggle | [바로가기](https://www.kaggle.com/datasets/jeanmidev/smart-meters-in-london) |
| Software Industry Salary Dataset - 2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/software-professional-salaries-2022) |
| Sokoto Coventry Fingerprint Dataset (SOCOFing) | kaggle | [바로가기](https://www.kaggle.com/datasets/ruizgara/socofing) |
| Song lyrics from 79 musical genres | kaggle | [바로가기](https://www.kaggle.com/datasets/neisse/scrapped-lyrics-from-6-genres) |
| Spaceship Titanic | kaggle | [바로가기](https://www.kaggle.com/datasets/hardikgarg03/spaceship-titanic) |
| Spanish Rail Tickets Pricing - Renfe | kaggle | [바로가기](https://www.kaggle.com/datasets/thegurusteam/spanish-high-speed-rail-system-ticket-pricing) |
| Spanish Wine Quality Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset) |
| Speech Accent Archive | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/speech-accent-archive) |
| Speech Emotion Recognition (en) | kaggle | [바로가기](https://www.kaggle.com/datasets/dmitrybabko/speech-emotion-recognition-en) |
| Speed Dating Experiment | kaggle | [바로가기](https://www.kaggle.com/datasets/annavictoria/speed-dating-experiment) |
| Spotify 1.2M+ Songs | kaggle | [바로가기](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs) |
| Spotify and Youtube | kaggle | [바로가기](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube) |
| Spotify Charts | kaggle | [바로가기](https://www.kaggle.com/datasets/dhruvildave/spotify-charts) |
| Spotify Global Music Dataset (2009-2025) | kaggle | [바로가기](https://www.kaggle.com/datasets/wardabilal/spotify-global-music-dataset-20092025) |
| Spotify Million Song Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset) |
| Spotify Most Streamed Songs | kaggle | [바로가기](https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs) |
| Spotify Music Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset) |
| Spotify Playlists | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/spotify-playlists) |
| Spotify Song Attributes | kaggle | [바로가기](https://www.kaggle.com/datasets/geomack/spotifyclassification) |
| Spotify Top 100 Songs of 2010-2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019) |
| Spotify Top 10000 Streamed Songs | kaggle | [바로가기](https://www.kaggle.com/datasets/rakkesharv/spotify-top-10000-streamed-songs) |
| Spotify Top 200 Charts (2020-2021) | kaggle | [바로가기](https://www.kaggle.com/datasets/sashankpillai/spotify-top-200-charts-20202021) |
| Spotify Tracks Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) |
| Spotify Tracks DB | kaggle | [바로가기](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db) |
| Spotify's Long Hits (2014-2024) | kaggle | [바로가기](https://www.kaggle.com/datasets/kanchana1990/spotifys-long-hits-2014-2024) |
| sql injection dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/syedsaqlainhussain/sql-injection-dataset) |
| SQL Murder Mystery Database | kaggle | [바로가기](https://www.kaggle.com/datasets/johnp47/sql-murder-mystery-database) |
| sRNA sequencing - Pancreas (GSE84133) | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/indian-women-rehabilitation) |
| Stanford Car Dataset by classes folder | kaggle | [바로가기](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder) |
| Stanford Dogs Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset) |
| Star Cluster Simulations | kaggle | [바로가기](https://www.kaggle.com/datasets/mariopasquato/star-cluster-simulations) |
| Star dataset to predict star types | kaggle | [바로가기](https://www.kaggle.com/datasets/deepu1109/star-dataset) |
| Star Wars Movie Scripts | kaggle | [바로가기](https://www.kaggle.com/datasets/xvivancos/star-wars-movie-scripts) |
| Starbucks | kaggle | [바로가기](https://www.kaggle.com/datasets/henryshan/starbucks) |
| Starbucks Locations Worldwide | kaggle | [바로가기](https://www.kaggle.com/datasets/starbucks/store-locations) |
| Start Up Investments (Crunchbase) | kaggle | [바로가기](https://www.kaggle.com/datasets/arindam235/startup-investments-crunchbase) |
| Startup Investments | kaggle | [바로가기](https://www.kaggle.com/datasets/justinas/startup-investments) |
| State of Data Brazil 2021-2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/datahackers/state-of-data-2021) |
| State of Data Brazil 2022-2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/datahackers/state-of-data-2022) |
| State of Data Brazil 2023-2024 | kaggle | [바로가기](https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023) |
| State of Data Brazil 2024-2025 | kaggle | [바로가기](https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-20242025) |
| Steam Games Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) |
| Steam Store Games (Clean dataset) | kaggle | [바로가기](https://www.kaggle.com/datasets/nikdavis/steam-store-games) |
| Stroke Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) |
| Students Exam Scores: Extended Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/desalegngeb/students-exam-scores) |
| Students Performance | kaggle | [바로가기](https://www.kaggle.com/datasets/joebeachcapital/students-performance) |
| Students Performance Clean Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muhammadroshaanriaz/students-performance-dataset-cleaned) |
| Students Performance Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset) |
| Students Performance in Exams | kaggle | [바로가기](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) |
| Students Performance in Exams | kaggle | [바로가기](https://www.kaggle.com/datasets/whenamancodes/students-performance-in-exams) |
| Students' Academic Performance Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data) |
| Students_Academic_Performance_Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sadiajavedd/students-academic-performance-dataset) |
| Suicide Rates Overview 1985 to 2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016) |
| Suicides in India | kaggle | [바로가기](https://www.kaggle.com/datasets/rajanand/suicides-in-india) |
| Summer Olympics Medals (1976-2008) | kaggle | [바로가기](https://www.kaggle.com/datasets/divyansh22/summer-olympics-medals) |
| Sunspots | kaggle | [바로가기](https://www.kaggle.com/datasets/robervalt/sunspots) |
| Super Heroes Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/claudiodavi/superhero-set) |
| Superbowl History 1967 - 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/timoboz/superbowl-history-1967-2020) |
| Superstore Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) |
| Superstore Marketing Campaign Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ahsan81/superstore-marketing-campaign-dataset) |
| superstore_data | kaggle | [바로가기](https://www.kaggle.com/datasets/jr2ngb/superstore-data) |
| Supply Chain Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis) |
| Swiggy Restaurants dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/abhijitdahatonde/swiggy-restuarant-dataset) |
| TACO Dataset YOLO Format | kaggle | [바로가기](https://www.kaggle.com/datasets/vencerlanz09/taco-dataset-yolo-format) |
| Tagged Anime Illustrations | kaggle | [바로가기](https://www.kaggle.com/datasets/mylesoneill/tagged-anime-illustrations) |
| Taxi Trajectory Data | kaggle | [바로가기](https://www.kaggle.com/datasets/crailtap/taxi-trajectory) |
| TED Talks | kaggle | [바로가기](https://www.kaggle.com/datasets/ashishjangra27/ted-talks) |
| TED Talks | kaggle | [바로가기](https://www.kaggle.com/datasets/rounakbanik/ted-talks) |
| Telecom Churn Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mnassrib/telecom-churn-datasets) |
| Teo Me Why Loyalty System | kaggle | [바로가기](https://www.kaggle.com/datasets/teocalvo/teomewhy-loyalty-system) |
| The Complete Pokemon Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rounakbanik/pokemon) |
| The Depression Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/arashnic/the-depression-dataset) |
| The Economic Freedom Index | kaggle | [바로가기](https://www.kaggle.com/datasets/lewisduncan93/the-economic-freedom-index) |
| The History of Baseball | kaggle | [바로가기](https://www.kaggle.com/datasets/seanlahman/the-history-of-baseball) |
| The Holy Quran | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/the-holy-quran) |
| The Human Freedom Index | kaggle | [바로가기](https://www.kaggle.com/datasets/gsutters/the-human-freedom-index) |
| The LJ Speech Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mathurinache/the-lj-speech-dataset) |
| The Movies Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) |
| The Oscar Award, 1927 - 2025 | kaggle | [바로가기](https://www.kaggle.com/datasets/unanimad/the-oscar-award) |
| The Oxford-IIIT Pet Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tanlikesmath/the-oxfordiiit-pet-dataset) |
| The Simpsons Characters Data | kaggle | [바로가기](https://www.kaggle.com/datasets/alexattia/the-simpsons-characters-dataset) |
| The Spotify Hit Predictor Dataset (1960-2019) | kaggle | [바로가기](https://www.kaggle.com/datasets/theoverman/the-spotify-hit-predictor-dataset) |
| The Ultimate Halloween Candy Power Ranking | kaggle | [바로가기](https://www.kaggle.com/datasets/fivethirtyeight/the-ultimate-halloween-candy-power-ranking) |
| The World Factbook by CIA | kaggle | [바로가기](https://www.kaggle.com/datasets/lucafrance/the-world-factbook-by-cia) |
| Things on Reddit | kaggle | [바로가기](https://www.kaggle.com/datasets/residentmario/things-on-reddit) |
| Titanic | kaggle | [바로가기](https://www.kaggle.com/datasets/azeembootwala/titanic) |
| titanic | kaggle | [바로가기](https://www.kaggle.com/datasets/broaniki/titanic) |
| Titanic | kaggle | [바로가기](https://www.kaggle.com/datasets/hardikgarg03/titanic) |
| Titanic | kaggle | [바로가기](https://www.kaggle.com/datasets/heptapod/titanic) |
| Titanic | kaggle | [바로가기](https://www.kaggle.com/datasets/rahulsah06/titanic) |
| Titanic csv | kaggle | [바로가기](https://www.kaggle.com/datasets/fossouodonald/titaniccsv) |
| Titanic dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/brendan45774/test-file) |
| Titanic Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/titanic-dataset) |
| Titanic extended dataset (Kaggle + Wikipedia) | kaggle | [바로가기](https://www.kaggle.com/datasets/pavlofesenko/titanic-extended) |
| Titanic-Dataset (train.csv) | kaggle | [바로가기](https://www.kaggle.com/datasets/hesh97/titanicdataset-traincsv) |
| TMDB 5000 Movie Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) |
| TMDB Website Movie Database | kaggle | [바로가기](https://www.kaggle.com/datasets/omercolakoglu/tmdb-website-movie-database) |
| TMNIST Alphabet (94 characters) | kaggle | [바로가기](https://www.kaggle.com/datasets/nikbearbrown/tmnist-alphabet-94-characters) |
| Tomato | kaggle | [바로가기](https://www.kaggle.com/datasets/noulam/tomato) |
| Top 1000 Highest Grossing Movies | kaggle | [바로가기](https://www.kaggle.com/datasets/sanjeetsinghnaik/top-1000-highest-grossing-movies) |
| Top 50 Spotify Songs - 2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/leonardopena/top50spotify2019) |
| Top Football Leagues Scorers | kaggle | [바로가기](https://www.kaggle.com/datasets/mohamedhanyyy/top-football-leagues-scorers) |
| Top Games on Google Play Store | kaggle | [바로가기](https://www.kaggle.com/datasets/dhruvildave/top-play-store-games) |
| Top Hits Spotify from 2000-2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019) |
| Top Instagram Influencers Data (Cleaned) | kaggle | [바로가기](https://www.kaggle.com/datasets/surajjha101/top-instagram-influencers-data-cleaned) |
| Top Personality Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/arslanali4343/top-personality-dataset) |
| Top Spotify Listening History Songs in Countries | kaggle | [바로가기](https://www.kaggle.com/datasets/anandshaw2001/top-spotify-songs-in-countries) |
| Top Spotify Songs | kaggle | [바로가기](https://www.kaggle.com/datasets/arnavvvvv/spotify-music) |
| Top Spotify songs from 2010-2019 - BY YEAR | kaggle | [바로가기](https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year) |
| Top Spotify Tracks of 2017 | kaggle | [바로가기](https://www.kaggle.com/datasets/nadintamer/top-tracks-of-2017) |
| Top Spotify Tracks of 2018 | kaggle | [바로가기](https://www.kaggle.com/datasets/nadintamer/top-spotify-tracks-of-2018) |
| Top Streamers on Twitch | kaggle | [바로가기](https://www.kaggle.com/datasets/aayushmishra1512/twitchdata) |
| Toronto emotional speech set (TESS) | kaggle | [바로가기](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess) |
| Toy Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/carlolepelaars/toy-dataset) |
| Traffic Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/traffic-prediction-dataset) |
| Traffic Signs Dataset in YOLO format | kaggle | [바로가기](https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-dataset-in-yolo-format) |
| Traffic Signs Preprocessed | kaggle | [바로가기](https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-preprocessed) |
| Transit systems of world | kaggle | [바로가기](https://www.kaggle.com/datasets/citylines/city-lines) |
| Traveler Trip Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rkiattisak/traveler-trip-data) |
| Trip Advisor Restaurants Info for 31 Euro-Cities | kaggle | [바로가기](https://www.kaggle.com/datasets/damienbeneschi/krakow-ta-restaurans-data-raw) |
| Tu Simple | kaggle | [바로가기](https://www.kaggle.com/datasets/manideep1108/tusimple) |
| U.S. Educational Finances | kaggle | [바로가기](https://www.kaggle.com/datasets/noriuk/us-educational-finances) |
| U.S. Opiate Prescriptions/Overdoses | kaggle | [바로가기](https://www.kaggle.com/datasets/apryor6/us-opiate-prescriptions) |
| Uber and Lyft Dataset Boston, MA | kaggle | [바로가기](https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma) |
| Uber Data Analytics Dashboard | kaggle | [바로가기](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard) |
| Uber Fares Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset) |
| Uber Pickups in New York City | kaggle | [바로가기](https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city) |
| UCL Matches and Players Data | kaggle | [바로가기](https://www.kaggle.com/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league) |
| Udemy Courses | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/udemy-courses) |
| UFC-Fight historical data from 1993 to 2021 | kaggle | [바로가기](https://www.kaggle.com/datasets/rajeevw/ufcdata) |
| UFO Sightings | kaggle | [바로가기](https://www.kaggle.com/datasets/NUFORC/ufo-sightings) |
| Ultimate UFC Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mdabbert/ultimate-ufc-dataset) |
| Unemployment dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/pantanjali/unemployment-dataset) |
| Unicorn Startups | kaggle | [바로가기](https://www.kaggle.com/datasets/ramjasmaurya/unicorn-startups) |
| Unsupervised Learning on Country Data | kaggle | [바로가기](https://www.kaggle.com/datasets/rohan0301/unsupervised-learning-on-country-data) |
| UNSW_NB15 | kaggle | [바로가기](https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15) |
| Urban Dictionary Words And Definitions | kaggle | [바로가기](https://www.kaggle.com/datasets/therohk/urban-dictionary-words-dataset) |
| Urban Sound8K | kaggle | [바로가기](https://www.kaggle.com/datasets/chrisfilo/urbansound8k) |
| US Baby Names | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/us-baby-names) |
| US Border Crossing Data | kaggle | [바로가기](https://www.kaggle.com/datasets/divyansh22/us-border-crossing-data) |
| US Cars Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/doaaalsenani/usa-cers-dataset) |
| US Elections Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tunguz/us-elections-dataset) |
| US Mass Shootings | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/us-mass-shootings-last-50-years) |
| US Minimum Wage by State from 1968 to 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/lislejoem/us-minimum-wage-by-state-from-1968-to-2017) |
| US Permanent Visa Applications | kaggle | [바로가기](https://www.kaggle.com/datasets/jboysen/us-perm-visas) |
| US Police Shootings | kaggle | [바로가기](https://www.kaggle.com/datasets/ahsen1330/us-police-shootings) |
| US Public Food Assistance 1 - WIC | kaggle | [바로가기](https://www.kaggle.com/datasets/jpmiller/publicassistance) |
| US Traffic Fatality Records | kaggle | [바로가기](https://www.kaggle.com/datasets/usdot/nhtsa-traffic-fatalities) |
| US Unemployment Rate by County, 1990-2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/jayrav13/unemployment-by-county-us) |
| USA Name Data | kaggle | [바로가기](https://www.kaggle.com/datasets/datagov/usa-names) |
| USA Real Estate Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset) |
| Used Cars Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) |
| Used-cars-catalog | kaggle | [바로가기](https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog) |
| UTKFace | kaggle | [바로가기](https://www.kaggle.com/datasets/jangedoo/utkface-new) |
| V2 Plant Seedlings Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vbookshelf/v2-plant-seedlings-dataset) |
| Vehicle dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho) |
| VGG-16 | kaggle | [바로가기](https://www.kaggle.com/datasets/crawford/vgg16) |
| Volcanic Eruptions in the Holocene Period | kaggle | [바로가기](https://www.kaggle.com/datasets/smithsonian/volcanic-eruptions) |
| Walmart Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/walmart-dataset) |
| weight-height.csv | kaggle | [바로가기](https://www.kaggle.com/datasets/mustafaali96/weight-height) |
| Where it Pays to Attend College | kaggle | [바로가기](https://www.kaggle.com/datasets/wsj/college-salaries) |
| Who eats the food we grow? | kaggle | [바로가기](https://www.kaggle.com/datasets/dorbicycle/world-foodfeed-production) |
| Wikibooks Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/dhruvildave/wikibooks-dataset) |
| Wikipedia Movie Plots | kaggle | [바로가기](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots) |
| Wikipedia Plaintext (2023-07-01) | kaggle | [바로가기](https://www.kaggle.com/datasets/jjinho/wikipedia-20230701) |
| Wikipedia Structured Contents | kaggle | [바로가기](https://www.kaggle.com/datasets/wikimedia-foundation/wikipedia-structured-contents) |
| Win-Go, Color_Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/najeedosmani/wingo-color-prediction) |
| Windows Store | kaggle | [바로가기](https://www.kaggle.com/datasets/vishnuvarthanrao/windows-store) |
| Wine Quality | kaggle | [바로가기](https://www.kaggle.com/datasets/rajyellow46/wine-quality) |
| Wine Quality Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset) |
| World cities database | kaggle | [바로가기](https://www.kaggle.com/datasets/juanmah/world-cities) |
| World Cities Database | kaggle | [바로가기](https://www.kaggle.com/datasets/max-mind/world-cities-database) |
| World Development Indicators | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/world-development-indicators) |
| World Development Indicators | kaggle | [바로가기](https://www.kaggle.com/datasets/theworldbank/world-development-indicators) |
| World Development Indicators (WDI) Data | kaggle | [바로가기](https://www.kaggle.com/datasets/bigquery/worldbank-wdi) |
| World Educational Data | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/world-educational-data) |
| World Soccer DB: archive of odds [01-JUN-2021] | kaggle | [바로가기](https://www.kaggle.com/datasets/sashchernuh/european-football) |
| World University Rankings | kaggle | [바로가기](https://www.kaggle.com/datasets/mylesoneill/world-university-rankings) |
| Worldwide Average IQ Levels | kaggle | [바로가기](https://www.kaggle.com/datasets/abhijitdahatonde/worldwide-average-iq-levels) |
| Yelp Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset) |
| Yoga Poses Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/niharika41298/yoga-poses-dataset) |
| Zika Virus Epidemic | kaggle | [바로가기](https://www.kaggle.com/datasets/cdc/zika-virus-epidemic) |
| Zillow Economics Data | kaggle | [바로가기](https://www.kaggle.com/datasets/zillow/zecon) |
| Zomato | kaggle | [바로가기](https://www.kaggle.com/datasets/rishikeshkonapure/zomato) |
| Zomato Bangalore Restaurants | kaggle | [바로가기](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants) |
| Zomato Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchikakumbhar/zomato-dataset) |
| Zomato Restaurants Data | kaggle | [바로가기](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data) |
| Zomato Restaurants Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/abhijitdahatonde/zomato-restaurants-dataset) |
| Zoo Animals Extended Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/agajorte/zoo-animals-extended-dataset) |

### environment (총 483개)

| dataset_name | source | link |
|---|---|---|
| (EXPERIMENTAL) NOAA Four Cast Net Global Forecast System (Four Cast NetGFS) (EXPERIMENTAL) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nws-fourcastnetgfs/) |
| 10m Annual Land Use Land Cover (9-class) | aws_open_data | [바로가기](https://registry.opendata.aws/io-lulc/) |
| 3-Band Cryo Data Wide-field Infrared Survey Explorer (WISE) | aws_open_data | [바로가기](https://registry.opendata.aws/wise-cryo-3band/) |
| A Global Drought and Flood Catalogue from 1950 to 2016 | aws_open_data | [바로가기](https://registry.opendata.aws/global-drought-flood-catalogue/) |
| A region-wide, multi-year set of crop field boundary labels for Africa | aws_open_data | [바로가기](https://registry.opendata.aws/africa-field-boundary-labels/) |
| ABoVE: Bias-Corrected IMERG Monthly Precipitation for Alaska and Canada, 2000-2020 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-imergprecipcanadaalaska2097/) |
| Africa Soil Information Service (AfSIS) Soil Chemistry | aws_open_data | [바로가기](https://registry.opendata.aws/afsis/) |
| AI Weather Prediction (AIWP) Model Reforecasts | aws_open_data | [바로가기](https://registry.opendata.aws/aiwp/) |
| AIRS/Aqua L1B Infrared (IR) geolocated and calibrated radiances V005 (AIRIBRAD) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-airibrad/) |
| AIRS/Aqua L1C Infrared (IR) resampled and corrected radiances V6.7 (AIRICRAD) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-airicrad/) |
| All-Sky Data Wide-field Infrared Survey Explorer (WISE) | aws_open_data | [바로가기](https://registry.opendata.aws/wise-allsky/) |
| AllWISE Data Wide-field Infrared Survey Explorer (WISE) | aws_open_data | [바로가기](https://registry.opendata.aws/wise-allwise/) |
| Amazonia EO satellite on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/amazonia/) |
| Analysis Ready Sentinel-1 Backscatter Imagery | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel-1-rtc-indigo/) |
| ARCO-OCEAN | aws_open_data | [바로가기](https://registry.opendata.aws/ogs-arco-ocean/) |
| ASF SAR Data Products for Disaster Events | aws_open_data | [바로가기](https://registry.opendata.aws/asf-event-data/) |
| ASKAP Radio Telescope | aws_open_data | [바로가기](https://registry.opendata.aws/askap/) |
| ASTER Level 1T Precision Terrain Corrected Registered At-Sensor Radiance V004 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-astl1t/) |
| ATLAS/ICESat-2 L2A Global Geolocated Photon Data V006 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-atl03/) |
| ATLAS/ICESat-2 L3A Land and Vegetation Height V006 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-atl08/) |
| Biodiversity Heritage Library Metadata and Page Images | aws_open_data | [바로가기](https://registry.opendata.aws/bhl-open-data/) |
| Blended TROPOMI+GOSAT Satellite Data Product for Atmospheric Methane | aws_open_data | [바로가기](https://registry.opendata.aws/blended-tropomi-gosat-methane/) |
| Canopy Tree Height Map for the Amazon Forest (mean height composite 2020-2024) by CTrees.org | aws_open_data | [바로가기](https://registry.opendata.aws/ctrees-amazon-canopy-height/) |
| Capella Space Synthetic Aperture Radar (SAR) Open Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/capella_opendata/) |
| CCAFS-Climate Data | aws_open_data | [바로가기](https://registry.opendata.aws/cgiardata/) |
| Central Weather Administration Open Data | aws_open_data | [바로가기](https://registry.opendata.aws/cwa_opendata/) |
| Central Weather Bureau Open Data | aws_open_data | [바로가기](https://registry.opendata.aws/cwb_opendata/) |
| Clay v1.5 Sentinel-2 | aws_open_data | [바로가기](https://registry.opendata.aws/clay-v1-5-sentinel2/) |
| Cloud to Street - Microsoft Flood and Clouds Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/c2smsfloods/) |
| Co-Produced Climate Data to Support California's Resilience Investments | aws_open_data | [바로가기](https://registry.opendata.aws/caladapt-coproduced-climate-data/) |
| Community Earth System Model Large Ensemble (CESM LENS) | aws_open_data | [바로가기](https://registry.opendata.aws/ncar-cesm-lens/) |
| Community Earth System Model v2 ARISE (CESM2 ARISE) | aws_open_data | [바로가기](https://registry.opendata.aws/ncar-cesm2-arise/) |
| Community Earth System Model v2 Large Ensemble (CESM2 LENS) | aws_open_data | [바로가기](https://registry.opendata.aws/ncar-cesm2-lens/) |
| Community Multiscale Air Quality (CMAQ) 2019 3D Gridded and Column data from the EPA's Air Quality Time Series (EQUATES) Project | aws_open_data | [바로가기](https://registry.opendata.aws/epa-equates-v1/) |
| Conformational Space of Short Peptides | aws_open_data | [바로가기](https://registry.opendata.aws/short_peptides/) |
| Coupled Model Intercomparison Project Phase 5 (CMIP5) University of Wisconsin-Madison Probabilistic Downscaling Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-uwpd-cmip5/) |
| Crowdsourced Bathymetry | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-dcdb-bathymetry-pds/) |
| Defense Meteorology Satellite Program (DMSP) Auroral Particle Flux | aws_open_data | [바로가기](https://registry.opendata.aws/dmspssj/) |
| Department of Energy's Geothermal Data Repository (GDR) Data Lake | aws_open_data | [바로가기](https://registry.opendata.aws/gdr-data-lake/) |
| Department of Energy's Marine Energy Data Lake | aws_open_data | [바로가기](https://registry.opendata.aws/marine-energy-data/) |
| Department of Energy's Open Energy Data Initiative (OEDI) | aws_open_data | [바로가기](https://registry.opendata.aws/oedi-data-lake/) |
| Digital Earth Africa - Copernicus Global Land Service - Lake Water Quality | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-clgm-lwq/) |
| Digital Earth Africa ALOS PALSAR, ALOS-2 PALSAR-2 and JERS-1 | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-alos-jers/) |
| Digital Earth Africa CHIRPS Rainfall | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-chirps/) |
| Digital Earth Africa Coastlines | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-coastlines/) |
| Digital Earth Africa Cropland Extent Map (2019) | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-crop-extent/) |
| Digital Earth Africa Fractional Cover | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-fractional-cover/) |
| Digital Earth Africa GeoMAD | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-geomad/) |
| Digital Earth Africa Global Mangrove Watch | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-mangrove/) |
| Digital Earth Africa Landsat Collection 2 Level 2 | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-landsat/) |
| Digital Earth Africa Monthly Normalised Difference Vegetation Index (NDVI) Anomaly | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-ndvi_anomaly/) |
| Digital Earth Africa Normalised Difference Vegetation Index (NDVI) Climatology | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-ndvi_climatology_ls/) |
| Digital Earth Africa Sentinel-1 Radiometrically Terrain Corrected | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-sentinel-1/) |
| Digital Earth Africa Sentinel-2 Level-2A | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-sentinel-2/) |
| Digital Earth Africa Sentinel-2 Level-2A Surface Reflectance Collection 1 | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-sentinel-2-c1/) |
| Digital Earth Africa Water Observations from Space | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-wofs/) |
| Digital Earth Pacific Mangroves Extent and Density | aws_open_data | [바로가기](https://registry.opendata.aws/dep-mangroves/) |
| Digital Earth Pacific Water Observatins from Space (WOfS) | aws_open_data | [바로가기](https://registry.opendata.aws/dep-wofs/) |
| DOE's Water Power Technology Office's (WPTO) US Wave dataset | aws_open_data | [바로가기](https://registry.opendata.aws/wpto-pds-us-wave/) |
| Downscaled Climate Data for Alaska (v1.1, August 2023) | aws_open_data | [바로가기](https://registry.opendata.aws/wrf-alaska-snap/) |
| Earth Observation Data Cubes for Brazil | aws_open_data | [바로가기](https://registry.opendata.aws/brazil-data-cubes/) |
| Earth Radio Occultation | aws_open_data | [바로가기](https://registry.opendata.aws/gnss-ro-opendata/) |
| Ensemble Meteorological Dataset for Planet Earth, EM-Earth | aws_open_data | [바로가기](https://registry.opendata.aws/emearth/) |
| ESA World Cover Sentinel-1 and Sentinel-2 10m Annual Composites | aws_open_data | [바로가기](https://registry.opendata.aws/esa-worldcover-vito-composites/) |
| Finnish Meteorological Institute Weather Radar Data | aws_open_data | [바로가기](https://registry.opendata.aws/fmi-radar/) |
| Galaxy Evolution Explorer Satellite (GALEX) | aws_open_data | [바로가기](https://registry.opendata.aws/mast-galex/) |
| GEDI L2A Elevation and Height Metrics Data Global Footprint Level V002 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gedi02a/) |
| GEDI L4A Footprint Level Aboveground Biomass Density, Version 2.1 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gedil4aagbdensityv212056/) |
| Geosnap Data, Center for Geospatial Sciences | aws_open_data | [바로가기](https://registry.opendata.aws/spatial-ucr/) |
| GHRSST Level 2P Global Sea Surface Skin Temperature from the MODIS on the NASA Terra satellite (GDS2) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-modis-t-jpl-l2p-v2019-0/) |
| GHRSST Level 4 MUR Global Foundation Sea Surface Temperature Analysis (v4.1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mur-jpl-l4-glob-v41/) |
| GLAD Landsat ARD | aws_open_data | [바로가기](https://registry.opendata.aws/glad-landsat-ard/) |
| Global Biodiversity Information Facility (GBIF) Species Occurrences | aws_open_data | [바로가기](https://registry.opendata.aws/gbif/) |
| Global Seasonal Sentinel-1 Interferometric Coherence and Backscatter Data Set | aws_open_data | [바로가기](https://registry.opendata.aws/ebd-sentinel-1-global-coherence-backscatter/) |
| Google Satellite Embedding V1 | aws_open_data | [바로가기](https://registry.opendata.aws/aef-source/) |
| GPM DPR Precipitation Profile L2A 1.5 hours 5 km V07 (GPM_2ADPR) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpm2adpr/) |
| GPM IMERG Early Precipitation L3 1 day 0.1 degree x 0.1 degree V07 (GPM_3IMERGDE) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpm3imergde/) |
| GPM IMERG Early Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHHE) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpm3imerghhe/) |
| GPM IMERG Final Precipitation L3 1 day 0.1 degree x 0.1 degree V07 (GPM_3IMERGDF) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpm3imergdf/) |
| GPM IMERG Final Precipitation L3 1 month 0.1 degree x 0.1 degree V07 (GPM_3IMERGM) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpm3imergm/) |
| GPM IMERG Final Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHH) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpm3imerghh/) |
| GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V07 (GPM_3IMERGDL) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpm3imergdl/) |
| GPM IMERG Late Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHHL) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpm3imerghhl/) |
| High Resolution Downscaled Climate Data for Southeast Alaska | aws_open_data | [바로가기](https://registry.opendata.aws/wrf-se-alaska-snap/) |
| HIRLAM Weather Model | aws_open_data | [바로가기](https://registry.opendata.aws/hirlam/) |
| HLS Landsat Operational Land Imager Surface Reflectance and TOA Brightness Daily Global 30m v2.0 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-hlsl30/) |
| HLS Sentinel-2 Multi-spectral Instrument Surface Reflectance Daily Global 30m v2.0 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-hlss30/) |
| Hubble Space Telescope | aws_open_data | [바로가기](https://registry.opendata.aws/mast-hst/) |
| HYbrid Coordinate Ocean Model Global Ocean Forecast System Reanalysis | aws_open_data | [바로가기](https://registry.opendata.aws/hycom-gofs-3pt1-reanalysis/) |
| HYCOM-Ocean Track Integrated HYCOM Eulerian Fields and Lagrangian Trajectories Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/hycom-global-drifters/) |
| James Webb Space Telescope (JWST) | aws_open_data | [바로가기](https://registry.opendata.aws/mast-jwst/) |
| JAXA /USGS /NASA Kaguya/SELENE Terrain Camera Digital Terrain Models | aws_open_data | [바로가기](https://registry.opendata.aws/jaxa-usgs-nasa-kaguya-tc-dtms/) |
| JAXA /USGS /NASA Kaguya/SELENE Terrain Camera Observations | aws_open_data | [바로가기](https://registry.opendata.aws/jaxa-usgs-nasa-kaguya-tc/) |
| JMA Himawari-8/9 | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-himawari/) |
| Korea Meteorological Administration (KMA) GK-2A Satellite Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-gk2a-pds/) |
| Land/Sea static mask relevant to IMERG precipitation 0.1x0.1 degree V2 (GPM_IMERG_Land Sea Mask) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpmimerglandseamask/) |
| Landsat Geometric Median and Absolute Deviations (GeoMAD) over the Pacific | aws_open_data | [바로가기](https://registry.opendata.aws/dep-ls-geomads/) |
| LGND Clay v1.5 Sentinel-2 | aws_open_data | [바로가기](https://registry.opendata.aws/lgnd-clay-v1-5-sentinel2/) |
| Low Altitude Disaster Imagery (LADI) Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ladi/) |
| Marine Animal - Satellite Relay Tagging - Quality controlled profiles | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_animal_ctd_satellite_relay_tagging_delayed_qc/) |
| Mars Spectrometry 2: Gas Chromatography for the Sample Analysis at Mars Data (SAM) Instrument | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gcms/) |
| Mars Spectrometry: Detect Evidence for Past Habitability | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-ega/) |
| MERRA-2 inst3_3d_aer_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Aerosol Mixing Ratio 0.625 x 0.5 degree | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-m2i3nvaer/) |
| MERRA-2 inst3_3d_asm_Np: 3d,3-Hourly,Instantaneous,Pressure-Level,Assimilation,Assimilated Meteorological Fields | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-m2i3npasm/) |
| MERRA-2 inst3_3d_asm_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Assimilated Meteorological Fields 0.625 x 0.5 degree | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-m2i3nvasm/) |
| MERRA-2 tavg1_2d_slv_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-m2t1nxslv/) |
| Met Office Global Ocean model on a 2-year rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-global-ocean/) |
| Met Office NWS Ocean model on a 2-year rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-nws-ocean/) |
| Met Office UK Earth System Model (UKESM1) ARISE-SAI geoengineering experiment data | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-ukesm1-arise/) |
| MISR Level 1B2 Ellipsoid Data V004 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mi1b2e/) |
| MODIS/Aqua Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-myd09ga/) |
| MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-myd09gq/) |
| MODIS/Terra Calibrated Radiances 5-Min L1B Swath 500m | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mod02hkm/) |
| MODIS/Terra Net Evapotranspiration 8-Day L4 Global 500m SIN Grid V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mod16a2/) |
| MODIS/Terra Surface Reflectance 8-Day L3 Global 500m SIN Grid V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mod09a1/) |
| MODIS/Terra Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mod09ga/) |
| MODIS/Terra Surface Reflectance Daily L2G Global 250m SIN Grid V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mod09gq/) |
| MODIS/Terra Vegetation Indices 16-Day L3 Global 250m SIN Grid V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mod13q1/) |
| MODIS/Terra+Aqua BRDF/Albedo Albedo Daily L3 Global - 500m V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mcd43a3/) |
| MODIS/Terra+Aqua BRDF/Albedo Model Parameters Daily L3 Global - 500m V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mcd43a1/) |
| MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global - 500m V061 | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-mcd43a4/) |
| Multi-Scale Ultra High Resolution (MUR) Sea Surface Temperature (SST) | aws_open_data | [바로가기](https://registry.opendata.aws/mur/) |
| NASA /USGS Controlled Europa DTMs | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-usgs-europa-dtms/) |
| NASA /USGS Controlled THEMIS Mosaics | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-usgs-themis-mosaics/) |
| NASA /USGS Europa Controlled Observation Mosaics | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-usgs-europa-mosaics/) |
| NASA /USGS Europa Controlled Observations | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-usgs-europa-observations/) |
| NASA /USGS Lunar Orbiter Laser Altimeter Cloud Optimized Point Cloud | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-usgs-lunar-orbiter-laser-altimeter/) |
| NASA /USGS Mars Reconnaissance Orbiter (MRO) Context Camera (CTX) Targeted DTMs | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-usgs-controlled-mro-ctx-dtms/) |
| NASA /USGS Released HiRISE Digital Terrain Models | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-usgs-mars-hirise-dtms/) |
| NASA /USGS Uncontrolled HiRISE RDRs | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-usgs-mars-hirise/) |
| NASA Earth Exchange (NEX) Data Collection | aws_open_data | [바로가기](https://registry.opendata.aws/nasanex/) |
| NASA Earth Exchange Global Daily Downscaled Projections (NEX-GDDP-CMIP6) | aws_open_data | [바로가기](https://registry.opendata.aws/nex-gddp-cmip6/) |
| NASA High Energy Astrophysics Mission Data | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-heasarc/) |
| NASA Legacy Archive for Microwave Background Data Analysis (LAMBDA) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-lambda/) |
| NASA Physical Sciences Informatics (PSI) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-psi/) |
| NASA Prediction of Worldwide Energy Resources (POWER) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-power/) |
| NASA SOTERIA Simulation Testbed Data | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-soteria-data/) |
| NASA Space Biology Open Science Data Repository (OSDR) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-osdr/) |
| National Climate Database (NCDB) | aws_open_data | [바로가기](https://registry.opendata.aws/nrel-pds-ncdb/) |
| Natural Earth | aws_open_data | [바로가기](https://registry.opendata.aws/naturalearth/) |
| NCEP/CPC L3 Half Hourly 4km Global (60S - 60N) Merged IR V1 (GPM_MERGIR) at GES DISC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-gpmmergir/) |
| NEOWISE Post-Cryo Data Wide-field Infrared Survey Explorer (WISE) | aws_open_data | [바로가기](https://registry.opendata.aws/wise-postcryo/) |
| NEOWISE Reactivation Data Near-Earth Object Wide-field Infrared Survey Explorer (NEOWISE) | aws_open_data | [바로가기](https://registry.opendata.aws/wise-neowiser/) |
| NEXRAD on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nexrad/) |
| Nighttime-Fire-Flare | aws_open_data | [바로가기](https://registry.opendata.aws/black_marble_combustion/) |
| NOAA - hourly position, current, and sea surface temperature from drifters | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-oar-hourly-gdp/) |
| NOAA /NGA Satellite Computed Bathymetry Assessment-SCuBA | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nos-scuba-icesat2-pds/) |
| NOAA 3-D Surge and Tide Operational Forecast System for the Atlantic Basin (STOFS-3D-Atlantic) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nos-stofs3d/) |
| NOAA Analysis of Record for Calibration (AORC) Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nws-aorc/) |
| NOAA Atmospheric Climate Data Records | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-cdr-atmospheric/) |
| NOAA Climate Forecast System (CFS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-cfs/) |
| NOAA Cloud Optimized Zarr Reference Files (Kerchunk) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nodd-kerchunk/) |
| NOAA Coastal Lidar Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-coastal-lidar/) |
| NOAA Continuously Operating Reference Stations (CORS) Network (NCN) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ncn/) |
| NOAA EAGLE (Experimental AI Global and Limited-Area Ensemble) Global Deterministic and Ensemble Forecasts | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nws-graphcastgfs-pds/) |
| NOAA Emergency Response Imagery | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-eri/) |
| NOAA Fundamental Climate Data Records (FCDR) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-cdr-fundamental/) |
| NOAA GEFS - dynamical.org Icechunk Zarr | aws_open_data | [바로가기](https://registry.opendata.aws/dynamical-noaa-gefs/) |
| NOAA Geostationary Operational Environmental Satellites (GOES) 16, 17, 18 and 19 | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-goes/) |
| NOAA GFS - dynamical.org Icechunk Zarr | aws_open_data | [바로가기](https://registry.opendata.aws/dynamical-noaa-gfs/) |
| NOAA Global Data Assimilation (DA) Test Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-gdas-pds/) |
| NOAA Global Ensemble Forecast System (GEFS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-gefs/) |
| NOAA Global Ensemble Forecast System (GEFS) Re-forecast | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-gefs-reforecast/) |
| NOAA Global Forecast System (GFS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-gfs-bdp-pds/) |
| NOAA Global Forecast System (GFS) netCDF Formatted Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-oar-arl-nacc-pds/) |
| NOAA Global Historical Climatology Network Daily (GHCN-D) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ghcn/) |
| NOAA Global Hydro Estimator (GHE) /Enterprise Rain Rate | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ghe/) |
| NOAA Global Mosaic of Geostationary Satellite Imagery (GMGSI) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-gmgsi/) |
| NOAA Global Real-Time Ocean Forecast System (Global RTOFS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-rtofs/) |
| NOAA Global Surface Summary of Day | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-gsod/) |
| NOAA Global Surge and Tide Operational Forecast System 2-D (STOFS-2D-Global) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-gestofs/) |
| NOAA High-Resolution Rapid Refresh (HRRR) Model | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-hrrr-pds/) |
| NOAA Historical Maps and Charts | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-historicalcharts/) |
| NOAA HRRR - dynamical.org Icechunk Zarr | aws_open_data | [바로가기](https://registry.opendata.aws/dynamical-noaa-hrrr/) |
| NOAA Hurricane Analysis and Forecast System (HAFS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nws-hafs/) |
| NOAA HYSPLIT-compatible meteorological data archives | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-arl-hysplit/) |
| NOAA Integrated Surface Database (ISD) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-isd/) |
| NOAA Joint Polar Satellite System (JPSS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-jpss/) |
| NOAA Multi-Radar/Multi-Sensor System (MRMS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-mrms-pds/) |
| NOAA Multi-Year Reanalysis of Remotely Sensed Storms (MYRORSS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-oar-myrorss-pds/) |
| NOAA n Clim Grid and Livneh Gridded Historical Climate Observation Thresholds | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-cris-hist/) |
| NOAA NASA Joint Archive (NNJA) of Observations for Earth System Reanalysis | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-reanalyses-pds/) |
| NOAA National Air Quality Forecast Capability (NAQFC) Regional Model Guidance | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nws-naqfc-pds/) |
| NOAA National Bathymetric Source Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-bathymetry/) |
| NOAA National Blend of Models (NBM) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nbm/) |
| NOAA National Blend of Models (NBM) Parallel | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nbm-parallel/) |
| NOAA National Digital Forecast Database (NDFD) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ndfd/) |
| NOAA National Water Model CONUS Retrospective Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/nwm-archive/) |
| NOAA National Water Model Short-Range Forecast | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nwm-pds/) |
| NOAA North American Mesoscale Forecast System (NAM) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nam/) |
| NOAA Oceanic Climate Data Records | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-cdr-oceanic/) |
| NOAA Office of Coast Survey - Hydrographic Survey Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ocs-hydrodata/) |
| NOAA Operational Forecast System (OFS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ofs/) |
| NOAA Rapid Refresh (RAP) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-rap/) |
| NOAA Rapid Refresh Forecast System (RRFS) [Prototype] | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-rrfs/) |
| NOAA Real-Time Mesoscale Analysis (RTMA) /Unrestricted Mesoscale Analysis (URMA) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-rtma/) |
| NOAA S-102 Bathymetric Surface Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-s102/) |
| NOAA S-104 Water Level Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-s104/) |
| NOAA S-111 Surface Water Currents Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-s111/) |
| NOAA Severe Weather Data Inventory (SWDI) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-swdi/) |
| NOAA Space Weather Follow-On Mission Geostationary Operational Environmental Satellite (GOES) 19 | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nesdis-swfo-ccor-1-pds/) |
| NOAA Space Weather Forecast and Observation Data | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-space-weather/) |
| NOAA Terrestrial Climate Data Records | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-cdr-terrestrial/) |
| NOAA U.S. Climate Gridded Dataset (NClim Grid) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nclimgrid/) |
| NOAA U.S. Climate Normals | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-climate-normals/) |
| NOAA Unified Forecast System (UFS) Coastal Model | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-coastal-pds/) |
| NOAA Unified Forecast System (UFS) Global Ensemble Forecast System (GEFS) Version 13 Replay | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-gefsv13replay-pds/) |
| NOAA Unified Forecast System (UFS) Hierarchical Testing Framework (HTF) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-htf-pds/) |
| NOAA Unified Forecast System (UFS) Land Data Assimilation (DA) System | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-land-da/) |
| NOAA Unified Forecast System (UFS) Marine Reanalysis: 1979-2019 | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-marinereanalysis/) |
| NOAA Unified Forecast System Short-Range Weather (UFS SRW) Application | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-shortrangeweather/) |
| NOAA Unified Forecast System Subseasonal to Seasonal Prototypes | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-s2s/) |
| NOAA Unified Forecast System Weather Model (UFS-WM) Regression Tests | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ufs-regtests/) |
| NOAA Wang Sheeley Arge (WSA) Enlil | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-wsa-enlil/) |
| NOAA Water-Column Sonar Data Archive | aws_open_data | [바로가기](https://registry.opendata.aws/ncei-wcsd-archive/) |
| NOAA Wave Ensemble Reforecast | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-wave-ensemble-reforecast/) |
| NOAA Whole Atmosphere Model-Ionosphere Plasmasphere Electrodynamics (WAM-IPE) Forecast System (WFS) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nws-wam-ipe/) |
| NOAA World Ocean Database (WOD) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-wod/) |
| NOAA's Coastal Ocean Reanalysis (CORA) Dataset: 1979-2022 | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nos-cora/) |
| NOAA/PMEL Ocean Climate Stations Moorings | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-ocean-climate-stations/) |
| Northern California Earthquake Data | aws_open_data | [바로가기](https://registry.opendata.aws/northern-california-earthquakes/) |
| NREL National Solar Radiation Database | aws_open_data | [바로가기](https://registry.opendata.aws/nrel-pds-nsrdb/) |
| NREL Wind Integration National Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/nrel-pds-wtk/) |
| NUVIEW - Multi-State Geospatial Data | aws_open_data | [바로가기](https://registry.opendata.aws/nuview-state/) |
| Ocean Biodiversity Information System (OBIS) species occurrence data | aws_open_data | [바로가기](https://registry.opendata.aws/obis/) |
| Ocean Current - Gridded sea level anomaly - Near real time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_model_sea_level_anomaly_gridded_realtime/) |
| Ocean Gliders - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_slocum_glider_delayed_qc/) |
| Ocean Omics | aws_open_data | [바로가기](https://registry.opendata.aws/oceanomics/) |
| Ocean Radar - Bonney coast site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_bonneycoast_velocity_hourly_averaged_delayed_qc/) |
| Ocean Radar - Capricorn bunker group site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_capricornbunkergroup_velocity_hourly_averaged_delayed_qc/) |
| Ocean Radar - Capricorn bunker group site - Wave - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_capricornbunkergroup_wave_delayed_qc/) |
| Ocean Radar - Capricorn bunker group site - Wind - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_capricornbunkergroup_wind_delayed_qc/) |
| Ocean Radar - Coffs Harbour site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_coffsharbour_velocity_hourly_averaged_delayed_qc/) |
| Ocean Radar - Coffs Harbour site - Wave - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_coffsharbour_wave_delayed_qc/) |
| Ocean Radar - Coffs Harbour site - Wind - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_coffsharbour_wind_delayed_qc/) |
| Ocean Radar - Coral coast site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_coralcoast_velocity_hourly_averaged_delayed_qc/) |
| Ocean Radar - Newcastle site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_newcastle_velocity_hourly_averaged_delayed_qc/) |
| Ocean Radar - Northwest shelf site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_northwestshelf_velocity_hourly_averaged_delayed_qc/) |
| Ocean Radar - Rottnest shelf site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_rottnestshelf_velocity_hourly_averaged_delayed_qc/) |
| Ocean Radar - Rottnest shelf site - Wave - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_rottnestshelf_wave_delayed_qc/) |
| Ocean Radar - Rottnest shelf site - Wind - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_rottnestshelf_wind_delayed_qc/) |
| Ocean Radar - South Australian gulfs site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_southaustraliagulfs_velocity_hourly_averaged_delayed_qc/) |
| Ocean Radar - South Australian gulfs site - Wave - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_southaustraliagulfs_wave_delayed_qc/) |
| Ocean Radar - South Australian gulfs site - Wind - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_southaustraliagulfs_wind_delayed_qc/) |
| Ocean Radar - Turquoise coast site - Sea water velocity - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_radar_turquoisecoast_velocity_hourly_averaged_delayed_qc/) |
| Open-Meteo Weather API Database | aws_open_data | [바로가기](https://registry.opendata.aws/open-meteo/) |
| OPERA Coregistered Single-Look Complex from Sentinel-1 Static Layers validated product (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal2cslc-s1-staticv1/) |
| OPERA Coregistered Single-Look Complex from Sentinel-1 validated product (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal2cslc-s1v1/) |
| OPERA Dynamic Surface Water Extent from Harmonized Landsat Sentinel-2 product (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal3dswx-hlsv1/) |
| OPERA Dynamic Surface Water Extent from Sentinel-1 (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal3dswx-s1v1/) |
| OPERA Land Surface Disturbance Alert from Harmonized Landsat Sentinel-2 product (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal3dist-alert-hlsv1/) |
| OPERA Land Surface Disturbance Alert from Harmonized Landsat Sentinel-2 provisional product (Version 0) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal3dist-alert-hlsprovisionalv0/) |
| OPERA Land Surface Disturbance Annual from Harmonized Landsat Sentinel-2 product (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal3dist-ann-hlsv1/) |
| OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 Static Layers validated product (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal2rtc-s1-staticv1/) |
| OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 validated product (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal2rtc-s1v1/) |
| OPERA Surface Displacement from Sentinel-1 validated product (Version 1) | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-operal3disp-s1v1/) |
| OS-Climate Physrisk | aws_open_data | [바로가기](https://registry.opendata.aws/os-climate-physrisk/) |
| Ozone Monitoring Instrument (OMI) /Aura NO2 Tropospheric Column Density | aws_open_data | [바로가기](https://registry.opendata.aws/omi-no2-nasa/) |
| Pacific Ocean Sound Recordings | aws_open_data | [바로가기](https://registry.opendata.aws/pacific-sound/) |
| PALSAR-2 ScanSAR Turkey and Syria Earthquake (L2.1 and L1.1) | aws_open_data | [바로가기](https://registry.opendata.aws/palsar2-scansar-turkey-syria/) |
| Rain over Africa | aws_open_data | [바로가기](https://registry.opendata.aws/roa/) |
| RAPID NRT Flood Maps | aws_open_data | [바로가기](https://registry.opendata.aws/rapid-nrt-flood-maps/) |
| Satellite - Altimetry calibration and validation | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_mooring_satellite_altimetry_calibration_validation/) |
| Satellite - Ocean Colour - MODIS - 1 day - Chlorophyll-a concentration (Carder model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_carder_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Chlorophyll-a concentration (GSM model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_gsm_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Chlorophyll-a concentration (OC3 model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_oc3_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Chlorophyll-a concentration (OCI model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_oci_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Diffuse attenuation coefficient (k490) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_diffuse_attenuation_coefficent_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Nanoplankton fraction (OC3 model and Brewin et al 2012 algorithm) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_nanoplankton_fraction_oc3_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Net Primary Productivity (GSM model and Eppley-VGPM algorithm) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_net_primary_productivity_gsm_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Net Primary Productivity (OC3 model and Eppley-VGPM algorithm) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_net_primary_productivity_oc3_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Optical Water Type (Moore et al 2009 algorithm) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_optical_water_type_1day_aqua/) |
| Satellite - Ocean Colour - MODIS - 1 day - Picoplankton fraction (OC3 model and Brewin et al 2012 algorithm) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_picoplankton_fraction_oc3_1day_aqua/) |
| Satellite - Ocean Colour - NOAA20 - 1 day - Chlorophyll-a concentration (GSM model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_gsm_1day_noaa20/) |
| Satellite - Ocean Colour - NOAA20 - 1 day - Chlorophyll-a concentration (OC3 model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_oc3_1day_noaa20/) |
| Satellite - Ocean Colour - NOAA20 - 1 day - Chlorophyll-a concentration (OCI model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_oci_1day_noaa20/) |
| Satellite - Ocean Colour - NOAA20 - 1 day - Diffuse attenuation coefficient (k490) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_diffuse_attenuation_coefficent_1day_noaa20/) |
| Satellite - Ocean Colour - SNPP - 1 day - Chlorophyll-a concentration (GSM model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_gsm_1day_snpp/) |
| Satellite - Ocean Colour - SNPP - 1 day - Chlorophyll-a concentration (OC3 model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_oc3_1day_snpp/) |
| Satellite - Ocean Colour - SNPP - 1 day - Chlorophyll-a concentration (OCI model) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_chlorophylla_oci_1day_snpp/) |
| Satellite - Ocean Colour - SNPP - 1 day - Diffuse attenuation coefficient (k490) | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_diffuse_attenuation_coefficent_1day_snpp/) |
| Satellite - Sea surface temperature - Level 3 - Multi sensor - 1 day - Day and night time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l3s_1day_daynighttime_multi_sensor_australia/) |
| Satellite - Sea surface temperature - Level 3 - Multi sensor - 3 day - Day and night time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l3s_3day_daynighttime_multi_sensor_australia/) |
| Satellite - Sea surface temperature - Level 3 - Single sensor - 1 day - Day and night time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l3s_1day_daynighttime_single_sensor_australia/) |
| Satellite - Sea surface temperature - Level 3 - Single sensor - 1 day - Day and night time - Southern Ocean | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l3s_1day_daynighttime_single_sensor_southernocean/) |
| Satellite - Sea surface temperature - Level 3 - Single sensor - 1 month - Day time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l3s_1month_daytime_single_sensor_australia/) |
| Satellite - Sea surface temperature - Level 3 - Single sensor - 6 day - Day and night time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l3s_6day_daynighttime_single_sensor_australia/) |
| Satellite - Sea surface temperature - Level 3 - Single sensor - Himawari-8 - 1 day - Night time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l3c_1day_nighttime_himawari8/) |
| Satellite - Sea surface temperature - Level 4 - Multi sensor - Global Australian | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l4_gamssa_1day_multi_sensor_world/) |
| Satellite - Sea surface temperature - Level 4 - Multi sensor - Regional Australian | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_satellite_ghrsst_l4_ramssa_1day_multi_sensor_australia/) |
| Satellogic Earth View dataset | aws_open_data | [바로가기](https://registry.opendata.aws/satellogic-earthview/) |
| Sea Around Us Global Fisheries Catch Data | aws_open_data | [바로가기](https://registry.opendata.aws/sau-global-fisheries-catch-data/) |
| Sea Surface Temperature Daily Analysis: European Space Agency Climate Change Initiative product version 2.1 | aws_open_data | [바로가기](https://registry.opendata.aws/surftemp-sst/) |
| Sentinel Near Real-time Canada Mirror Miroir Sentinel temps quasi reel du Canada | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel-products-ca-mirror/) |
| Sentinel-1 | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel-1/) |
| Sentinel-1 Mean and Median Annual Mosaic | aws_open_data | [바로가기](https://registry.opendata.aws/dep-s1-annual-mosaics/) |
| Sentinel-1 Monthly Mosaic | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-sentinel-1-mosaic/) |
| Sentinel-1 Precise Orbit Determination (POD) Products | aws_open_data | [바로가기](https://registry.opendata.aws/s1-orbits/) |
| Sentinel-1 SLC dataset for Germany | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel1-slc/) |
| Sentinel-1 SLC dataset for South and Southeast Asia, Taiwan, Korea and Japan | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel1-slc-seasia-pds/) |
| SENTINEL-1A_DUAL_POL_GRD_HIGH_RES | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-sentinel-1adpgrdhigh/) |
| SENTINEL-1A_SLC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-sentinel-1aslc/) |
| SENTINEL-1B_DUAL_POL_GRD_HIGH_RES | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-sentinel-1bdpgrdhigh/) |
| SENTINEL-1B_SLC | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-sentinel-1bslc/) |
| Sentinel-2 | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel-2/) |
| Sentinel-2 ACOLITE-DSF Aquatic Reflectance for the Conterminous United States | aws_open_data | [바로가기](https://registry.opendata.aws/usgs_aqr/) |
| Sentinel-2 Cloud-Optimized GeoTIFFs | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel-2-l2a-cogs/) |
| Sentinel-2 Geometric Median and Absolute Deviations (GeoMAD) over the Pacific | aws_open_data | [바로가기](https://registry.opendata.aws/dep-s2-geomads/) |
| Sentinel-2 L2A 120m Mosaic | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel-s2-l2a-mosaic-120/) |
| Sentinel-3 | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel-3/) |
| Sentinel-5P Level 2 | aws_open_data | [바로가기](https://registry.opendata.aws/sentinel5p/) |
| Ships of Opportunity - Air-sea fluxes - Meteorological and flux - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_vessel_air_sea_flux_product_delayed/) |
| Ships of Opportunity - Air-sea fluxes - Meteorological and sea surface temperature - Real time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_vessel_air_sea_flux_sst_meteo_realtime/) |
| Ships of Opportunity - Biogeochemical sensors - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_vessel_co2_delayed_qc/) |
| Ships of Opportunity - Sea surface temperature - 1-minute average data products | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_vessel_sst_delayed_qc/) |
| SILAM Air Quality | aws_open_data | [바로가기](https://registry.opendata.aws/silam/) |
| SILO climate data on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/silo/) |
| SMN Hi-Res Weather Forecast over Argentina | aws_open_data | [바로가기](https://registry.opendata.aws/smn-ar-wrf-dataset/) |
| Solar Dynamics Observatory (SDO) Machine Learning Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/sdoml-fdl/) |
| Southern California Earthquake Data | aws_open_data | [바로가기](https://registry.opendata.aws/southern-california-earthquakes/) |
| Space Eye-T VVHR EO Open Data | aws_open_data | [바로가기](https://registry.opendata.aws/st-open-data/) |
| Space Net | aws_open_data | [바로가기](https://registry.opendata.aws/spacenet/) |
| Spatiam Corporation National Lab Research Announcement International Space Station Technology Demonstration | aws_open_data | [바로가기](https://registry.opendata.aws/spatiam-nlra-iss-experiments/) |
| SSL4EO S12 Landsat Multi Product Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ssl4eo-multi-product-data/) |
| Storm EVent Image Ry (SEVIR) | aws_open_data | [바로가기](https://registry.opendata.aws/sevir/) |
| Transiting Exoplanet Survey Satellite (TESS) | aws_open_data | [바로가기](https://registry.opendata.aws/mast-tess/) |
| Tropical Cyclone Precipitation, Infrared, Microwave, and Environmental Dataset (TC PRIMED) | aws_open_data | [바로가기](https://registry.opendata.aws/noaa-nesdis-tcprimed-pds/) |
| Unblurred Coadds of the Wide-field Infrared Survey Explorer (unWISE) | aws_open_data | [바로가기](https://registry.opendata.aws/wise-unwise/) |
| USGS COAWST (Coupled Ocean Atmosphere Wave and Sediment Transport) Forecast Model Archive, US East and Gulf Coasts | aws_open_data | [바로가기](https://registry.opendata.aws/coawst/) |
| USGS Landsat | aws_open_data | [바로가기](https://registry.opendata.aws/usgs-landsat/) |
| Vermont Open Geospatial on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/vt-opendata/) |
| Wildfire Projections to Support Climate Resilience | aws_open_data | [바로가기](https://registry.opendata.aws/caladapt-wildfire-dataset/) |
| Wind AI Bench | aws_open_data | [바로가기](https://registry.opendata.aws/nrel-pds-windai/) |
| us-weather-history | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/us-weather-history) |
| weather-check | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/weather-check) |
| 1.88 Million US Wildfires | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires) |
| 2016 Global Ecological Footprint | kaggle | [바로가기](https://www.kaggle.com/datasets/footprintnetwork/ecological-footprint) |
| 38-Cloud: Cloud Segmentation in Satellite Images | kaggle | [바로가기](https://www.kaggle.com/datasets/sorour/38cloud-cloud-segmentation-in-satellite-images) |
| A Large Scale Fish Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/crowww/a-large-scale-fish-dataset) |
| AAU Rain Snow Traffic Surveillance Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/aalborguniversity/aau-rainsnow) |
| Acoustic Extinguisher Fire Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/acoustic-extinguisher-fire-dataset) |
| African Wildlife | kaggle | [바로가기](https://www.kaggle.com/datasets/biancaferreira/african-wildlife) |
| Agriculture crop images | kaggle | [바로가기](https://www.kaggle.com/datasets/aman2000jaiswal/agriculture-crop-images) |
| Agriculture Crop Production In India | kaggle | [바로가기](https://www.kaggle.com/datasets/srinivas1/agricuture-crops-production-in-india) |
| Air Pollution in Seoul | kaggle | [바로가기](https://www.kaggle.com/datasets/bappekim/air-pollution-in-seoul) |
| Air Quality and Pollution Assessment | kaggle | [바로가기](https://www.kaggle.com/datasets/mujtabamatin/air-quality-and-pollution-assessment) |
| Air Quality Data in India (2015 - 2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india) |
| Air Quality Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set) |
| Air Quality in Madrid (2001-2018) | kaggle | [바로가기](https://www.kaggle.com/datasets/decide-soluciones/air-quality-madrid) |
| Air Quality Index of Bangladesh Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/air-quality-index-of-bangladesh-dataset) |
| Aircraft Wildlife Strikes, 1990-2015 | kaggle | [바로가기](https://www.kaggle.com/datasets/faa/wildlife-strikes) |
| All Agriculture related Datasets for India | kaggle | [바로가기](https://www.kaggle.com/datasets/thammuio/all-agriculture-related-datasets-for-india) |
| All Space Missions from 1957 | kaggle | [바로가기](https://www.kaggle.com/datasets/agirlcoding/all-space-missions-from-1957) |
| Appliances Energy Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/loveall/appliances-energy-prediction) |
| Arabidopsis thaliana Short Reads | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/district-wise-crop-production-statistics) |
| Austin Weather | kaggle | [바로가기](https://www.kaggle.com/datasets/grubenm/austin-weather) |
| Biodiversity in National Parks | kaggle | [바로가기](https://www.kaggle.com/datasets/nationalparkservice/park-biodiversity) |
| Chennai Water Management | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/chennai-water-management) |
| Climate change Indicators | kaggle | [바로가기](https://www.kaggle.com/datasets/tarunrm09/climate-change-indicators) |
| Climate Change: Earth Surface Temperature Data | kaggle | [바로가기](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) |
| Climate Weather Surface of Brazil - Hourly | kaggle | [바로가기](https://www.kaggle.com/datasets/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region) |
| CO2 and GHG emission data | kaggle | [바로가기](https://www.kaggle.com/datasets/srikantsahu/co2-and-ghg-emission-data) |
| CO2 Emission by Vehicles | kaggle | [바로가기](https://www.kaggle.com/datasets/debajyotipodder/co2-emission-by-vehicles) |
| crop and weed detection data with bounding boxes | kaggle | [바로가기](https://www.kaggle.com/datasets/ravirajsinh45/crop-and-weed-detection-data-with-bounding-boxes) |
| Crop Recommendation Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) |
| Crop Yield Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset) |
| Daily Climate time series data | kaggle | [바로가기](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data) |
| Daily Temperature of Major Cities | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities) |
| Deep Globe Land Cover Classification Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset) |
| Delhi Air Quality Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kunshbhatia/delhi-air-quality-dataset) |
| Delhi Weather Data | kaggle | [바로가기](https://www.kaggle.com/datasets/mahirkukreja/delhi-weather-data) |
| Did it rain in Seattle? (1948-2017) | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/did-it-rain-in-seattle-19482017) |
| Disaster Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/vstepanenko/disaster-tweets) |
| Earthquake dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/warcoder/earthquake-dataset) |
| Electric Motor Temperature | kaggle | [바로가기](https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature) |
| Emissions by Country | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/global-fossil-co2-emissions-by-country-2002-2022) |
| Energy consumption of the Netherlands | kaggle | [바로가기](https://www.kaggle.com/datasets/lucabasa/dutch-energy) |
| Exoplanet Hunting in Deep Space | kaggle | [바로가기](https://www.kaggle.com/datasets/keplersmachines/kepler-labelled-time-series-data) |
| Fibrosis SMOC2 Raw Counts | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/ecological-footprint) |
| FIRE Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/phylake1337/fire-dataset) |
| Fires from Space: Australia | kaggle | [바로가기](https://www.kaggle.com/datasets/carlosparadis/fires-from-space-australia-and-new-zeland) |
| Forest Cover Type Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/forest-cover-type-dataset) |
| Forest Fires Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/elikplim/forest-fires-data-set) |
| Forest Fires in Brazil | kaggle | [바로가기](https://www.kaggle.com/datasets/gustavomodelli/forest-fires-in-brazil) |
| Gas emissions (CO2-e) by transport sector | kaggle | [바로가기](https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadsdioxidecsv) |
| Geospatial Learn Course Data | kaggle | [바로가기](https://www.kaggle.com/datasets/alexisbcook/geospatial-learn-course-data) |
| Global Air Pollution Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset) |
| Global Data on Sustainable Energy (2000-2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy) |
| Global Earthquake-Tsunami Risk Assessment Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset) |
| Historical Air Quality | kaggle | [바로가기](https://www.kaggle.com/datasets/epa/epa-historical-air-quality) |
| Historical Hourly Weather Data 2012-2017 | kaggle | [바로가기](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data) |
| Hourly Energy Consumption | kaggle | [바로가기](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption) |
| Hourly energy demand generation and weather | kaggle | [바로가기](https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather) |
| Hurricanes and Typhoons, 1851-2014 | kaggle | [바로가기](https://www.kaggle.com/datasets/noaa/hurricane-database) |
| India Agriculture Crop Production | kaggle | [바로가기](https://www.kaggle.com/datasets/pyatakov/india-agriculture-crop-production) |
| India Air Quality Data | kaggle | [바로가기](https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data) |
| Indian Weather Repository (Daily Updating) | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/indian-weather-repository-daily-snapshot) |
| International Energy Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/unitednations/international-energy-statistics) |
| Kepler Exoplanet Search Results | kaggle | [바로가기](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results) |
| Kepler Telescope Exoplanet Discoveries | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/kepler-confirmed-planets) |
| Meteorite Landings | kaggle | [바로가기](https://www.kaggle.com/datasets/nasa/meteorite-landings) |
| Mount Rainier Weather and Climbing Data | kaggle | [바로가기](https://www.kaggle.com/datasets/codersree/mount-rainier-weather-and-climbing-data) |
| NASA - Nearest Earth Objects | kaggle | [바로가기](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects) |
| NASA Bearing Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset) |
| NASA Turbofan Jet Engine Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/behrad3d/nasa-cmaps) |
| NLP for Disaster Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/hardikgarg03/nlp-for-disaster-tweets) |
| NOAA GSOD | kaggle | [바로가기](https://www.kaggle.com/datasets/noaa/gsod) |
| Planes in Satellite Imagery | kaggle | [바로가기](https://www.kaggle.com/datasets/rhammell/planesnet) |
| Predict Droughts using Weather and Soil Data | kaggle | [바로가기](https://www.kaggle.com/datasets/cdminix/us-drought-meteorological-data) |
| Rain in Australia | kaggle | [바로가기](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package) |
| Renewable Energy (1960-2023) | kaggle | [바로가기](https://www.kaggle.com/datasets/imtkaggleteam/renewable-energy-1960-2023) |
| Satellite Image Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/mahmoudreda55/satellite-image-classification) |
| Satellite Images of Water Bodies | kaggle | [바로가기](https://www.kaggle.com/datasets/franciscoescobar/satellite-images-of-water-bodies) |
| Sea Animals Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste) |
| Ships in Satellite Imagery | kaggle | [바로가기](https://www.kaggle.com/datasets/rhammell/ships-in-satellite-imagery) |
| Significant Earthquakes, 1965-2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/usgs/earthquake-database) |
| Smart Home Dataset with weather Information | kaggle | [바로가기](https://www.kaggle.com/datasets/taranvee/smart-home-dataset-with-weather-information) |
| Smoke-Fire-Detection-YOLO | kaggle | [바로가기](https://www.kaggle.com/datasets/sayedgamal99/smoke-fire-detection-yolo) |
| Solar Power Generation Data | kaggle | [바로가기](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data) |
| Solar Radiation Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/dronio/SolarEnergy) |
| Star Type Classification /NASA | kaggle | [바로가기](https://www.kaggle.com/datasets/brsdincer/star-type-classification) |
| Temperature change | kaggle | [바로가기](https://www.kaggle.com/datasets/sevgisarac/temperature-change) |
| Temperature Readings: IOT Devices | kaggle | [바로가기](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices) |
| The Estonia Disaster Passenger List | kaggle | [바로가기](https://www.kaggle.com/datasets/christianlillelund/passenger-list-for-the-estonia-ferry-disaster) |
| Titanic: Machine Learning from Disaster | kaggle | [바로가기](https://www.kaggle.com/datasets/shuofxz/titanic-machine-learning-from-disaster) |
| U.S. Pollution Data | kaggle | [바로가기](https://www.kaggle.com/datasets/sogun3/uspollution) |
| US Natural Disaster Declarations | kaggle | [바로가기](https://www.kaggle.com/datasets/headsortails/us-natural-disaster-declarations) |
| US Weather Events (2016 - 2022) | kaggle | [바로가기](https://www.kaggle.com/datasets/sobhanmoosavi/us-weather-events) |
| Water Quality | kaggle | [바로가기](https://www.kaggle.com/datasets/adityakadiwal/water-potability) |
| Water quality | kaggle | [바로가기](https://www.kaggle.com/datasets/mssmartypants/water-quality) |
| Water Quality and Potability | kaggle | [바로가기](https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability) |
| Weather Conditions in World War Two | kaggle | [바로가기](https://www.kaggle.com/datasets/smid80/weatherww2) |
| Weather Data | kaggle | [바로가기](https://www.kaggle.com/datasets/prasad22/weather-data) |
| Weather Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muthuj7/weather-dataset) |
| Weather Image Recognition | kaggle | [바로가기](https://www.kaggle.com/datasets/jehanbhathena/weather-dataset) |
| Weather in Szeged 2006-2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/budincsevity/szeged-weather) |
| WEATHER PREDICTION | kaggle | [바로가기](https://www.kaggle.com/datasets/ananthr1/weather-prediction) |
| Weather Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/weather-prediction) |
| Weather Type Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/nikhil7280/weather-type-classification) |
| weather.csv | kaggle | [바로가기](https://www.kaggle.com/datasets/zaraavagyan/weathercsv) |
| Wildlife Animals Images | kaggle | [바로가기](https://www.kaggle.com/datasets/anshulmehtakaggl/wildlife-animals-images) |
| Wind Power Forecasting | kaggle | [바로가기](https://www.kaggle.com/datasets/theforcecoder/wind-power-forecasting) |
| Wind Power Generation Data | kaggle | [바로가기](https://www.kaggle.com/datasets/jorgesandoval/wind-power-generation) |
| Wind Turbine Scada Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset) |
| World Air Quality Data 2024 (Updated) | kaggle | [바로가기](https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated) |
| World Energy Consumption | kaggle | [바로가기](https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption) |
| World Weather Repository (Daily Updating) | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository) |
| Access to Energy | ourworldindata | [바로가기](https://ourworldindata.org/energy-access) |
| Air Pollution | ourworldindata | [바로가기](https://ourworldindata.org/air-pollution) |
| Air Pollution Explore historical emissions of air pollutants across the world | ourworldindata | [바로가기](https://ourworldindata.org/explorers/air-pollution) |
| Biodiversity | ourworldindata | [바로가기](https://ourworldindata.org/biodiversity) |
| Climate Change | ourworldindata | [바로가기](https://ourworldindata.org/climate-change) |
| Climate Change Impacts Explore the impacts of global climate change | ourworldindata | [바로가기](https://ourworldindata.org/explorers/climate-change) |
| CO2 and Greenhouse Gas Emissions | ourworldindata | [바로가기](https://ourworldindata.org/co2-and-greenhouse-gas-emissions) |
| CO2 and Greenhouse Gas Emissions Explore data on greenhouse gas emissions | ourworldindata | [바로가기](https://ourworldindata.org/explorers/co2) |
| Crop Yields Explore crop yields across the world | ourworldindata | [바로가기](https://ourworldindata.org/explorers/crop-yields) |
| Energy | ourworldindata | [바로가기](https://ourworldindata.org/energy) |
| Energy Explore data on energy production and sources | ourworldindata | [바로가기](https://ourworldindata.org/explorers/energy) |
| Energy Mix | ourworldindata | [바로가기](https://ourworldindata.org/energy-mix) |
| Environmental Impacts of Food Explore the land use, carbon, and water footprints of food products | ourworldindata | [바로가기](https://ourworldindata.org/explorers/food-footprints) |
| Fish and Overfishing | ourworldindata | [바로가기](https://ourworldindata.org/fish-and-overfishing) |
| Fish Stocks Explore available data on the world's fish stocks | ourworldindata | [바로가기](https://ourworldindata.org/explorers/fish-stocks) |
| Indoor Air Pollution | ourworldindata | [바로가기](https://ourworldindata.org/indoor-air-pollution) |
| Land Use | ourworldindata | [바로가기](https://ourworldindata.org/land-use) |
| Lead Pollution | ourworldindata | [바로가기](https://ourworldindata.org/lead-pollution) |
| Nuclear Energy | ourworldindata | [바로가기](https://ourworldindata.org/nuclear-energy) |
| Outdoor Air Pollution | ourworldindata | [바로가기](https://ourworldindata.org/outdoor-air-pollution) |
| Plastic Pollution | ourworldindata | [바로가기](https://ourworldindata.org/plastic-pollution) |
| Plastic Waste and Pollution Explore global data on plastic waste generation, pollution, and trade | ourworldindata | [바로가기](https://ourworldindata.org/explorers/plastic-pollution) |
| Renewable Energy | ourworldindata | [바로가기](https://ourworldindata.org/renewable-energy) |
| Water Use and Stress | ourworldindata | [바로가기](https://ourworldindata.org/water-use-stress) |
| Water, Sanitation and Hygiene (WASH) Explore global data on water, sanitation and hygiene access | ourworldindata | [바로가기](https://ourworldindata.org/explorers/water-and-sanitation) |
| Energy Efficiency | uci | [바로가기](https://archive.ics.uci.edu/dataset/242/energy+efficiency) |
| Forest Fires | uci | [바로가기](https://archive.ics.uci.edu/dataset/162/forest+fires) |
| MAGIC Gamma Telescope | uci | [바로가기](https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope) |
| A Cross-Country Database of Fiscal Space | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_CCDFS) |
| Climate and Economic Analyses for Resilience in Water (CLEAR Water) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_CLEAR) |
| CO2 and Greenhouse Gas Emissions | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/OWID_CB) |
| Europe and Central Asia (ECA) Water Security Assessment | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_EWSA) |
| Global Biodiversity Data | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_GBIOD) |
| Global Solar Atlas | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_SOLAR_ATLAS) |
| Sustainable Energy For All (SE4ALL) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_SE4ALL) |
| U.S. Energy Information Administration | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/EIA_EIAOD) |

### public (총 474개)

| dataset_name | source | link |
|---|---|---|
| 1000 Genomes | aws_open_data | [바로가기](https://registry.opendata.aws/1000-genomes/) |
| 1000 Genomes Phase 3 Reanalysis with DRAGEN 3.5, 3.7, 4.0, 4.2, and 4.4 | aws_open_data | [바로가기](https://registry.opendata.aws/ilmn-dragen-1kgp/) |
| 1KG-ONT-VIENNA panel | aws_open_data | [바로가기](https://registry.opendata.aws/1kg-ont-vienna/) |
| 3000 Rice Genomes Project | aws_open_data | [바로가기](https://registry.opendata.aws/3kricegenome/) |
| 3DCoMPaT: Composition of Materials on Parts of 3D Things | aws_open_data | [바로가기](https://registry.opendata.aws/3dcompat/) |
| 4D Nucleome (4DN) | aws_open_data | [바로가기](https://registry.opendata.aws/4dnucleome/) |
| A Realistic Cyber Defense Dataset (CSE-CIC-IDS2018) | aws_open_data | [바로가기](https://registry.opendata.aws/cse-cic-ids2018/) |
| A2D2: Audi Autonomous Driving Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/aev-a2d2/) |
| ABEJA CC JA | aws_open_data | [바로가기](https://registry.opendata.aws/abeja-cc-ja/) |
| Adaptive Flow Ligand Libraries | aws_open_data | [바로가기](https://registry.opendata.aws/vf-libraries/) |
| AG-LOAM Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ag-loam/) |
| AI2 Diagram Dataset (AI2D) | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-diagrams/) |
| AI2 Meaningful Citations Data Set | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-meaningful-citations/) |
| AI2 Tablestore (November 2015 Snapshot) | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-tablestore/) |
| AI2 TabMCQ: Multiple Choice Questions aligned with the Aristo Tablestore | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-tablestore-questions/) |
| All The Bacteria | aws_open_data | [바로가기](https://registry.opendata.aws/allthebacteria/) |
| Allen Cell Imaging Collections | aws_open_data | [바로가기](https://registry.opendata.aws/allen-cell-imaging-collections/) |
| Allen Institute for Neural Dynamics - Mouse Neuroanatomy and Physiology Data | aws_open_data | [바로가기](https://registry.opendata.aws/allen-nd-open-data/) |
| Allen Ivy Glioblastoma Atlas | aws_open_data | [바로가기](https://registry.opendata.aws/allen-ivy-glioblastoma-atlas/) |
| Amazon Berkeley Objects Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/amazon-berkeley-objects/) |
| Amazon-PQA | aws_open_data | [바로가기](https://registry.opendata.aws/amazon-pqa/) |
| Answer Reformulation | aws_open_data | [바로가기](https://registry.opendata.aws/answer-reformulation/) |
| APEX-CONNECTS | aws_open_data | [바로가기](https://registry.opendata.aws/apex/) |
| ArcticDEM | aws_open_data | [바로가기](https://registry.opendata.aws/pgc-arcticdem/) |
| Argo marine floats data and metadata from Global Data Assembly Centre (Argo GDAC) | aws_open_data | [바로가기](https://registry.opendata.aws/argo-gdac-marinedata/) |
| Argoverse | aws_open_data | [바로가기](https://registry.opendata.aws/argoverse/) |
| Aristo Tuple KB | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-tuple-kb/) |
| ASL 1000 | aws_open_data | [바로가기](https://registry.opendata.aws/asl_1000/) |
| ASTER L1T Cloud-Optimized GeoTIFFs | aws_open_data | [바로가기](https://registry.opendata.aws/aster-l1t/) |
| Atmospheric Models from Meteo-France | aws_open_data | [바로가기](https://registry.opendata.aws/meteo-france-models/) |
| Australasian Genomes | aws_open_data | [바로가기](https://registry.opendata.aws/australasian-genomics/) |
| AWS i Genomes | aws_open_data | [바로가기](https://registry.opendata.aws/aws-igenomes/) |
| AWS Public Blockchain Data | aws_open_data | [바로가기](https://registry.opendata.aws/aws-public-blockchain/) |
| Baby Open Brains (BOBs) Repository on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/bobsrepository/) |
| Basic Local Alignment Sequences Tool (BLAST) Databases | aws_open_data | [바로가기](https://registry.opendata.aws/ncbi-blast-databases/) |
| Beat Acute Myeloid Leukemia (AML) 1.0 | aws_open_data | [바로가기](https://registry.opendata.aws/beataml/) |
| Bio LiP | aws_open_data | [바로가기](https://registry.opendata.aws/biolip/) |
| BodyM Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/bodym/) |
| Boltz-1 Training Data | aws_open_data | [바로가기](https://registry.opendata.aws/boltz1/) |
| Boreas Autonomous Driving Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/boreas/) |
| BossDB Open Neuroimagery Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/bossdb/) |
| Brai Dyn-BC: Cued lever-pull task dataset | aws_open_data | [바로가기](https://registry.opendata.aws/braidyn-bc_cued-lever-pull/) |
| BUSCO Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/busco-data/) |
| Caenorabditis Diversity Natural Resource | aws_open_data | [바로가기](https://registry.opendata.aws/caendr/) |
| CAFE60 reanalysis | aws_open_data | [바로가기](https://registry.opendata.aws/csiro-cafe60/) |
| CAM6 Data Assimilation Research Testbed (DART) Reanalysis: Cloud-Optimized Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ncar-dart-cam6/) |
| Can Elevation - Canada Digital Elevation Models | aws_open_data | [바로가기](https://registry.opendata.aws/canelevation-dem/) |
| CarbonPDF | aws_open_data | [바로가기](https://registry.opendata.aws/carbonpdf/) |
| Carto Store | aws_open_data | [바로가기](https://registry.opendata.aws/cartostore/) |
| CBERS on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/cbers/) |
| CCRS MODIS albedo over Canada Albedo MODIS du CCT couvrant le Canada | aws_open_data | [바로가기](https://registry.opendata.aws/ccrsmodisalbedo/) |
| Cell Painting Gallery | aws_open_data | [바로가기](https://registry.opendata.aws/cellpainting-gallery/) |
| CESM-HR | aws_open_data | [바로가기](https://registry.opendata.aws/cesm-hr/) |
| Chalmers Cloud Ice Climatology | aws_open_data | [바로가기](https://registry.opendata.aws/ccic/) |
| CHAMMI-75 | aws_open_data | [바로가기](https://registry.opendata.aws/chammi/) |
| CHIMERA | aws_open_data | [바로가기](https://registry.opendata.aws/chimera/) |
| Citrus Farm Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/citrus-farm/) |
| Clay Model v0 Embeddings | aws_open_data | [바로가기](https://registry.opendata.aws/clay-model-v0-embeddings/) |
| Clay v1.5 NAIP-2 | aws_open_data | [바로가기](https://registry.opendata.aws/clay-v1-5-naip-2/) |
| Cloud Indexes for Bowtie, Kraken, HISAT, and Centrifuge | aws_open_data | [바로가기](https://registry.opendata.aws/jhu-indexes/) |
| CMAS Data Warehouse | aws_open_data | [바로가기](https://registry.opendata.aws/cmas-data-warehouse/) |
| CMIP6 GCMs downscaled using WRF | aws_open_data | [바로가기](https://registry.opendata.aws/wrf-cmip6/) |
| COBRA | aws_open_data | [바로가기](https://registry.opendata.aws/cobra/) |
| COCO - Common Objects in Context - fast.ai datasets | aws_open_data | [바로가기](https://registry.opendata.aws/fast-ai-coco/) |
| Common Crawl | aws_open_data | [바로가기](https://registry.opendata.aws/commoncrawl/) |
| Common Screens | aws_open_data | [바로가기](https://registry.opendata.aws/comonscreens/) |
| CoMMpass from the Multiple Myeloma Research Foundation | aws_open_data | [바로가기](https://registry.opendata.aws/mmrf-commpass/) |
| Consented Activities of People | aws_open_data | [바로가기](https://registry.opendata.aws/visym-cap/) |
| Copernicus Digital Elevation Model (DEM) | aws_open_data | [바로가기](https://registry.opendata.aws/copernicus-dem/) |
| Corn Kernel Counting Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/intelinair_corn_kernel_counting/) |
| Coupled Model Intercomparison Project 6 | aws_open_data | [바로가기](https://registry.opendata.aws/cmip6/) |
| CoversBR | aws_open_data | [바로가기](https://registry.opendata.aws/covers-br/) |
| CryoET Data Portal | aws_open_data | [바로가기](https://registry.opendata.aws/cryoet-data-portal/) |
| CZ Grand Challenges - Imaging BSD licensed data and models | aws_open_data | [바로가기](https://registry.opendata.aws/czi-imaging-bsd/) |
| CZ Grand Challenges - Imaging MIT Licensed data and models | aws_open_data | [바로가기](https://registry.opendata.aws/czi-imagining-mit/) |
| CZ Grand Challenges - Model Benchmarking | aws_open_data | [바로가기](https://registry.opendata.aws/czi-benchmarking/) |
| CZ Grand Challenges - Transcriptomic MIT Licensed data and models | aws_open_data | [바로가기](https://registry.opendata.aws/czi-transcriptomics-mit/) |
| Danish Meteorological Institute (DMI) Open Data Forecasts | aws_open_data | [바로가기](https://registry.opendata.aws/dmi-opendata/) |
| Danish Meteorological Institute (DMI) Reanalysis dataset v0.5 | aws_open_data | [바로가기](https://registry.opendata.aws/dmi-danra-05/) |
| DARPA Invisible Headlights Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/darpa-invisible-headlights/) |
| Data to Science Catalog | aws_open_data | [바로가기](https://registry.opendata.aws/data-to-science/) |
| Daylight Map Distribution of Open Street Map | aws_open_data | [바로가기](https://registry.opendata.aws/daylight-osm/) |
| DCR Office of Resilience Planning - Public File Repository | aws_open_data | [바로가기](https://registry.opendata.aws/vadcr-crmp-aws/) |
| DE Africa Waterbodies Monitoring Service | aws_open_data | [바로가기](https://registry.opendata.aws/deafrica-waterbodies/) |
| Demand-Side Grid (dsgrid) Toolkit | aws_open_data | [바로가기](https://registry.opendata.aws/nrel-pds-dsgrid/) |
| Dendritic Consortium Multimodal Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/dendritic-consortium/) |
| Digital Corpora | aws_open_data | [바로가기](https://registry.opendata.aws/digitalcorpora/) |
| Discrete Reasoning Over the content of Paragraphs (DROP) | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-drop/) |
| Distributed Archives for Neurophysiology Data Integration (DANDI) | aws_open_data | [바로가기](https://registry.opendata.aws/dandiarchive/) |
| E11bio PRISM | aws_open_data | [바로가기](https://registry.opendata.aws/e11bio-prism/) |
| EarthDEM | aws_open_data | [바로가기](https://registry.opendata.aws/pgc-earthdem/) |
| ECMWF IFS ENS - dynamical.org Icechunk Zarr | aws_open_data | [바로가기](https://registry.opendata.aws/dynamical-ecmwf-ifs-ens/) |
| ECMWF real-time forecasts | aws_open_data | [바로가기](https://registry.opendata.aws/ecmwf-forecasts/) |
| EEGDash on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/eegdash/) |
| EMBER Open Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/ember/) |
| EMory Br East Imaging Dataset (EMBED) | aws_open_data | [바로가기](https://registry.opendata.aws/emory-breast-imaging-dataset-embed/) |
| Emory Knee Radiograph (MRKR) dataset | aws_open_data | [바로가기](https://registry.opendata.aws/mrkr/) |
| End of Term Web Archive Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/eot-web-archive/) |
| ENHANCE.PET 1.6k - Whole-/Total-Body [18F]FDG-PET/CT with CT-Derived Segmentations | aws_open_data | [바로가기](https://registry.opendata.aws/enhance-pet-1-6k/) |
| EPA Dynamically Downscaled Ensemble (EDDE) Version 1 | aws_open_data | [바로가기](https://registry.opendata.aws/epa-edde-v1/) |
| EPA Dynamically Downscaled Ensemble (EDDE) Version 2 | aws_open_data | [바로가기](https://registry.opendata.aws/epa-edde-v2/) |
| EPA Risk-Screening Environmental Indicators | aws_open_data | [바로가기](https://registry.opendata.aws/epa-rsei-pds/) |
| Epigenomes of the Human Pangenome Reference Consortium (HPRC) Release 2 | aws_open_data | [바로가기](https://registry.opendata.aws/hprc-epigenome/) |
| Epilepsy.Science | aws_open_data | [바로가기](https://registry.opendata.aws/epilepsy-science/) |
| Epoch of Reionization Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/epoch-of-reionization/) |
| ERA5-for-WRF Open Data on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/era5-for-wrf/) |
| ESA World Cover | aws_open_data | [바로가기](https://registry.opendata.aws/esa-worldcover-vito/) |
| Essential-Web v1.0: 24T tokens of organized web data | aws_open_data | [바로가기](https://registry.opendata.aws/eai-essential-web-v1/) |
| Euclid Quick Release 1 (Q1) | aws_open_data | [바로가기](https://registry.opendata.aws/euclid-q1/) |
| EURO-CORDEX - European component of the Coordinated Regional Downscaling Experiment | aws_open_data | [바로가기](https://registry.opendata.aws/euro-cordex/) |
| Exceptional Responders Initiative | aws_open_data | [바로가기](https://registry.opendata.aws/exceptional-responders/) |
| Fashion Local Triplets | aws_open_data | [바로가기](https://registry.opendata.aws/fashionlocaltriplets/) |
| FLAb: Fitness Landscapes for Antibodies | aws_open_data | [바로가기](https://registry.opendata.aws/flab/) |
| Ford Multi-AV Seasonal Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ford-multi-av-seasonal/) |
| Gabriella Miller Kids First Pediatric Research Program (Kids First) | aws_open_data | [바로가기](https://registry.opendata.aws/kids-first/) |
| Gaia DR3 | aws_open_data | [바로가기](https://registry.opendata.aws/mast-gaia-dr3/) |
| GATK Structural Variation (SV) Data | aws_open_data | [바로가기](https://registry.opendata.aws/gatk-sv-data/) |
| GATK Test Data | aws_open_data | [바로가기](https://registry.opendata.aws/gatk-test-data/) |
| Geo Net Aotearoa New Zealand Data | aws_open_data | [바로가기](https://registry.opendata.aws/geonet/) |
| GEOGLOWS Hydrological Model Version 2 | aws_open_data | [바로가기](https://registry.opendata.aws/geoglows-v2/) |
| GeoJSON Files for Geo-TIDE | aws_open_data | [바로가기](https://registry.opendata.aws/geo_tide_geojsons/) |
| GEOS-Chem Input Data | aws_open_data | [바로가기](https://registry.opendata.aws/geoschem-input-data/) |
| GEOS-Chem Nested Input Data | aws_open_data | [바로가기](https://registry.opendata.aws/geoschem-nested-input-data/) |
| Global 30m Height Above Nearest Drainage (HAND) | aws_open_data | [바로가기](https://registry.opendata.aws/glo-30-hand/) |
| Global Cache of Japan | aws_open_data | [바로가기](https://registry.opendata.aws/wis2-global-cache-jma/) |
| Global Carbon Budget Data | aws_open_data | [바로가기](https://registry.opendata.aws/gcbo-dataset/) |
| Google Books Ngrams | aws_open_data | [바로가기](https://registry.opendata.aws/google-ngrams/) |
| GRAF Reforecast | aws_open_data | [바로가기](https://registry.opendata.aws/graf-reforecast/) |
| Grid Algorithms and Data Analytics Library (GADAL) | aws_open_data | [바로가기](https://registry.opendata.aws/gadal/) |
| GX database for NCBI Foreign Contamination Screen (FCS) Tool Suite | aws_open_data | [바로가기](https://registry.opendata.aws/ncbi-fcs-gx/) |
| Harvard Electroencephalography Database | aws_open_data | [바로가기](https://registry.opendata.aws/bdsp-harvard-eeg/) |
| Hecatomb Databases | aws_open_data | [바로가기](https://registry.opendata.aws/hecatomb/) |
| Helpful Sentences from Reviews | aws_open_data | [바로가기](https://registry.opendata.aws/helpful-sentences-from-reviews/) |
| High Resolution Canopy Height Maps by WRI and Meta | aws_open_data | [바로가기](https://registry.opendata.aws/dataforgood-fb-forests/) |
| High resolution, annual cropland and landcover maps for selected African countries | aws_open_data | [바로가기](https://registry.opendata.aws/mapping-africa/) |
| High-Order Accurate Direct Numerical Simulation of Flow over a MTU-T161 Low Pressure Turbine Blade | aws_open_data | [바로가기](https://registry.opendata.aws/pyfr-mtu-t161-dns-data/) |
| Human Cell Atlas | aws_open_data | [바로가기](https://registry.opendata.aws/humancellatlas/) |
| Human Pan Genomics Project | aws_open_data | [바로가기](https://registry.opendata.aws/hpgp-data/) |
| Humor patterns used for querying Alexa traffic | aws_open_data | [바로가기](https://registry.opendata.aws/humor-patterns/) |
| Hybrid statistical-dynamic downscaling based on multi-model ensembles in Southeast Asia | aws_open_data | [바로가기](https://registry.opendata.aws/cmip6-era5-hybrid-southeast-asia/) |
| i Naturalist Licensed Observation Images | aws_open_data | [바로가기](https://registry.opendata.aws/inaturalist-open-data/) |
| I-CARE:International Cardiac Arrest REsearch consortium Electroencephalography Database | aws_open_data | [바로가기](https://registry.opendata.aws/bdsp-icare/) |
| IBL Neuropixels Brainwide Map on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/ibl-autism/) |
| IBL Neuropixels Reproducible Ephys Data on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/ibl-reproducible-ephys/) |
| ICGC on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/icgc/) |
| IGP Coal Plant | aws_open_data | [바로가기](https://registry.opendata.aws/asset-data-igp-coal-plant/) |
| Indexes for Kaiju | aws_open_data | [바로가기](https://registry.opendata.aws/kaiju-indexes/) |
| Indian High Court Judgments | aws_open_data | [바로가기](https://registry.opendata.aws/indian-high-court-judgments/) |
| Indian Supreme Court Judgments | aws_open_data | [바로가기](https://registry.opendata.aws/indian-supreme-court-judgments/) |
| Indiana Statewide Elevation Catalog | aws_open_data | [바로가기](https://registry.opendata.aws/in-elevation/) |
| International Neuroimaging Data-Sharing Initiative (INDI) | aws_open_data | [바로가기](https://registry.opendata.aws/fcp-indi/) |
| International Skin Imaging Collaboration (ISIC) Archive | aws_open_data | [바로가기](https://registry.opendata.aws/isic-archive/) |
| iSDAsoil | aws_open_data | [바로가기](https://registry.opendata.aws/isdasoil/) |
| ISERV | aws_open_data | [바로가기](https://registry.opendata.aws/iserv/) |
| IWMI DIWASA Blue ET for Africa | aws_open_data | [바로가기](https://registry.opendata.aws/blue_et/) |
| IWMI DIWASA Green ET for Africa | aws_open_data | [바로가기](https://registry.opendata.aws/green_et/) |
| IWMI DIWASA Rainfed and Irrigated Cropland Map for Africa | aws_open_data | [바로가기](https://registry.opendata.aws/cropland_partitioining/) |
| Japan Prefectures, 3D Point Cloud Data | aws_open_data | [바로가기](https://registry.opendata.aws/japan_pointcloud/) |
| Japanese Tokenizer Dictionaries | aws_open_data | [바로가기](https://registry.opendata.aws/cotonoha-dic/) |
| K2 Mission Data | aws_open_data | [바로가기](https://registry.opendata.aws/mast-k2/) |
| Kanagawa, 3D Point Cloud Data | aws_open_data | [바로가기](https://registry.opendata.aws/kanagawa_pointcloud/) |
| Kepler Mission Data | aws_open_data | [바로가기](https://registry.opendata.aws/kepler/) |
| Knowledge Portal Network Bottom-line Genetic Associations | aws_open_data | [바로가기](https://registry.opendata.aws/dig-open-analysis-data/) |
| Kraken2 NCBI Ref Seq Complete V205 database on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/kraken2-ncbi-refseq-complete-v205/) |
| Ky From Above on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/kyfromabove/) |
| Legal Entity Identifier (LEI) and Legal Entity Reference Data (LE-RD) | aws_open_data | [바로가기](https://registry.opendata.aws/lei/) |
| LOFAR ELAIS-N1 cycle 2 observations on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/lofar-elais-n1/) |
| Longitudinal Nutrient Deficiency | aws_open_data | [바로가기](https://registry.opendata.aws/intelinair_longitudinal_nutrient_deficiency/) |
| Louisiana Watershed Initiative (LWI) Model Data | aws_open_data | [바로가기](https://registry.opendata.aws/lwi-model-data/) |
| Low Context Name Entity Recognition (NER) Datasets with Gazetteer | aws_open_data | [바로가기](https://registry.opendata.aws/lowcontext-ner-gaz/) |
| MAN Truck Scenes | aws_open_data | [바로가기](https://registry.opendata.aws/man-truckscenes/) |
| Marginal Build Emissions Rates (MBERs) for Electricity | aws_open_data | [바로가기](https://registry.opendata.aws/mbers-open-data/) |
| Materials Project Data | aws_open_data | [바로가기](https://registry.opendata.aws/materials-project/) |
| Maxar Open Data Program | aws_open_data | [바로가기](https://registry.opendata.aws/maxar-open-data/) |
| Mega Scenes | aws_open_data | [바로가기](https://registry.opendata.aws/megascenes/) |
| Met Office Global and Regional Ensemble Prediction System - UK (MOGREPS-UK) on a 30-day rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-uk-ensemble/) |
| Met Office Global Deterministic 10km on a 2-year rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-global-deterministic/) |
| Met Office Global Ensemble Prediction System (MOGREPS-G) on a 30-day rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-global-ensemble/) |
| Met Office Global Wave model on a 2-year rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-global-wave/) |
| Met Office NWS Wave model on a 2-year rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-nws-wave/) |
| Met Office UK Deterministic (UKV)2km on a 2-year rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-uk-deterministic/) |
| Met Office UK Land Surface Observations | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-uk-land-observations/) |
| Meta-Organized Stimuli And fMRI Imaging data for Computational modeling (MOSAIC) | aws_open_data | [바로가기](https://registry.opendata.aws/mosaic/) |
| Metagenomic reference libraries for Slacken | aws_open_data | [바로가기](https://registry.opendata.aws/slacken/) |
| mirrulations | aws_open_data | [바로가기](https://registry.opendata.aws/mirrulations/) |
| MODIS MYD13A1, MOD13A1, MYD11A1, MOD11A1, MCD43A4 | aws_open_data | [바로가기](https://registry.opendata.aws/modis-astraea/) |
| Molecular Profiling to Predict Response to Treatment (phs001965) | aws_open_data | [바로가기](https://registry.opendata.aws/mp2prt/) |
| MONKEY | aws_open_data | [바로가기](https://registry.opendata.aws/monkey/) |
| Multi CoNER Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/multiconer/) |
| Multi Token Completion | aws_open_data | [바로가기](https://registry.opendata.aws/multi-token-completion/) |
| Multilingual Name Entity Recognition (NER) Datasets with Gazetteer | aws_open_data | [바로가기](https://registry.opendata.aws/code-mixed-ner/) |
| Multimedia Commons | aws_open_data | [바로가기](https://registry.opendata.aws/multimedia-commons/) |
| MWIS VR Instances | aws_open_data | [바로가기](https://registry.opendata.aws/mwis-vr-instances/) |
| My School Today | aws_open_data | [바로가기](https://registry.opendata.aws/sdgstoday-mst/) |
| NA-CORDEX - North American component of the Coordinated Regional Downscaling Experiment | aws_open_data | [바로가기](https://registry.opendata.aws/ncar-na-cordex/) |
| NAIP on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/naip/) |
| Napier One Mixed File Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/napierone/) |
| National Archives Catalog | aws_open_data | [바로가기](https://registry.opendata.aws/nara-national-archives-catalog/) |
| National Herbarium of Israel | aws_open_data | [바로가기](https://registry.opendata.aws/huj-herbarium/) |
| National Herbarium of NSW | aws_open_data | [바로가기](https://registry.opendata.aws/nsw-herbarium/) |
| National Mooring Network - CTD profiles | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_mooring_ctd_delayed_qc/) |
| Natural Scenes Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/nsd/) |
| New York City Taxi and Limousine Commission (TLC) Trip Record Data | aws_open_data | [바로가기](https://registry.opendata.aws/nyc-tlc-trip-records-pds/) |
| New Zealand Coastal Elevation | aws_open_data | [바로가기](https://registry.opendata.aws/nz-coastal/) |
| New Zealand Elevation | aws_open_data | [바로가기](https://registry.opendata.aws/nz-elevation/) |
| NHGRI AnVIL Project | aws_open_data | [바로가기](https://registry.opendata.aws/anvilproject/) |
| NIFS Large Helical Device (LHD) Experiment | aws_open_data | [바로가기](https://registry.opendata.aws/nifs-lhd/) |
| NIH Roadmap Epigenomics | aws_open_data | [바로가기](https://registry.opendata.aws/roadmapepigenomics/) |
| Normalized Difference Urban Index (NDUI) | aws_open_data | [바로가기](https://registry.opendata.aws/ndui/) |
| NSF NCAR Curated ECMWF Reanalysis 5 (ERA5) | aws_open_data | [바로가기](https://registry.opendata.aws/nsf-ncar-era5/) |
| nu Plan | aws_open_data | [바로가기](https://registry.opendata.aws/motional-nuplan/) |
| nu Scenes | aws_open_data | [바로가기](https://registry.opendata.aws/motional-nuscenes/) |
| NYU Langone and FAIR FastMRI Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/nyu-fastmri/) |
| OME-Zarr Open Sci Vis Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/ome-zarr-open-scivis/) |
| ONS Open Data Portal | aws_open_data | [바로가기](https://registry.opendata.aws/ons-opendata-portal/) |
| ONT Methylation Benchmarking Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/ont_basemod_data/) |
| Open Aerial Map on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/openaerialmap/) |
| Open Alex dataset | aws_open_data | [바로가기](https://registry.opendata.aws/openalex/) |
| Open CEDA by Watershed | aws_open_data | [바로가기](https://registry.opendata.aws/open-ceda/) |
| Open Cell on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/czb-opencell/) |
| Open City Model (OCM) | aws_open_data | [바로가기](https://registry.opendata.aws/opencitymodel/) |
| Open Fold3 Training Data | aws_open_data | [바로가기](https://registry.opendata.aws/openfold3/) |
| Open Food Facts Images | aws_open_data | [바로가기](https://registry.opendata.aws/openfoodfacts-images/) |
| Open Observatory of Network Interference (OONI) | aws_open_data | [바로가기](https://registry.opendata.aws/ooni/) |
| Open Robo Care Multi-Modal Expert Demonstration Dataset for Robot-Assisted Caregiving | aws_open_data | [바로가기](https://registry.opendata.aws/open-robo-care/) |
| Open Street Map on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/osm/) |
| Open Surfaces | aws_open_data | [바로가기](https://registry.opendata.aws/opensurfaces/) |
| Open Targets | aws_open_data | [바로가기](https://registry.opendata.aws/opentargets/) |
| Open Universe 2024 Simulated Roman and Rubin Images | aws_open_data | [바로가기](https://registry.opendata.aws/openuniverse2024/) |
| Open VLF: Scientific Open Data Initiative for CRAAM's SAVNET and AWESOME VLF Data | aws_open_data | [바로가기](https://registry.opendata.aws/craam-open-vlf/) |
| Open Wings Open Data | aws_open_data | [바로가기](https://registry.opendata.aws/openwings/) |
| OpenAQ | aws_open_data | [바로가기](https://registry.opendata.aws/openaq/) |
| OpenCRAVAT | aws_open_data | [바로가기](https://registry.opendata.aws/open-cravat/) |
| OpenEEW | aws_open_data | [바로가기](https://registry.opendata.aws/grillo-openeew/) |
| Opioid Industry Documents Archive (OIDA) Data on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/oida/) |
| Orcasound - bioacoustic data for marine conservation | aws_open_data | [바로가기](https://registry.opendata.aws/orcasound/) |
| OSAP 2022 Modeling Platform | aws_open_data | [바로가기](https://registry.opendata.aws/epa-2022-modeling-platform/) |
| Overture Maps Foundation Open Map Data | aws_open_data | [바로가기](https://registry.opendata.aws/overture/) |
| Pacific Coastlines Change | aws_open_data | [바로가기](https://registry.opendata.aws/dep-coastlines/) |
| PALSAR-2 ScanSAR CARD4L (L2.2) | aws_open_data | [바로가기](https://registry.opendata.aws/jaxa-alos-palsar2-scansar/) |
| PALSAR-2 ScanSAR Flooding in Rwanda (L2.1) | aws_open_data | [바로가기](https://registry.opendata.aws/palsar-2-scansar-flooding-in-rwanda/) |
| PALSAR-2 ScanSAR Tropical Cycolne Mocha (L2.1) | aws_open_data | [바로가기](https://registry.opendata.aws/palsar-2-scansar-flooding-in-bangladesh/) |
| PASS: Perturb-and-Select Summarizer for Product Reviews | aws_open_data | [바로가기](https://registry.opendata.aws/pass-summaries-fewsum/) |
| PD12M | aws_open_data | [바로가기](https://registry.opendata.aws/pd12m/) |
| Person Path22 | aws_open_data | [바로가기](https://registry.opendata.aws/person-path-22/) |
| Physionet | aws_open_data | [바로가기](https://registry.opendata.aws/physionet/) |
| Planette ERA5 Archive | aws_open_data | [바로가기](https://registry.opendata.aws/planette_era5_reanalysis/) |
| Platinum Pedigree | aws_open_data | [바로가기](https://registry.opendata.aws/platinum-pedigree/) |
| Pohang Canal Dataset: A Multimodal Maritime Dataset for Autonomous Navigation in Restricted Waters | aws_open_data | [바로가기](https://registry.opendata.aws/pohang-canal-dataset/) |
| Poro Tomo | aws_open_data | [바로가기](https://registry.opendata.aws/nrel-pds-porotomo/) |
| Poseidon 3D Seismic, Australia | aws_open_data | [바로가기](https://registry.opendata.aws/tgs-opendata-poseidon/) |
| Pre- and post-purchase product questions | aws_open_data | [바로가기](https://registry.opendata.aws/pre-post-purchase-questions/) |
| Product Comparison Dataset for Online Shopping | aws_open_data | [바로가기](https://registry.opendata.aws/prod-comp-shopping/) |
| PROJ datum grids | aws_open_data | [바로가기](https://registry.opendata.aws/proj-datum-grids/) |
| Provision of Web-Scale Parallel Corpora for Official European Languages (Para Crawl) | aws_open_data | [바로가기](https://registry.opendata.aws/paracrawl/) |
| Public Utility Data Liberation Project | aws_open_data | [바로가기](https://registry.opendata.aws/catalyst-cooperative-pudl/) |
| Py Envs and Call Args | aws_open_data | [바로가기](https://registry.opendata.aws/pyenvs-and-callargs/) |
| QIIME 2 Tutorial Data | aws_open_data | [바로가기](https://registry.opendata.aws/qiime2/) |
| Quoref | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-quoref/) |
| RACECAR Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/racecar-dataset/) |
| RADARSAT-1 | aws_open_data | [바로가기](https://registry.opendata.aws/radarsat-1/) |
| Radiant MLHub | aws_open_data | [바로가기](https://registry.opendata.aws/radiant-mlhub/) |
| RADIANT Public Data | aws_open_data | [바로가기](https://registry.opendata.aws/radiant/) |
| Rare Planes | aws_open_data | [바로가기](https://registry.opendata.aws/rareplanes/) |
| RCM CEOS Analysis Ready Data Donnees pretes a l'analyse du CEOS pour le MCR | aws_open_data | [바로가기](https://registry.opendata.aws/rcm-ceos-ard/) |
| real-changesets | aws_open_data | [바로가기](https://registry.opendata.aws/real-changesets/) |
| Reasoning Over Paragraph Effects in Situations (ROPES) | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-ropes/) |
| recount3 | aws_open_data | [바로가기](https://registry.opendata.aws/recount/) |
| Reference data for Hi Fi human WGS | aws_open_data | [바로가기](https://registry.opendata.aws/pacbio-human-wgs-reference/) |
| Reference Elevation Model of Antarctica (REMA) | aws_open_data | [바로가기](https://registry.opendata.aws/pgc-rema/) |
| Reference Indexes for krepp | aws_open_data | [바로가기](https://registry.opendata.aws/kreppref/) |
| Registry of Open Data on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/registry-open-data/) |
| RSNA Abdominal Traumatic Injury CT (RATIC) | aws_open_data | [바로가기](https://registry.opendata.aws/rsna-ratic/) |
| run_dbcan CAZyme and CGC annotation database on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/run_dbcan/) |
| Safecast | aws_open_data | [바로가기](https://registry.opendata.aws/safecast/) |
| Sanborn Maps Data Package | aws_open_data | [바로가기](https://registry.opendata.aws/loc-sanborn-maps/) |
| SatPM2.5 | aws_open_data | [바로가기](https://registry.opendata.aws/surface-pm2-5-v6gl/) |
| See Far V0 | aws_open_data | [바로가기](https://registry.opendata.aws/seefar/) |
| Serratus: Ultra-deep Search for Novel Viruses - Versioned Data Release | aws_open_data | [바로가기](https://registry.opendata.aws/serratus-lovelywater/) |
| Ships of Opportunity - Expendable bathythermographs - Delayed mode | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_vessel_xbt_delayed_qc/) |
| Ships of Opportunity - Expendable bathythermographs - Real time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_vessel_xbt_realtime_nonqc/) |
| Ships of Opportunity - Fisheries vessels - Real time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_vessel_fishsoop_realtime_qc/) |
| Ships of Opportunity - Tropical research vessels - Real time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_vessel_trv_realtime_qc/) |
| Shopping Humor Generation | aws_open_data | [바로가기](https://registry.opendata.aws/shopping-humor-generation/) |
| Si Pe CaM (Sitios Permanentes de la Calibracion y Monitoreo de la Biodiversidad) | aws_open_data | [바로가기](https://registry.opendata.aws/sipecam/) |
| Single-Cell Atlas of Human Blood During Healthy Aging | aws_open_data | [바로가기](https://registry.opendata.aws/singlecellhumanbloodatlas/) |
| Smithsonian Open Access | aws_open_data | [바로가기](https://registry.opendata.aws/smithsonian-open-access/) |
| Sofar Spotter Archive | aws_open_data | [바로가기](https://registry.opendata.aws/sofar-spotter-archive/) |
| Software Heritage Graph Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/software-heritage/) |
| Somatic Mosaicism across Human Tissues (SMaHT) | aws_open_data | [바로가기](https://registry.opendata.aws/smaht/) |
| Sounds of Central African landscapes | aws_open_data | [바로가기](https://registry.opendata.aws/elp-nouabale-landscape/) |
| SPARTAN Data | aws_open_data | [바로가기](https://registry.opendata.aws/spartan-cloud/) |
| Speedtest by Ookla Global Fixed and Mobile Network Performance Maps | aws_open_data | [바로가기](https://registry.opendata.aws/speedtest-global-performance/) |
| Spitzer Enhanced Imaging Products (SEIP) Super Mosaics | aws_open_data | [바로가기](https://registry.opendata.aws/spitzer-seip/) |
| State of Colorado Elevation Data | aws_open_data | [바로가기](https://registry.opendata.aws/colorado-elevation-data/) |
| stdpopsim species resources | aws_open_data | [바로가기](https://registry.opendata.aws/stdpopsim_kern/) |
| Steinegger Lab Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/steineggerlab/) |
| STOIC2021 Training | aws_open_data | [바로가기](https://registry.opendata.aws/stoic2021-training/) |
| Sub-Meter Canopy Tree Height of California in 2020 by CTrees.org | aws_open_data | [바로가기](https://registry.opendata.aws/ctrees-california-vhr-tree-height/) |
| SUCHO Ukrainian Cultural Heritage Web Archives | aws_open_data | [바로가기](https://registry.opendata.aws/sucho/) |
| Sup3rCC | aws_open_data | [바로가기](https://registry.opendata.aws/nrel-pds-sup3rcc/) |
| Surya Bench | aws_open_data | [바로가기](https://registry.opendata.aws/surya-bench/) |
| Swiss Public Transport Stops | aws_open_data | [바로가기](https://registry.opendata.aws/schweizer-haltestellen-oev/) |
| Synthea Coherent Data Set | aws_open_data | [바로가기](https://registry.opendata.aws/synthea-coherent-data/) |
| Tabula Muris | aws_open_data | [바로가기](https://registry.opendata.aws/tabula-muris/) |
| Tabula Muris Senis | aws_open_data | [바로가기](https://registry.opendata.aws/tabula-muris-senis/) |
| Tabula Sapiens | aws_open_data | [바로가기](https://registry.opendata.aws/tabula-sapiens/) |
| Terra Fusion Data Sampler | aws_open_data | [바로가기](https://registry.opendata.aws/terrafusion/) |
| Terrain Tiles | aws_open_data | [바로가기](https://registry.opendata.aws/terrain-tiles/) |
| TESS-GAIA Light Curve (TGLC) | aws_open_data | [바로가기](https://registry.opendata.aws/mast-tglc/) |
| TESS-SPOC | aws_open_data | [바로가기](https://registry.opendata.aws/mast-tess-spoc/) |
| The Human Connectome Project | aws_open_data | [바로가기](https://registry.opendata.aws/hcp-openaccess/) |
| The Impact of Variation on Function Consortium (IGVF) | aws_open_data | [바로가기](https://registry.opendata.aws/igvf-consortium/) |
| The MIT Supercloud Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/dcc/) |
| The Singapore Nanopore Expression Data Set | aws_open_data | [바로가기](https://registry.opendata.aws/sgnex/) |
| Therapeutically Applicable Research to Generate Effective Treatments (TARGET) | aws_open_data | [바로가기](https://registry.opendata.aws/target/) |
| TIGER Training | aws_open_data | [바로가기](https://registry.opendata.aws/tiger/) |
| TSBench | aws_open_data | [바로가기](https://registry.opendata.aws/tsbench/) |
| U.S. Environmental Protection Agency (EPA) Center for Computational Toxicology and Exposure High Throughput Transcriptomics Data | aws_open_data | [바로가기](https://registry.opendata.aws/epa-ccte-httr/) |
| UCSF Renal Mass CT Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ucsf-rmac/) |
| UK Biobank Linkage Disequilibrium Matrices | aws_open_data | [바로가기](https://registry.opendata.aws/ukbb-ld/) |
| UK Biobank Pan-Ancestry Summary Statistics | aws_open_data | [바로가기](https://registry.opendata.aws/broad-pan-ukb/) |
| UK Biobank Pharma Proteomics Project (UKB-PPP) | aws_open_data | [바로가기](https://registry.opendata.aws/ukbppp/) |
| UMASSD-FVCOM-GOM3-Hindcast | aws_open_data | [바로가기](https://registry.opendata.aws/fvcom_gom3/) |
| Uni Prot | aws_open_data | [바로가기](https://registry.opendata.aws/uniprot/) |
| USearch Molecules | aws_open_data | [바로가기](https://registry.opendata.aws/usearch-molecules/) |
| VENUS L2A Cloud-Optimized GeoTIFFs | aws_open_data | [바로가기](https://registry.opendata.aws/venus-l2a-cogs/) |
| Virtual Shizuoka, 3D Point Cloud Data | aws_open_data | [바로가기](https://registry.opendata.aws/virtual_shizuoka/) |
| VitalDB | aws_open_data | [바로가기](https://registry.opendata.aws/vitaldb/) |
| Voi SeR | aws_open_data | [바로가기](https://registry.opendata.aws/amazon-conversational-product-search/) |
| Voices Obscured in Complex Environmental Settings (VOiCES) | aws_open_data | [바로가기](https://registry.opendata.aws/lab41-sri-voices/) |
| Wave buoys observations - Real time | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_wave_buoy_realtime_nonqc/) |
| Whiffle WINS50 Open Data on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/whiffle-wins50/) |
| WIS2 Global Cache on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/wis2-global-cache/) |
| Wizard of Tasks | aws_open_data | [바로가기](https://registry.opendata.aws/wizard-of-tasks/) |
| Xiph.Org Test Media | aws_open_data | [바로가기](https://registry.opendata.aws/xiph-media/) |
| You Tube 8 Million - Data Lakehouse Ready | aws_open_data | [바로가기](https://registry.opendata.aws/yt8m/) |
| ZEST: ZEro Shot learning from Task descriptions | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-zest/) |
| ZINC Database | aws_open_data | [바로가기](https://registry.opendata.aws/zinc15/) |
| Zwicky Transient Facility (ZTF) | aws_open_data | [바로가기](https://registry.opendata.aws/ztf/) |
| Abortion Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadsabortioncsv) |
| Airbnb Open Data | kaggle | [바로가기](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata) |
| Billionaires Statistics Dataset (2023) | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/billionaires-statistics-dataset) |
| Boston Airbnb Open Data | kaggle | [바로가기](https://www.kaggle.com/datasets/airbnb/boston) |
| California STD Statistics (2001-2021) | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/stds-in-california) |
| Country Statistics - UNData | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/undata-country-profiles) |
| FIFA23 OFFICIAL DATASET | kaggle | [바로가기](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database) |
| Global Commodity Trade Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/unitednations/global-commodity-trade-statistics) |
| Global Food and Agriculture Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/unitednations/global-food-agriculture-statistics) |
| Global You Tube Statistics 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023) |
| Insightful and Vast USA Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/goldenoakresearch/us-acs-mortgage-equity-loans-rent-statistics) |
| Japan Trade Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/zanjibar/japan-trade-statistics) |
| Kickstarter Project Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/socathie/kickstarter-project-statistics) |
| New York City Airbnb Open Data | kaggle | [바로가기](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) |
| New York City Bus Data | kaggle | [바로가기](https://www.kaggle.com/datasets/stoney71/new-york-city-transport-statistics) |
| NFL Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/kendallgillies/nflstatistics) |
| NYC Open Data | kaggle | [바로가기](https://www.kaggle.com/datasets/nycopendata/new-york) |
| Predict FIFA 2018 Man of the Match | kaggle | [바로가기](https://www.kaggle.com/datasets/mathan/fifa-2018-match-statistics) |
| PUBG Match Deaths and Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/skihikingkevin/pubg-match-deaths) |
| Seattle Airbnb Open Data | kaggle | [바로가기](https://www.kaggle.com/datasets/airbnb/seattle) |
| U.S. Airbnb Open Data | kaggle | [바로가기](https://www.kaggle.com/datasets/kritikseth/us-airbnb-open-data) |
| UFC Fighters' Statistics Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/ufc-fighters-statistics) |
| WHO Suicide Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/szamil/who-suicide-statistics) |
| Youtube Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/advaypatil/youtube-statistics) |
| Age Structure | ourworldindata | [바로가기](https://ourworldindata.org/age-structure) |
| Alcohol Consumption | ourworldindata | [바로가기](https://ourworldindata.org/alcohol-consumption) |
| Animal Welfare | ourworldindata | [바로가기](https://ourworldindata.org/animal-welfare) |
| Animal Welfare Explore the number of animals slaughtered and welfare impacts | ourworldindata | [바로가기](https://ourworldindata.org/explorers/animal-welfare) |
| Antibiotics and Antibiotic Resistance | ourworldindata | [바로가기](https://ourworldindata.org/antibiotics) |
| Bioenergy and Biofuels | ourworldindata | [바로가기](https://ourworldindata.org/bioenergy-biofuels) |
| Cardiovascular Diseases | ourworldindata | [바로가기](https://ourworldindata.org/cardiovascular-diseases) |
| Causes of Death | ourworldindata | [바로가기](https://ourworldindata.org/causes-of-death) |
| Conflict Data Source Explore the world's conflicts through the leading approaches to measuring them | ourworldindata | [바로가기](https://ourworldindata.org/explorers/conflict-data-source) |
| Conflict Explore the world's conflicts through their deaths, number, and locations | ourworldindata | [바로가기](https://ourworldindata.org/explorers/conflict-data) |
| Countries in Conflict Explore conflict deaths and death rates across the world's countries | ourworldindata | [바로가기](https://ourworldindata.org/explorers/countries-in-conflict-data) |
| Democracy Explore changes in the world's democratic and non-democratic systems | ourworldindata | [바로가기](https://ourworldindata.org/explorers/democracy) |
| Diarrheal Diseases | ourworldindata | [바로가기](https://ourworldindata.org/diarrheal-diseases) |
| Environmental Impacts of Food Production | ourworldindata | [바로가기](https://ourworldindata.org/environmental-impacts-of-food) |
| Eradication of Diseases | ourworldindata | [바로가기](https://ourworldindata.org/eradication-of-diseases) |
| Fertility Rate | ourworldindata | [바로가기](https://ourworldindata.org/fertility-rate) |
| Fertilizers Explore the use and impact of fertilizers across the world | ourworldindata | [바로가기](https://ourworldindata.org/explorers/fertilizers) |
| Food Prices Explore the cost and affordability of diets across the world | ourworldindata | [바로가기](https://ourworldindata.org/explorers/food-prices) |
| Forests and Deforestation | ourworldindata | [바로가기](https://ourworldindata.org/forests-and-deforestation) |
| Fossil Fuels | ourworldindata | [바로가기](https://ourworldindata.org/fossil-fuels) |
| Fossil Fuels Explore reserves, production, trade, and consumption of fossil fuels | ourworldindata | [바로가기](https://ourworldindata.org/explorers/natural-resources) |
| Global Food Explore the world's food system, from production to supply | ourworldindata | [바로가기](https://ourworldindata.org/explorers/global-food) |
| Healthcare Spending | ourworldindata | [바로가기](https://ourworldindata.org/financing-healthcare) |
| HIV/AIDS | ourworldindata | [바로가기](https://ourworldindata.org/hiv-aids) |
| Illicit Drug Use | ourworldindata | [바로가기](https://ourworldindata.org/illicit-drug-use) |
| Influenza | ourworldindata | [바로가기](https://ourworldindata.org/influenza) |
| IPCC Scenarios Explore the global shared socioeconomic pathways used in IPCC scenarios | ourworldindata | [바로가기](https://ourworldindata.org/explorers/ipcc-scenarios) |
| Life Expectancy | ourworldindata | [바로가기](https://ourworldindata.org/life-expectancy) |
| Malaria | ourworldindata | [바로가기](https://ourworldindata.org/malaria) |
| Metals and Minerals | ourworldindata | [바로가기](https://ourworldindata.org/metals-minerals) |
| Minerals Explore the production, reserves and value of minerals | ourworldindata | [바로가기](https://ourworldindata.org/explorers/minerals) |
| Mpox (monkeypox) | ourworldindata | [바로가기](https://ourworldindata.org/mpox) |
| Natural Disasters | ourworldindata | [바로가기](https://ourworldindata.org/natural-disasters) |
| Natural Disasters Explore the global frequency, severity, and consequences of disasters | ourworldindata | [바로가기](https://ourworldindata.org/explorers/natural-disasters) |
| Neglected Tropical Diseases | ourworldindata | [바로가기](https://ourworldindata.org/neglected-tropical-diseases) |
| Obesity | ourworldindata | [바로가기](https://ourworldindata.org/obesity) |
| Oil Spills | ourworldindata | [바로가기](https://ourworldindata.org/oil-spills) |
| Ozone Layer | ourworldindata | [바로가기](https://ourworldindata.org/ozone-layer) |
| Pandemics | ourworldindata | [바로가기](https://ourworldindata.org/pandemics) |
| Pneumonia | ourworldindata | [바로가기](https://ourworldindata.org/pneumonia) |
| Polio | ourworldindata | [바로가기](https://ourworldindata.org/polio) |
| Smallpox | ourworldindata | [바로가기](https://ourworldindata.org/smallpox) |
| Smoking | ourworldindata | [바로가기](https://ourworldindata.org/smoking) |
| Species Habitat Availability Explore future projections of species' habitats under different agricultural interventions | ourworldindata | [바로가기](https://ourworldindata.org/explorers/habitat-loss) |
| Suicides | ourworldindata | [바로가기](https://ourworldindata.org/suicide) |
| Tetanus | ourworldindata | [바로가기](https://ourworldindata.org/tetanus) |
| Tuberculosis | ourworldindata | [바로가기](https://ourworldindata.org/tuberculosis) |
| Urbanization | ourworldindata | [바로가기](https://ourworldindata.org/urbanization) |
| Vaccination | ourworldindata | [바로가기](https://ourworldindata.org/vaccination) |
| Wildfires | ourworldindata | [바로가기](https://ourworldindata.org/wildfires) |
| Aquastat | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/FAO_AS) |
| Aqueduct 4.0 Current and Future Country Rankings | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WRI_AQDT) |
| Artificial Intelligence (AI) Preparedness Index | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_AI) |
| Balance of Payments (BOP) and International Investment Position (IIP) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_BOP) |
| Benchmarking Infrastructure Development | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_BID) |
| BOOST: Open Budget Portal | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_BOOST) |
| Broadband and Telecom Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/OECD_BROADBAND) |
| Commodity Terms of Trade | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_PCTOT) |
| Cost and Affordability of a Healthy Diet (CoAHD) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/FAO_CAHD) |
| Democracy Index | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/EIU_DI) |
| Digital Economy and Technology | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/UNCTAD_DE) |
| Direction of Trade Statistics (DOTS) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_DOT) |
| EM Thematic Bond Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IFC_GB) |
| Emissions Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/FAO_EMS) |
| Emissions Database for Global Atmospheric Research (EDGAR) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/JRC_EDGAR) |
| Emissions Totals | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/FAO_EMSTOT) |
| Fiscal Decentralization | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_FISCALDECENTRALIZATION) |
| Fiscal Monitor (FM) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_FM) |
| Food Balance Sheet | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/FAO_FBS) |
| Fossil Fuel Subsidies | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_FFS) |
| Global Competitiveness Index (GCI) 4.0 | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WEF_GCI) |
| Global Cybersecurity Index | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/ITU_GCI) |
| Global Database Of Shared Prosperity | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_SHP) |
| Global Economic Prospects | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_GEP) |
| Global Emerging Markets (GEMs) Risk Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IFC_GEM) |
| Global Findex Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_FINDEX) |
| Global Productivity: A Cross-country Database of Productivity | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_ASPD) |
| Human Capital Index (HCI) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_HCI) |
| Human Capital Index Plus (HCI+) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_HCIP) |
| Human Capital Project (HCP) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_HCP) |
| ICT Regulatory Tracker | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/ITU_ICT) |
| Identification for Development (ID4D) Global Dataset | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_ID4D) |
| Informal Economy Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_INFECDB) |
| Infralatam | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IDB_INFRALATAM) |
| Intellectual Property Statistics - Patent indicators | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WIPO_ICT) |
| Interconnection Database, Number of Connected Data Centers | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/PEERING_DB) |
| International Debt Statistics (IDS) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_IDS) |
| International Reserves and Foreign Currency Liquidity (IRFCL) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_IRFCL) |
| Internet Exchange Directory | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/PCH_IXP) |
| Maritime Transport | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/UNCTAD_MT) |
| Nations in Transit | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/FH_NIT) |
| OECD Artificial Intelligence | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/OECD_AI) |
| Political Regime Characteristics Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/POLITY5_PRC) |
| Product Market Regulation Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/OECDWBG_PMR) |
| Rule of Law Index | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WJP_ROL) |
| SDG Indicators | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/FAO_SDGB) |
| Sendai Framework Monitor (SFM) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/UNDRR_SFM) |
| Statistical Performance Indicators (SPI) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_SPI) |
| Sustainable Development Goals (SDG) Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/UN_SDG) |
| Sustainable Governance Indicators (SGI) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/BS_SGI) |
| Think Hazard! | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_THINK_HAZARD) |
| Trade in Value Added (TiVA) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/OECD_TIVA) |
| Travel and Tourism Development Index (TTDI) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WEF_TTDI) |
| UNSD Environmental Indicators | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/UNSD_EI) |
| What a Waste Global Database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_WWGD) |
| Women, Business and the Law (WBL) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_WBL) |
| World Development Indicators (WDI) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_WDI) |
| World Economic Outlook (WEO) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_WEO) |
| World Integrated Trade Solution (WITS) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_WITS) |
| Worldwide Bureaucracy Indicators (WWBI) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_WWBI) |

### social (총 352개)

| dataset_name | source | link |
|---|---|---|
| 1940 Census Population Schedules, Enumeration District Maps, and Enumeration District Descriptions | aws_open_data | [바로가기](https://registry.opendata.aws/nara-1940-census/) |
| 1950 Census Population Schedules, Enumeration District Maps, and Enumeration District Descriptions | aws_open_data | [바로가기](https://registry.opendata.aws/nara-1950-census/) |
| 2010 Census Production Settings Demographic and Housing Characteristics (DHC) Demonstration Noisy Measurement File | aws_open_data | [바로가기](https://registry.opendata.aws/census-2010-dhc-nmf/) |
| 2010 Census Production Settings Redistricting Data (P.L. 94-171) Demonstration Noisy Measurement File | aws_open_data | [바로가기](https://registry.opendata.aws/census-2010-pl94-nmf/) |
| 2020 Census Demographic and Housing Characteristics (DHC) Noisy Measurement File | aws_open_data | [바로가기](https://registry.opendata.aws/census-2020-dhc-nmf/) |
| 2020 Census Redistricting Data (P.L. 94-171) Noisy Measurement File | aws_open_data | [바로가기](https://registry.opendata.aws/census-2020-pl94-nmf/) |
| 2020 Redistricting Data File Least Squares Estimates | aws_open_data | [바로가기](https://registry.opendata.aws/census-2020-pl94-gls/) |
| Catalina Sky Survey (CSS) subset data on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/sbn-css/) |
| CZ CELLxGENE Discover Census | aws_open_data | [바로가기](https://registry.opendata.aws/czi-cellxgene-census/) |
| Estimating Confidence Intervals for 2020 Census Statistics Using Approximate Monte Carlo Simulation (2010 Census Proof of Concept) | aws_open_data | [바로가기](https://registry.opendata.aws/census-2010-amc-mdf-replicates/) |
| Estimating Confidence Intervals for 2020 Census Statistics Using Approximate Monte Carlo Simulation (2020 Census Production Run) | aws_open_data | [바로가기](https://registry.opendata.aws/census-2020-amc-mdf-replicates/) |
| Gulfwide Avian Colony Monitoring Survey Photos | aws_open_data | [바로가기](https://registry.opendata.aws/gulfwide-avian-monitoring/) |
| High Resolution Population Density Maps + Demographic Estimates by CIESIN and Meta | aws_open_data | [바로가기](https://registry.opendata.aws/dataforgood-fb-hrsl/) |
| IBL Behavioral Data on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/ibl-behaviour/) |
| Pan-STARRS PS1 Survey | aws_open_data | [바로가기](https://registry.opendata.aws/mast-panstarrs/) |
| Social Gene Ref Seq Databases | aws_open_data | [바로가기](https://registry.opendata.aws/socialgene/) |
| SPHEREx Quick Release (QR): An All-Sky Spectral Survey | aws_open_data | [바로가기](https://registry.opendata.aws/spherex-qr/) |
| The JWST Advanced Extragalactic Survey JADES | aws_open_data | [바로가기](https://registry.opendata.aws/mast-jades/) |
| U.S. Census ACS PUMS | aws_open_data | [바로가기](https://registry.opendata.aws/census-dataworld-pums/) |
| ahca-polls | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/ahca-polls) |
| airline-safety | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/airline-safety) |
| alcohol-consumption | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption) |
| antiquities-act | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/antiquities-act) |
| august-senate-polls | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/august-senate-polls) |
| bad-drivers | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/bad-drivers) |
| bechdel | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/bechdel) |
| biopics | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/biopics) |
| births | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/births) |
| buster-posey-mvp | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/buster-posey-mvp) |
| cabinet-turnover | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/cabinet-turnover) |
| candy-power-ranking | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking) |
| chess-transfers | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/chess-transfers) |
| college-majors | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/college-majors) |
| comic-characters | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/comic-characters) |
| comma-survey | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/comma-survey) |
| congress-age | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/congress-age) |
| congress-biden-score | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/congress-biden-score) |
| congress-demographics | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/congress-demographics) |
| congress-generic-ballot | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/congress-generic-ballot) |
| congress-resignations | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/congress-resignations) |
| congress-trump-score | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/congress-trump-score) |
| cousin-marriage | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/cousin-marriage) |
| democratic-bench | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/democratic-bench) |
| district-urbanization-index-2022 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/district-urbanization-index-2022) |
| drug-use-by-age | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/drug-use-by-age) |
| early-senate-polls | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/early-senate-polls) |
| election-deniers | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/election-deniers) |
| election-forecasts-2020 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/election-forecasts-2020) |
| election-forecasts-2022 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/election-forecasts-2022) |
| elo-blatter | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/elo-blatter) |
| endorsements | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/endorsements) |
| endorsements-june-30 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/endorsements-june-30) |
| fandango | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/fandango) |
| flying-etiquette-survey | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/flying-etiquette-survey) |
| foul-balls | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/foul-balls) |
| goose | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/goose) |
| gop-candidate-visits-2024 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/gop-candidate-visits-2024) |
| gop-delegate-benchmarks-2024 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/gop-delegate-benchmarks-2024) |
| hate-crimes | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/hate-crimes) |
| hip-hop-candidate-lyrics | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/hip-hop-candidate-lyrics) |
| historical-ncaa-forecasts | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/historical-ncaa-forecasts) |
| impeachment-polls | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/impeachment-polls) |
| inconvenient-sequel | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/inconvenient-sequel) |
| infrastructure-jobs | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/infrastructure-jobs) |
| lebron | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/lebron) |
| librarians | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/librarians) |
| mad-men | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/mad-men) |
| male-flight-attendants | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/male-flight-attendants) |
| marriage | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/marriage) |
| masculinity-survey | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/masculinity-survey) |
| mayweather-mcgregor | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/mayweather-mcgregor) |
| media-mentions-2020 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/media-mentions-2020) |
| most-common-name | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/most-common-name) |
| mueller-polls | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/mueller-polls) |
| murder_2016 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/murder_2016) |
| next-bechdel | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/next-bechdel) |
| non-voters | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/non-voters) |
| nutrition-studies | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/nutrition-studies) |
| obama-commutations | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/obama-commutations) |
| off-year-turnout-2023 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/off-year-turnout-2023) |
| partisan-lean | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/partisan-lean) |
| pew-religions | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/pew-religions) |
| police-killings | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/police-killings) |
| police-locals | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/police-locals) |
| political-elasticity-scores | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/political-elasticity-scores) |
| poll-of-pollsters | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/poll-of-pollsters) |
| poll-quiz-guns | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/poll-quiz-guns) |
| polls | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/polls) |
| pollster-ratings | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/pollster-ratings) |
| potential-candidates | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/potential-candidates) |
| presidential-campaign-trail | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/presidential-campaign-trail) |
| presidential-candidate-favorables-2019 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/presidential-candidate-favorables-2019) |
| presidential-commencement-speeches | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/presidential-commencement-speeches) |
| primary-candidates-2018 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/primary-candidates-2018) |
| primary-project-2022 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/primary-project-2022) |
| puerto-rico-media | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/puerto-rico-media) |
| pulitzer | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/pulitzer) |
| quiet-caucus-2024 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/quiet-caucus-2024) |
| rare-pepes | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/rare-pepes) |
| redistricting-2022-state-legislatures | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/redistricting-2022-state-legislatures) |
| redistricting-alternate-maps | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/redistricting-alternate-maps) |
| redlining | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/redlining) |
| region-survey | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/region-survey) |
| religion-survey | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/religion-survey) |
| reluctant-trump | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/reluctant-trump) |
| repeated-phrases-gop | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/repeated-phrases-gop) |
| riddler-castles | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/riddler-castles) |
| riddler-pick-lowest | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/riddler-pick-lowest) |
| russia-investigation | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/russia-investigation) |
| russian-troll-tweets | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/russian-troll-tweets) |
| san-andreas | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/san-andreas) |
| sandy-311-calls | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/sandy-311-calls) |
| science-giving | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/science-giving) |
| scrabble-games | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/scrabble-games) |
| sleeping-alone-data | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/sleeping-alone-data) |
| soccer-spi | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/soccer-spi) |
| special-elections | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/special-elections) |
| sports-political-donations | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/sports-political-donations) |
| state-of-the-polls-2024 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/state-of-the-polls-2024) |
| state-of-the-state | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/state-of-the-state) |
| steak-survey | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/steak-survey) |
| study-drugs | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/study-drugs) |
| subreddit-algebra | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/subreddit-algebra) |
| tenth-circuit | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/tenth-circuit) |
| terrorism | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/terrorism) |
| thanksgiving-2015 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/thanksgiving-2015) |
| the-big-lies-long-shadow | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/the-big-lies-long-shadow) |
| trump-2-poll-issue-questions | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/trump-2-poll-issue-questions) |
| trump-approval-ratings | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/trump-approval-ratings) |
| trump-lawsuits | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/trump-lawsuits) |
| trump-world-trust | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/trump-world-trust) |
| undefeated-boxers | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/undefeated-boxers) |
| unisex-names | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/unisex-names) |
| urbanization-index | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/urbanization-index) |
| voter-registration | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/voter-registration) |
| wnba-forecasts | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/wnba-forecasts) |
| 1.3M Linkedin Jobs and Skills (2024) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024) |
| 1.6 million UK traffic accidents | kaggle | [바로가기](https://www.kaggle.com/datasets/daveianhickey/2000-16-traffic-flow-england-scotland-wales) |
| 2016 US Election | kaggle | [바로가기](https://www.kaggle.com/datasets/benhamner/2016-us-election) |
| 2017 Kaggle Machine Learning and Data Science Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/kaggle-survey-2017) |
| 2018 Kaggle Machine Learning and Data Science Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/kaggle-survey-2018) |
| 2020 US General Election Turnout Rates | kaggle | [바로가기](https://www.kaggle.com/datasets/imoore/2020-us-general-election-turnout-rates) |
| 2022 Russia Ukraine War | kaggle | [바로가기](https://www.kaggle.com/datasets/piterfm/2022-ukraine-russian-war) |
| 2024 USA Election Polling Data | kaggle | [바로가기](https://www.kaggle.com/datasets/iamtanmayshukla/2024-u-s-election-generic-ballot-polling-data) |
| 500 Person Gender-Height-Weight-Body Mass Index | kaggle | [바로가기](https://www.kaggle.com/datasets/yersever/500-person-gender-height-weight-bodymassindex) |
| 7+ Million Company Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/peopledatalabssf/free-7-million-company-dataset) |
| Accidents in France from 2005 to 2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/ahmedlahlou/accidents-in-france-from-2005-to-2016) |
| Adult Census Income | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/adult-census-income) |
| Adult income dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/wenruliu/adult-income-dataset) |
| Aerial Bombing Operations in World War II | kaggle | [바로가기](https://www.kaggle.com/datasets/usaf/world-war-ii) |
| AI Assistant Usage in Student Life | kaggle | [바로가기](https://www.kaggle.com/datasets/ayeshasal89/ai-assistant-usage-in-student-life-synthetic) |
| AI Impact on Jobs 2030 | kaggle | [바로가기](https://www.kaggle.com/datasets/khushikyad001/ai-impact-on-jobs-2030) |
| AI-Powered Job Market Insights | kaggle | [바로가기](https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights) |
| Airbnb Listings 2016 Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/alexanderfreberg/airbnb-listings-2016-dataset) |
| Airlines Customer satisfaction | kaggle | [바로가기](https://www.kaggle.com/datasets/sjleshrac/airlines-customer-satisfaction) |
| Amazon consumer Behaviour Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/swathiunnikrishnan/amazon-consumer-behaviour-dataset) |
| Analyzing Student Academic Trends | kaggle | [바로가기](https://www.kaggle.com/datasets/saadaliyaseen/analyzing-student-academic-trends) |
| Armenian Online Job Postings | kaggle | [바로가기](https://www.kaggle.com/datasets/udacity/armenian-online-job-postings) |
| Australian Election 2019 Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/taniaj/australian-election-2019-tweets) |
| Average Time Spent By A User On Social Media | kaggle | [바로가기](https://www.kaggle.com/datasets/imyjoshua/average-time-spent-by-a-user-on-social-media) |
| Boston Housing | kaggle | [바로가기](https://www.kaggle.com/datasets/schirmerchad/bostonhoustingmlnd) |
| Boston housing dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/altavish/boston-housing-dataset) |
| Boston Housing dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/arunjangir245/boston-housing-dataset) |
| Business and Industry Reports | kaggle | [바로가기](https://www.kaggle.com/datasets/census/business-and-industry-reports) |
| California Housing Data (1990) | kaggle | [바로가기](https://www.kaggle.com/datasets/harrywang/housing) |
| California Housing Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/camnugent/california-housing-prices) |
| Cambridge Crime Data | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/cambridge-crime-data-2009-2024) |
| Census Data for Go Daddy | kaggle | [바로가기](https://www.kaggle.com/datasets/cdeotte/census-data-for-godaddy) |
| Chicago Crime | kaggle | [바로가기](https://www.kaggle.com/datasets/chicago/chicago-crime) |
| College Student Placement Factors Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset) |
| Company Bankruptcy Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction) |
| Confused student EEG brainwave data | kaggle | [바로가기](https://www.kaggle.com/datasets/wanghaohan/confused-eeg) |
| Consumer Reviews of Amazon Products | kaggle | [바로가기](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products) |
| Cost of International Education | kaggle | [바로가기](https://www.kaggle.com/datasets/adilshamim8/cost-of-international-education) |
| Crime Data in Brazil | kaggle | [바로가기](https://www.kaggle.com/datasets/inquisitivecrow/crime-data-in-brazil) |
| Crime in India | kaggle | [바로가기](https://www.kaggle.com/datasets/rajanand/crime-in-india) |
| Crimes in Boston | kaggle | [바로가기](https://www.kaggle.com/datasets/ankkur13/boston-crime-data) |
| Customer Churn | kaggle | [바로가기](https://www.kaggle.com/datasets/barun2104/telecom-churn) |
| Customer Churn Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset) |
| Customer Clustering | kaggle | [바로가기](https://www.kaggle.com/datasets/dev0914sharma/customer-clustering) |
| Customer Personality Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) |
| Customer Purchase | kaggle | [바로가기](https://www.kaggle.com/datasets/ybifoundation/customer-purchase) |
| Customer Shopping (Latest Trends) Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/bhadramohit/customer-shopping-latest-trends-dataset) |
| Customer Shopping Dataset - Retail Sales Data | kaggle | [바로가기](https://www.kaggle.com/datasets/mehmettahiraslan/customer-shopping-dataset) |
| Customer Shopping Trends Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset) |
| Data Analyst Job Postings [Pay, Skills, Benefits] | kaggle | [바로가기](https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search) |
| Data Analyst Jobs | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/data-analyst-jobs) |
| Data Hackers Survey 2019-2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/datahackers/pesquisa-data-hackers-2019) |
| Data Science Job Posting on Glassdoor | kaggle | [바로가기](https://www.kaggle.com/datasets/rashikrahmanpritom/data-science-job-posting-on-glassdoor) |
| Data Science Job Salaries | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries) |
| Data Science Jobs Salaries Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries) |
| Data Science, AI and ML Job Salaries in 2025 | kaggle | [바로가기](https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs) |
| Data Scientist Job Market in the U.S | kaggle | [바로가기](https://www.kaggle.com/datasets/sl6149/data-scientist-job-market-in-the-us) |
| Demographics of Academy Awards (Oscars) Winners | kaggle | [바로가기](https://www.kaggle.com/datasets/fmejia21/demographics-of-academy-awards-oscars-winners) |
| Denver Crime Data | kaggle | [바로가기](https://www.kaggle.com/datasets/paultimothymooney/denver-crime-data) |
| e Commerce behavior data from multi category store | kaggle | [바로가기](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store) |
| E-Commerce Customer Behavior and Sales Analysis -TR | kaggle | [바로가기](https://www.kaggle.com/datasets/umuttuygurr/e-commerce-customer-behavior-and-sales-analysis-tr) |
| E-commerce Customer Behavior Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uom190346a/e-commerce-customer-behavior-dataset) |
| E-commerce Customer Data For Behavior Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/shriyashjagtap/e-commerce-customer-for-behavior-analysis) |
| E-Commerce Shipping Data | kaggle | [바로가기](https://www.kaggle.com/datasets/prachi13/customer-analytics) |
| Ecommerce Customer Churn Analysis and Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction) |
| Education and Career Success | kaggle | [바로가기](https://www.kaggle.com/datasets/adilshamim8/education-and-career-success) |
| Education in India | kaggle | [바로가기](https://www.kaggle.com/datasets/rajanand/education-in-india) |
| Education Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/theworldbank/education-statistics) |
| EU LGBT Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/ruslankl/european-union-lgbt-survey-2012) |
| Explore Datascience Opportunities on Linked In | kaggle | [바로가기](https://www.kaggle.com/datasets/marianadeem755/explore-exciting-opportunities-on-linkedin) |
| Extrovert vs. Introvert Behavior Data | kaggle | [바로가기](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data) |
| Filipino Family Income and Expenditure | kaggle | [바로가기](https://www.kaggle.com/datasets/grosvenpaul/family-income-and-expenditure) |
| Fortune 500 Companies of 2017 in US [Latest] | kaggle | [바로가기](https://www.kaggle.com/datasets/shaz13/fotune500-2017) |
| French employment, salaries, population per town | kaggle | [바로가기](https://www.kaggle.com/datasets/etiennelq/french-employment-by-town) |
| Gender Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/hb20007/gender-classification) |
| Gender Classification Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/cashutosh/gender-classification-dataset) |
| Gender Classification Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/elakiricoder/gender-classification-dataset) |
| Gender Recognition by Voice | kaggle | [바로가기](https://www.kaggle.com/datasets/primaryobjects/voicegender) |
| Global AI Job Market and Salary Trends 2025 | kaggle | [바로가기](https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025) |
| Google Job Skills | kaggle | [바로가기](https://www.kaggle.com/datasets/niyamatalmass/google-job-skills) |
| Hacker Rank Developer Survey 2018 | kaggle | [바로가기](https://www.kaggle.com/datasets/hackerrank/developer-survey-2018) |
| Housing in London | kaggle | [바로가기](https://www.kaggle.com/datasets/justinas/housing-in-london) |
| Housing price in Beijing | kaggle | [바로가기](https://www.kaggle.com/datasets/ruiqurm/lianjia) |
| Housing Price Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction) |
| Housing Price Prediction Data | kaggle | [바로가기](https://www.kaggle.com/datasets/muhammadbinimran/housing-price-prediction-data) |
| Housing Prices Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset) |
| Housing Prices in Metropolitan Areas of India | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/housing-prices-in-metropolitan-areas-of-india) |
| HR Analytics: Job Change of Data Scientists | kaggle | [바로가기](https://www.kaggle.com/datasets/arashnic/hr-analytics-job-change-of-data-scientists) |
| Income classification | kaggle | [바로가기](https://www.kaggle.com/datasets/lodetomasi1995/income-classification) |
| Income Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mastmustu/income) |
| Indian Companies Registration Data [1857 - 2020] | kaggle | [바로가기](https://www.kaggle.com/datasets/rowhitswami/all-indian-companies-registration-data-1900-2019) |
| Indian School Education Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/vidyapb/indian-school-education-statistics) |
| Job Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset) |
| Jobs and Salaries in Data Science | kaggle | [바로가기](https://www.kaggle.com/datasets/hummaamqaasim/jobs-in-data) |
| Latest Data Science Job Salaries 2020 - 2025 | kaggle | [바로가기](https://www.kaggle.com/datasets/saurabhbadole/latest-data-science-job-salaries-2024) |
| Linked In Job Postings (2023 - 2024) | kaggle | [바로가기](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings) |
| London Crime Data | kaggle | [바로가기](https://www.kaggle.com/datasets/LondonDataStore/london-crime) |
| London Crime Data, 2008-2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/jboysen/london-crime) |
| Melbourne Housing Market | kaggle | [바로가기](https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market) |
| Melbourne Housing Snapshot | kaggle | [바로가기](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot) |
| Merger and Acquisitions by Tech Companies | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/company-acquisitions-7-top-companies) |
| Mobile Device Usage and User Behavior Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset) |
| Multidimensional Poverty Measures | kaggle | [바로가기](https://www.kaggle.com/datasets/ophi/mpi) |
| New York City Current Job Postings | kaggle | [바로가기](https://www.kaggle.com/datasets/new-york-city/new-york-city-current-job-postings) |
| New York Housing Market | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market) |
| Oil Pipeline Accidents, 2010-Present | kaggle | [바로가기](https://www.kaggle.com/datasets/usdot/pipeline-accidents) |
| Online Job Postings | kaggle | [바로가기](https://www.kaggle.com/datasets/madhab/jobposts) |
| Philadelphia Crime Data | kaggle | [바로가기](https://www.kaggle.com/datasets/mchirico/philadelphiacrimedata) |
| Population by Country - 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/tanuprabhu/population-by-country-2020) |
| Population by labour status - Italy | kaggle | [바로가기](https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadspopolazionecsv) |
| Predict Student Performance | kaggle | [바로가기](https://www.kaggle.com/datasets/stealthtechnologies/predict-student-performance-dataset) |
| Predict students' dropout and academic success | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention) |
| Real /Fake Job Posting Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction) |
| Restaurant Data with Consumer Ratings | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/restaurant-data-with-consumer-ratings) |
| Salary Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor) |
| Shop Customer Data | kaggle | [바로가기](https://www.kaggle.com/datasets/datascientistanna/customers-dataset) |
| Sloan Digital Sky Survey DR14 | kaggle | [바로가기](https://www.kaggle.com/datasets/lucidlenn/sloan-digital-sky-survey) |
| social media engagement | kaggle | [바로가기](https://www.kaggle.com/datasets/divyaraj2006/social-media-engagement) |
| Social Media Engagement: A Comprehensive Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/mehmetisik/livedataset) |
| Social Media Influencers in 2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/ramjasmaurya/top-1000-social-media-channels) |
| Social Media Sentiments Analysis Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kashishparmar02/social-media-sentiments-analysis-dataset) |
| Social Media Surveillance | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/social-media-surveillance) |
| Social Media Usage and Emotional Well-Being | kaggle | [바로가기](https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being) |
| Social Media User Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/rockyt07/social-media-user-analysis) |
| Social Network Ads | kaggle | [바로가기](https://www.kaggle.com/datasets/rakeshrau/social-network-ads) |
| Social Power NBA | kaggle | [바로가기](https://www.kaggle.com/datasets/noahgift/social-power-nba) |
| Stack Overflow 2018 Developer Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/stackoverflow/stack-overflow-2018-developer-survey) |
| Stack Overflow Developer Survey, 2017 | kaggle | [바로가기](https://www.kaggle.com/datasets/stackoverflow/so-survey-2017) |
| Starbucks Customer Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/mahirahmzh/starbucks-customer-retention-malaysia-survey) |
| Stress Analysis in Social Media | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/stress-analysis-in-social-media) |
| Student Academic Performance Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ayeshasiddiqa123/student-perfirmance) |
| Student Academic Stress Real World Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/poushal02/student-academic-stress-real-world-dataset) |
| Student Alcohol Consumption | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption) |
| Student Depression Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset) |
| Student Depression Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/hopesb/student-depression-dataset) |
| Student Exam Performance Dataset Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/grandmaster07/student-exam-performance-dataset-analysis) |
| Student Exam Performance Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/mrsimple07/student-exam-performance-prediction) |
| Student exam score dataset analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/grandmaster07/student-exam-score-dataset-analysis) |
| Student Grade Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/dipam7/student-grade-prediction) |
| Student Habits vs Academic Performance | kaggle | [바로가기](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance) |
| student lifestyle dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset) |
| Student Marks Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/student-marks-dataset) |
| Student Performance | kaggle | [바로가기](https://www.kaggle.com/datasets/whenamancodes/student-performance) |
| Student Performance (Multiple Linear Regression) | kaggle | [바로가기](https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression) |
| Student Performance and Behavior Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset) |
| Student Performance Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/larsen0966/student-performance-data-set) |
| Student Performance Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/devansodariya/student-performance-data) |
| Student Performance Factors | kaggle | [바로가기](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors) |
| Student performance prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/rkiattisak/student-performance-in-mathematics) |
| Student Performance Predictions | kaggle | [바로가기](https://www.kaggle.com/datasets/haseebindata/student-performance-predictions) |
| Student Stress Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/wardabilal/student-stress-analysis) |
| Student stress factors | kaggle | [바로가기](https://www.kaggle.com/datasets/samyakb/student-stress-factors) |
| Student Stress Factors: A Comprehensive Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis) |
| Student Stress Monitoring Datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets) |
| Student Study Hours | kaggle | [바로가기](https://www.kaggle.com/datasets/himanshunakrani/student-study-hours) |
| Student Study Performance | kaggle | [바로가기](https://www.kaggle.com/datasets/bhavikjikadara/student-study-performance) |
| Student's math score for different teaching style | kaggle | [바로가기](https://www.kaggle.com/datasets/soumyadiptadas/students-math-score-for-different-teaching-style) |
| Students Adaptability Level in Online Education | kaggle | [바로가기](https://www.kaggle.com/datasets/mdmahmudulhasansuzan/students-adaptability-level-in-online-education) |
| Students enrolled. Higher education institutions | kaggle | [바로가기](https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadsetudiantscsv) |
| Students' Perceptions of AI in Education | kaggle | [바로가기](https://www.kaggle.com/datasets/gianinamariapetrascu/survey-on-students-perceptions-of-ai-in-education) |
| Students' Social Media Addiction | kaggle | [바로가기](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships) |
| Telco Customer Churn | kaggle | [바로가기](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| Telco customer churn: IBM dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset) |
| Telecom customer | kaggle | [바로가기](https://www.kaggle.com/datasets/abhinav89/telecom-customer) |
| Telecom Customer Churn Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/shilongzhuang/telecom-customer-churn-by-maven-analytics) |
| The Marvel Universe Social Network | kaggle | [바로가기](https://www.kaggle.com/datasets/csanhueza/the-marvel-universe-social-network) |
| Traffic Accidents | kaggle | [바로가기](https://www.kaggle.com/datasets/oktayrdeki/traffic-accidents) |
| U.S. Education Datasets: Unification Project | kaggle | [바로가기](https://www.kaggle.com/datasets/noriuk/us-education-datasets-unification-project) |
| U.S. Incomes by Occupation and Gender | kaggle | [바로가기](https://www.kaggle.com/datasets/jonavery/incomes-by-career-and-gender) |
| UCF Crime Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/odins0n/ucf-crime-dataset) |
| UK Car Accidents 2005-2015 | kaggle | [바로가기](https://www.kaggle.com/datasets/silicon99/dft-accident-data) |
| UK Housing Prices Paid | kaggle | [바로가기](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid) |
| UK Road Safety: Traffic Accidents and Vehicles | kaggle | [바로가기](https://www.kaggle.com/datasets/tsiaras/uk-road-safety-accidents-and-vehicles) |
| United States Census | kaggle | [바로가기](https://www.kaggle.com/datasets/census/census-bureau-usa) |
| US Accidents (2016 - 2023) | kaggle | [바로가기](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents) |
| US Adult Income | kaggle | [바로가기](https://www.kaggle.com/datasets/johnolafenwa/us-census-data) |
| US Census Demographic Data | kaggle | [바로가기](https://www.kaggle.com/datasets/muonneutrino/us-census-demographic-data) |
| US Dept of Education: College Scorecard | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/college-scorecard) |
| US Election 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/unanimad/us-election-2020) |
| US Election 2020 Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets) |
| US Household Income Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/goldenoakresearch/us-household-income-stats-geo-locations) |
| US Population By Zip Code | kaggle | [바로가기](https://www.kaggle.com/datasets/census/us-population-by-zip-code) |
| Wages by Education in the USA (1973-2022) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/wages-by-education-in-the-usa-1973-2022) |
| Women Entrepreneurship and Labor Force | kaggle | [바로가기](https://www.kaggle.com/datasets/babyoda/women-entrepreneurship-and-labor-force) |
| World Happiness Report | kaggle | [바로가기](https://www.kaggle.com/datasets/unsdsn/world-happiness) |
| World Happiness Report 2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/PromptCloudHQ/world-happiness-report-2019) |
| World Happiness Report 2021 | kaggle | [바로가기](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021) |
| World Happiness Report up to 2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/mathurinache/world-happiness-report) |
| World Population Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset) |
| Young People Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/miroslavsabo/young-people-survey) |
| BNG(labor,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/73) |
| labor | openml | [바로가기](https://www.openml.org/d/4) |
| Gender Ratio | ourworldindata | [바로가기](https://ourworldindata.org/gender-ratio) |
| Migration | ourworldindata | [바로가기](https://ourworldindata.org/migration) |
| Migration Flows Explore global migration data, country-by-country | ourworldindata | [바로가기](https://ourworldindata.org/explorers/migration-flows) |
| Migration, Refugees, and Asylum Seekers Explore the migration of people across the world | ourworldindata | [바로가기](https://ourworldindata.org/explorers/migration) |
| Population and Demography Explore data from the United Nations World Population Prospects | ourworldindata | [바로가기](https://ourworldindata.org/explorers/population-and-demography) |
| Population Growth | ourworldindata | [바로가기](https://ourworldindata.org/population-growth) |
| Census Income | uci | [바로가기](https://archive.ics.uci.edu/dataset/20/census+income) |
| Adult Population Survey (APS) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/GEM_APS) |
| Consumer Price Indices | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/FAO_CP) |
| Coordinated Portfolio Investment Survey (CPIS) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_CPIS) |
| Education Statistics | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_EDSTATS) |
| Employment by economic activity | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/ILO_EMP) |
| Environment, Social and Governance (ESG) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_ESG) |
| Equality of Opportunity for Sexual and Gender Minorities (EQOSOGI) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_EQOSOGI) |
| Gender Statistics | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_GS) |
| Global Housing Watch, House Price-to-Income Ratio Around the World | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_GHW) |
| Macro Poverty Outlook (MPO) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_MPO) |
| Multidimensional Poverty Measure | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_MPM) |
| National Expert Survey (NES) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/GEM_NES) |
| Open Budget Survey | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IBP_OBS) |
| Poverty and Inequality Platform (PIP) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_PIP) |
| Social sustainability global database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_SSGD) |
| The Global Knowledge Partnership on Migration and Development (KNOMAD) database | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_KNOMAD) |
| UNESCO Education Statistics | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/UNESCO_UIS) |

### health (총 322개)

| dataset_name | source | link |
|---|---|---|
| Aging Mouse Brain Epigenetic | aws_open_data | [바로가기](https://registry.opendata.aws/salk-aging-mouse-brain-epigeneti/) |
| AI3 Protein-Ligand Binding Affinity Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ai3/) |
| Allen Brain Observatory - Visual Coding AWS Public Data Set | aws_open_data | [바로가기](https://registry.opendata.aws/allen-brain-observatory/) |
| Allen Institute for Brain Science - Synaptic Physiology Public Data Set | aws_open_data | [바로가기](https://registry.opendata.aws/allen-synphys/) |
| Allen Mouse Brain Atlas | aws_open_data | [바로가기](https://registry.opendata.aws/allen-mouse-brain-atlas/) |
| Alliance of Genome Resources | aws_open_data | [바로가기](https://registry.opendata.aws/alliance-genome-resources/) |
| Blue Brain Open Data | aws_open_data | [바로가기](https://registry.opendata.aws/bluebrain_opendata/) |
| Brain Encoding Response Generator (BERG) | aws_open_data | [바로가기](https://registry.opendata.aws/brain-encoding-response-generator/) |
| Brain Globe Atlases | aws_open_data | [바로가기](https://registry.opendata.aws/brainglobe/) |
| Brain/MINDS Marmoset Connectivity Resource on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/brainminds-marmoset-connectivity/) |
| Broad Genome References | aws_open_data | [바로가기](https://registry.opendata.aws/broad-references/) |
| Cancer Cell Line Encyclopedia (CCLE) | aws_open_data | [바로가기](https://registry.opendata.aws/ccle/) |
| Cancer Genome Characterization Initiatives - Burkitt Lymphoma, HIV+ Cervical Cancer | aws_open_data | [바로가기](https://registry.opendata.aws/cgci/) |
| CAncer MEtastases in LYmph n Odes challe Nge (CAMELYON) Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/camelyon/) |
| CIViC (Clinical Interpretation of Variants in Cancer) | aws_open_data | [바로가기](https://registry.opendata.aws/civic/) |
| Clinical Proteomic Tumor Analysis Consortium 2 (CPTAC-2) | aws_open_data | [바로가기](https://registry.opendata.aws/cptac-2/) |
| Clinical Proteomic Tumor Analysis Consortium 3 (CPTAC-3) | aws_open_data | [바로가기](https://registry.opendata.aws/cptac-3/) |
| Clinical Trial Sequencing Project - Diffuse Large B-Cell Lymphoma | aws_open_data | [바로가기](https://registry.opendata.aws/ctsp-dlbcl/) |
| Clinical Ultrasound Image Repository | aws_open_data | [바로가기](https://registry.opendata.aws/clinical-ultrasound-image-data/) |
| Covid Job Impacts - US Hiring Data Since March 1 2020 | aws_open_data | [바로가기](https://registry.opendata.aws/us-hiring-rates-pandemic/) |
| COVID-19 Data Lake | aws_open_data | [바로가기](https://registry.opendata.aws/aws-covid19-lake/) |
| COVID-19 Genome Sequence Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ncbi-covid-19/) |
| COVID-19 Harmonized Data | aws_open_data | [바로가기](https://registry.opendata.aws/talend-covid19/) |
| COVID-19 Molecular Structure and Therapeutics Hub | aws_open_data | [바로가기](https://registry.opendata.aws/molssi-covid19-hub/) |
| COVID-19 Open Research Dataset (CORD-19) | aws_open_data | [바로가기](https://registry.opendata.aws/cord-19/) |
| Deep Drug Protein Embeddings Bank (DPEB) | aws_open_data | [바로가기](https://registry.opendata.aws/deepdrug-dpeb/) |
| DHARANI Developing Human-Brain Atlas | aws_open_data | [바로가기](https://registry.opendata.aws/dharani-brain-dataset/) |
| DNAStack COVID19 SRA Data | aws_open_data | [바로가기](https://registry.opendata.aws/dnastack-covid-19-sra-data/) |
| Encyclopedia of DNA Elements (ENCODE) | aws_open_data | [바로가기](https://registry.opendata.aws/encode-project/) |
| Fly Brain Anatomy: Fly Light Gen1 and Split-GAL4 Imagery | aws_open_data | [바로가기](https://registry.opendata.aws/janelia-flylight/) |
| Foldingathome COVID-19 Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/foldingathome-covid19/) |
| Foundation Medicine Adult Cancer Clinical Dataset (FM-AD) | aws_open_data | [바로가기](https://registry.opendata.aws/fm-ad/) |
| Genome Aggregation Database (gnomAD) | aws_open_data | [바로가기](https://registry.opendata.aws/broad-gnomad/) |
| Genome Ark | aws_open_data | [바로가기](https://registry.opendata.aws/genomeark/) |
| Genome in a Bottle on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/giab/) |
| Genome Kit genomic data | aws_open_data | [바로가기](https://registry.opendata.aws/genomekit/) |
| Genomic Characterization of Metastatic Castration Resistant Prostate Cancer | aws_open_data | [바로가기](https://registry.opendata.aws/mcrpc/) |
| Golden Retriever Lifetime Study: Whole genome genotyping of Golden Retrievers on Axiom HD Arrays | aws_open_data | [바로가기](https://registry.opendata.aws/maf-genome/) |
| Google Brain Genomics Sequencing Dataset for Benchmarking and Development | aws_open_data | [바로가기](https://registry.opendata.aws/google-brain-genomics-public/) |
| Guy's Breast Cancer Lymph Nodes (GRAPE) | aws_open_data | [바로가기](https://registry.opendata.aws/guys-breast-cancer-lymph-nodes/) |
| Harvard-Emory ECG Database | aws_open_data | [바로가기](https://registry.opendata.aws/bdsp-heedb/) |
| Human and Mammalian Brain Atlas | aws_open_data | [바로가기](https://registry.opendata.aws/allen-hmba-releases/) |
| Human Cancer Models Initiative (HCMI) Cancer Model Development Center | aws_open_data | [바로가기](https://registry.opendata.aws/hcmi-cmdc/) |
| IBL Neuropixels Brainwide Map on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/ibl-brain-wide-map/) |
| iHART Whole Genome Sequencing Data Set | aws_open_data | [바로가기](https://registry.opendata.aws/ihart/) |
| In Rad COVID-19 X-Ray and CT Scans | aws_open_data | [바로가기](https://registry.opendata.aws/inlab-covid-19-images-dataset/) |
| Integrative Analysis of Lung Adenocarcinoma in Environment and Genetics Lung cancer Etiology (Phase 2) | aws_open_data | [바로가기](https://registry.opendata.aws/luad-eagle/) |
| Long Bench - cross-platform reference dataset profiling cancer cell lines with bulk and single-cell approaches | aws_open_data | [바로가기](https://registry.opendata.aws/longbench/) |
| Medical Segmentation Decathlon | aws_open_data | [바로가기](https://registry.opendata.aws/msd/) |
| MIMIC-III ('Medical Information Mart for Intensive Care') | aws_open_data | [바로가기](https://registry.opendata.aws/mimiciii/) |
| MIMIC-IV Clinical Database Demo | aws_open_data | [바로가기](https://registry.opendata.aws/mimic-iv-demo/) |
| MIMIC-IV-ECG: Diagnostic Electrocardiogram Matched Subset | aws_open_data | [바로가기](https://registry.opendata.aws/mimic-iv-ecg/) |
| Mouse Brain Anatomy: Mouse Light Imagery | aws_open_data | [바로가기](https://registry.opendata.aws/janelia-mouselight/) |
| Nanopore Reference Human Genome | aws_open_data | [바로가기](https://registry.opendata.aws/nanopore/) |
| National Cancer Institute Center for Cancer Research - Diffuse Large B Cell Lymphoma (DLBCL) Genomics and Expression | aws_open_data | [바로가기](https://registry.opendata.aws/nciccr-dlbcl/) |
| National Cancer Institute Imaging Data Commons (IDC) Collections | aws_open_data | [바로가기](https://registry.opendata.aws/nci-imaging-data-commons/) |
| NIH NLM NCBI Pub Med Central (PMC) Article Datasets - Full-Text Biomedical and Life Sciences Journal Articles on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/ncbi-pmc/) |
| NYUMets Brain Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/nyumets-brain/) |
| Open Bioinformatics Reference Data for Galaxy | aws_open_data | [바로가기](https://registry.opendata.aws/open-bio-ref-data/) |
| Open Human Genome Library | aws_open_data | [바로가기](https://registry.opendata.aws/openhgl/) |
| Open Neuro | aws_open_data | [바로가기](https://registry.opendata.aws/openneuro/) |
| Open Neuro Data | aws_open_data | [바로가기](https://registry.opendata.aws/open-neurodata/) |
| Open Protein Set | aws_open_data | [바로가기](https://registry.opendata.aws/openfold/) |
| Oregon Health and Science University Chronic Neutrophilic Leukemia Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ohsu-cnl/) |
| Pancreatic Cancer Organoid Profiling | aws_open_data | [바로가기](https://registry.opendata.aws/organoid-pancreatic/) |
| Protein Data Bank 3D Structural Biology Data | aws_open_data | [바로가기](https://registry.opendata.aws/pdb-3d-structural-biology-data/) |
| Protein Gym | aws_open_data | [바로가기](https://registry.opendata.aws/proteingym/) |
| REDASA COVID-19 Open Data | aws_open_data | [바로가기](https://registry.opendata.aws/redasa-covid-data/) |
| Refgenie reference genome assets | aws_open_data | [바로가기](https://registry.opendata.aws/refgenie/) |
| RNA structure by fragmentation frequency | aws_open_data | [바로가기](https://registry.opendata.aws/frag-struc/) |
| RSNA Screening Mammography Breast Cancer Detection (RSNA-SMBC) Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/rsna-screening-mammography-breast-cancer-detection/) |
| Seattle Alzheimer's Disease Brain Cell Atlas (SEA-AD) | aws_open_data | [바로가기](https://registry.opendata.aws/allen-sea-ad-atlas/) |
| Snp Eff and Snp Sift Genomic Variant Annotation Databases | aws_open_data | [바로가기](https://registry.opendata.aws/snpeff/) |
| SPARC: Datasets bridging the body and the brain | aws_open_data | [바로가기](https://registry.opendata.aws/sparc/) |
| SPaRCNet data:Seizures, Rhythmic and Periodic Patterns in ICU Electroencephalography | aws_open_data | [바로가기](https://registry.opendata.aws/bdsp-sparcnet/) |
| Synthea synthetic patient generator data in OMOP Common Data Model | aws_open_data | [바로가기](https://registry.opendata.aws/synthea-omop/) |
| The Cancer Dependency Map (Dep Map) Cancer Cell Line Encyclopedia (CCLE) Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/depmap-omics-ccle/) |
| The Cancer Genome Atlas | aws_open_data | [바로가기](https://registry.opendata.aws/tcga/) |
| The Genome Modeling System | aws_open_data | [바로가기](https://registry.opendata.aws/gmsdata/) |
| The Human Microbiome Project | aws_open_data | [바로가기](https://registry.opendata.aws/human-microbiome-project/) |
| The Human Sleep Project | aws_open_data | [바로가기](https://registry.opendata.aws/bdsp-hsp/) |
| The University of California San Francisco Brain Metastases Stereotactic Radiosurgery (UCSF-BMSR) MRI Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ucsf-bmsr/) |
| Toxicant Exposures and Responses by Genomic and Epigenomic Regulators of Transcription (TaRGET) | aws_open_data | [바로가기](https://registry.opendata.aws/targetepigenomics/) |
| UCSC Genome Browser Sequence and Annotations | aws_open_data | [바로가기](https://registry.opendata.aws/ucsc-genome-browser/) |
| University of British Columbia Sunflower Genome Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/ubc-sunflower-genome/) |
| covid-geography | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/covid-geography) |
| 1000 Cannabis Genomes Project | kaggle | [바로가기](https://www.kaggle.com/datasets/bigquery/genomics-cannabis) |
| 2019 Coronavirus dataset (January - February 2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/brendaso/2019-coronavirus-dataset-01212020-01262020) |
| [NeurIPS 2020] Data Science for COVID-19 (DS4C) | kaggle | [바로가기](https://www.kaggle.com/datasets/kimjihoo/coronavirusdataset) |
| Alzheimer's Disease Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset) |
| Augmented Alzheimer MRI Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset) |
| AV: Healthcare Analytics | kaggle | [바로가기](https://www.kaggle.com/datasets/shivan118/healthcare-analytics) |
| AV: Healthcare Analytics II | kaggle | [바로가기](https://www.kaggle.com/datasets/nehaprabhavalkar/av-healthcare-analytics-ii) |
| Br35H:: Brain Tumor Detection 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection) |
| Brain MRI Images for Brain Tumor Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection) |
| Brain MRI segmentation | kaggle | [바로가기](https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation) |
| Brain Stroke Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jillanisofttech/brain-stroke-dataset) |
| Brain stroke prediction dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/zzettrkalpakbal/full-filled-brain-stroke-dataset) |
| Brain Tumor | kaggle | [바로가기](https://www.kaggle.com/datasets/jakeshbohaju/brain-tumor) |
| Brain Tumor Classification (MRI) | kaggle | [바로가기](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri) |
| Brain Tumor Image Data Set: Semantic Segmentation | kaggle | [바로가기](https://www.kaggle.com/datasets/pkdarabi/brain-tumor-image-dataset-semantic-segmentation) |
| Brain Tumor MRI Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) |
| Brain Tumor Segmentation | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/brain-tumor-segmentation-in-mri-brats-2015) |
| Brain Tumor Segmentation(BraTS2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/awsaf49/brats2020-training-data) |
| Brain-EEG-Spectrograms | kaggle | [바로가기](https://www.kaggle.com/datasets/cdeotte/brain-eeg-spectrograms) |
| Brain-Spectrograms | kaggle | [바로가기](https://www.kaggle.com/datasets/cdeotte/brain-spectrograms) |
| Breast Cancer | kaggle | [바로가기](https://www.kaggle.com/datasets/reihanenamdari/breast-cancer) |
| Breast Cancer Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/nancyalaswad90/breast-cancer-dataset) |
| Breast cancer dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/wasiqaliyasir/breast-cancer-dataset) |
| Breast Cancer Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset) |
| Breast Cancer Gene Expression Profiles (METABRIC) | kaggle | [바로가기](https://www.kaggle.com/datasets/raghadalharbi/breast-cancer-gene-expression-profiles-metabric) |
| Breast Cancer Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/merishnasuwal/breast-cancer-prediction-dataset) |
| Breast Cancer Proteomes | kaggle | [바로가기](https://www.kaggle.com/datasets/piotrgrabo/breastcancerproteomes) |
| Breast Cancer Wisconsin (Diagnostic) Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) |
| Cancer Data | kaggle | [바로가기](https://www.kaggle.com/datasets/erdemtaha/cancer-data) |
| Cancer Inhibitors | kaggle | [바로가기](https://www.kaggle.com/datasets/xiaotawkaggle/inhibitors) |
| Cancer Patients Data | kaggle | [바로가기](https://www.kaggle.com/datasets/rishidamarla/cancer-patients-data) |
| Cardiovascular Disease dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) |
| Cardiovascular Diseases Risk Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/alphiree/cardiovascular-diseases-risk-prediction-dataset) |
| Cardiovascular_Disease_Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jocelyndumlao/cardiovascular-disease-dataset) |
| CBIS-DDSM: Breast Cancer Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/awsaf49/cbis-ddsm-breast-cancer-image-dataset) |
| Cervical Cancer largest dataset (Sipak Med) | kaggle | [바로가기](https://www.kaggle.com/datasets/prahladmehandiratta/cervical-cancer-largest-dataset-sipakmed) |
| Cervical Cancer Risk Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/loveall/cervical-cancer-risk-classification) |
| Chest X-ray (Covid-19 and Pneumonia) | kaggle | [바로가기](https://www.kaggle.com/datasets/prashant268/chest-xray-covid19-pneumonia) |
| Chronic Disease Indicators | kaggle | [바로가기](https://www.kaggle.com/datasets/cdc/chronic-disease) |
| Chronic KIdney Disease dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mansoordaku/ckdisease) |
| Cirrhosis Patient Survival Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/joebeachcapital/cirrhosis-patient-survival-prediction) |
| Corn or Maize Leaf Disease Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/smaranjitghose/corn-or-maize-leaf-disease-dataset) |
| Coronavirus (covid19) Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/smid80/coronavirus-covid19-tweets) |
| Coronavirus - Brazil | kaggle | [바로가기](https://www.kaggle.com/datasets/unanimad/corona-virus-brazil) |
| Coronavirus tweets NLP - Text Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/datatattle/covid-19-nlp-text-classification) |
| COVID -19 Coronavirus Pandemic Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/whenamancodes/covid-19-coronavirus-pandemic-dataset) |
| Covid Cases and Deaths World Wide | kaggle | [바로가기](https://www.kaggle.com/datasets/themrityunjaypathak/covid-cases-and-deaths-worldwide) |
| COVID-19 - Clinical Data to assess diagnosis | kaggle | [바로가기](https://www.kaggle.com/datasets/Sírio-Libanes/covid19) |
| COVID-19 All Vaccines Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/gpreda/all-covid19-vaccines-tweets) |
| COVID-19 and its Impact on Students | kaggle | [바로가기](https://www.kaggle.com/datasets/kunal28chaturvedi/covid19-and-its-impact-on-students) |
| Covid-19 Case Surveillance Public Use Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/arashnic/covid19-case-surveillance-public-use-dataset) |
| COVID-19 chest xray | kaggle | [바로가기](https://www.kaggle.com/datasets/bachrr/covid-chest-xray) |
| COVID-19 Clinical Trials dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/parulpandey/covid19-clinical-trials-dataset) |
| COVID-19 containment and mitigation measures | kaggle | [바로가기](https://www.kaggle.com/datasets/paultimothymooney/covid19-containment-and-mitigation-measures) |
| COVID-19 Corona Virus India Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/imdevskp/covid19-corona-virus-india-dataset) |
| COVID-19 Coronavirus Pandemic | kaggle | [바로가기](https://www.kaggle.com/datasets/rinichristy/covid19-coronavirus-pandemic) |
| COVID-19 CT scans | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/covid19-ct-scans) |
| COVID-19 data from John Hopkins University | kaggle | [바로가기](https://www.kaggle.com/datasets/antgoldbloom/covid19-data-from-john-hopkins-university) |
| COVID-19 dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/georgesaavedra/covid19-dataset) |
| COVID-19 Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/imdevskp/corona-virus-report) |
| COVID-19 Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/meirnizri/covid19-dataset) |
| Covid-19 Global Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset) |
| COVID-19 Healthy Diet Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mariaren/covid19-healthy-diet-dataset) |
| Covid-19 Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset) |
| COVID-19 in India | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-india) |
| COVID-19 in Italy | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-italy) |
| COVID-19 in USA | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-usa) |
| COVID-19 Indonesia Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/hendratno/covid19-indonesia) |
| COVID-19 patient pre-condition dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tanmoyx/covid19-patient-precondition-dataset) |
| COVID-19 Radiography Database | kaggle | [바로가기](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) |
| COVID-19 Symptoms Checker | kaggle | [바로가기](https://www.kaggle.com/datasets/iamhungundji/covid19-symptoms-checker) |
| COVID-19 Tracking Germany | kaggle | [바로가기](https://www.kaggle.com/datasets/headsortails/covid19-tracking-germany) |
| COVID-19 World Vaccination Progress | kaggle | [바로가기](https://www.kaggle.com/datasets/gpreda/covid-world-vaccination-progress) |
| COVID-19 World Vaccine Adverse Reactions | kaggle | [바로가기](https://www.kaggle.com/datasets/ayushggarg/covid19-vaccine-adverse-reactions) |
| COVID-19 Xray Dataset (Train and Test Sets) | kaggle | [바로가기](https://www.kaggle.com/datasets/khoongweihao/covid19-xray-dataset-train-test-sets) |
| COVID-19/SARS B-cell Epitope Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/futurecorporation/epitope-prediction) |
| COVID19 Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/gpreda/covid19-tweets) |
| CT Medical Images | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/siim-medical-images) |
| Death in the United States | kaggle | [바로가기](https://www.kaggle.com/datasets/cdc/mortality) |
| Diabetes | kaggle | [바로가기](https://www.kaggle.com/datasets/imtkaggleteam/diabetes) |
| Diabetes 130 US hospitals for years 1999-2008 | kaggle | [바로가기](https://www.kaggle.com/datasets/brandao/diabetes) |
| Diabetes Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset) |
| Diabetes Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mathchi/diabetes-data-set) |
| Diabetes Dataset - Pima Indians | kaggle | [바로가기](https://www.kaggle.com/datasets/nancyalaswad90/review) |
| Diabetes Health Indicators Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) |
| Diabetes Health Indicators Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mohankrishnathalla/diabetes-health-indicators-dataset) |
| Diabetes prediction dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) |
| Diabetes, Hypertension and Stroke Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/prosperchuks/health-dataset) |
| diabetes.csv | kaggle | [바로가기](https://www.kaggle.com/datasets/saurabh00007/diabetescsv) |
| Diabetics prediction using logistic regression | kaggle | [바로가기](https://www.kaggle.com/datasets/kandij/diabetes-dataset) |
| Diagnosis of COVID-19 and its clinical spectrum | kaggle | [바로가기](https://www.kaggle.com/datasets/einsteindata4u/covid19) |
| Disease Prediction Using Machine Learning | kaggle | [바로가기](https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning) |
| Disease Symptom Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset) |
| Disease Symptoms and Patient Profile Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uom190346a/disease-symptoms-and-patient-profile-dataset) |
| ECG Heartbeat Categorization Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/shayanfazeli/heartbeat) |
| EEG Brainwave Dataset: Feeling Emotions | kaggle | [바로가기](https://www.kaggle.com/datasets/birdy654/eeg-brainwave-dataset-feeling-emotions) |
| EEG data from basic sensory task in Schizophrenia | kaggle | [바로가기](https://www.kaggle.com/datasets/broach/button-tone-sz) |
| EEG-Alcohol | kaggle | [바로가기](https://www.kaggle.com/datasets/nnair25/Alcoholics) |
| Employee Attrition for Healthcare | kaggle | [바로가기](https://www.kaggle.com/datasets/jpmiller/employee-attrition-for-healthcare) |
| Fetal Health Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification) |
| Global Hospital Beds Capacity (for covid-19) | kaggle | [바로가기](https://www.kaggle.com/datasets/ikiulian/global-hospital-beds-capacity-for-covid19) |
| Global Trends in Mental Health Disorder | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/uncover-global-trends-in-mental-health-disorder) |
| Health Analytics | kaggle | [바로가기](https://www.kaggle.com/datasets/rajanand/key-indicators-of-annual-health-survey) |
| Health care: Heart attack possibility | kaggle | [바로가기](https://www.kaggle.com/datasets/nareshbhat/health-care-data-set-on-heart-attack-possibility) |
| Health Insurance Coverage | kaggle | [바로가기](https://www.kaggle.com/datasets/hhs/health-insurance) |
| Health Insurance Cross Sell Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction) |
| Health Insurance Marketplace | kaggle | [바로가기](https://www.kaggle.com/datasets/hhs/health-insurance-marketplace) |
| Health Nutrition and Population Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/theworldbank/health-nutrition-and-population-statistics) |
| Healthcare Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) |
| Heart Attack Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fatemehmohammadinia/heart-attack-dataset-tarik-a-rashid) |
| Heart Attack Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/imnikhilanand/heart-attack-prediction) |
| Heart Attack Risk Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset) |
| Heart Disease | kaggle | [바로가기](https://www.kaggle.com/datasets/oktayrdeki/heart-disease) |
| Heart Disease and Stroke Prevention | kaggle | [바로가기](https://www.kaggle.com/datasets/mazharkarimi/heart-disease-and-stroke-prevention) |
| Heart Disease Cleveland UCI | kaggle | [바로가기](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci) |
| Heart Disease Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) |
| Heart Disease Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mexwell/heart-disease-dataset) |
| Heart Disease Health Indicators Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset) |
| Heart Disease Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction) |
| Heart Failure Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data) |
| Heart Failure Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) |
| Hospital Beds Management | kaggle | [바로가기](https://www.kaggle.com/datasets/jaderz/hospital-beds-management) |
| Hospital Charges for Inpatients | kaggle | [바로가기](https://www.kaggle.com/datasets/speedoheck/inpatient-hospital-charges) |
| Hospital ratings | kaggle | [바로가기](https://www.kaggle.com/datasets/center-for-medicare-and-medicaid/hospital-ratings) |
| Human Stress Detection in and through Sleep | kaggle | [바로가기](https://www.kaggle.com/datasets/laavanya/human-stress-detection-in-and-through-sleep) |
| Impact of Covid-19 Pandemic on the Global Economy | kaggle | [바로가기](https://www.kaggle.com/datasets/shashwatwork/impact-of-covid19-pandemic-on-the-global-economy) |
| Indian Liver Patient Records | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/indian-liver-patient-records) |
| Indicators of Heart Disease (2022 UPDATE) | kaggle | [바로가기](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease) |
| Indonesia-Coronavirus | kaggle | [바로가기](https://www.kaggle.com/datasets/ardisragen/indonesia-coronavirus-cases) |
| Industrial Safety and Health Analytics Database | kaggle | [바로가기](https://www.kaggle.com/datasets/ihmstefanini/industrial-safety-and-health-analytics-database) |
| LA Restaurant and Market Health Data | kaggle | [바로가기](https://www.kaggle.com/datasets/cityofLA/la-restaurant-market-health-data) |
| Latest Covid-19 India Statewise Data | kaggle | [바로가기](https://www.kaggle.com/datasets/anandhuh/latest-covid19-india-statewise-data) |
| Logistic regression To predict heart disease | kaggle | [바로가기](https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression) |
| Lung and Colon Cancer Histopathological Images | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/lung-and-colon-cancer-histopathological-images) |
| Lung Cancer | kaggle | [바로가기](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer) |
| Lung Cancer | kaggle | [바로가기](https://www.kaggle.com/datasets/nancyalaswad90/lung-cancer) |
| Lung Cancer Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/yusufdede/lung-cancer-dataset) |
| Lung Cancer Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/cancer-patients-and-air-pollution-a-new-link) |
| Lyme Disease Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/lyme-disease-dataset) |
| Maternal Health Risk Data | kaggle | [바로가기](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data) |
| Medical Appointment No Shows | kaggle | [바로가기](https://www.kaggle.com/datasets/joniarroba/noshowappointments) |
| Medical Cost Personal Datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/mirichoi0218/insurance) |
| Medical Image Data Set: Brain Tumor Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/pkdarabi/medical-image-dataset-brain-tumor-detection) |
| Medical Insurance Cost Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mosapabdelghany/medical-insurance-cost-dataset) |
| Medical MNIST | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/medical-mnist) |
| Medical Speech, Transcription, and Intent | kaggle | [바로가기](https://www.kaggle.com/datasets/paultimothymooney/medical-speech-transcription-and-intent) |
| Medical Student Mental Health | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/medical-student-mental-health) |
| Medical Transcriptions | kaggle | [바로가기](https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions) |
| Mental Health | kaggle | [바로가기](https://www.kaggle.com/datasets/imtkaggleteam/mental-health) |
| Mental Health and Suicide Rates | kaggle | [바로가기](https://www.kaggle.com/datasets/twinkle0705/mental-health-and-suicide-rates) |
| Mental Health Conversational Data | kaggle | [바로가기](https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data) |
| Mental Health Counseling Conversations | kaggle | [바로가기](https://www.kaggle.com/datasets/melissamonfared/mental-health-counseling-conversations-k) |
| Mental Health Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset) |
| Mental Health Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/programmerrdai/mental-health-dataset) |
| Mental Health FAQ for Chatbot | kaggle | [바로가기](https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot) |
| Mental Health in Tech Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey) |
| Mental Health in the Tech Industry | kaggle | [바로가기](https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry) |
| MESSIDOR-2 DR Grades | kaggle | [바로가기](https://www.kaggle.com/datasets/google-brain/messidor2-dr-grades) |
| Multi Cancer Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/obulisainaren/multi-cancer) |
| Music and Mental Health Survey Results | kaggle | [바로가기](https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results) |
| My Complete Genome | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/mygenome) |
| National Health and Nutrition Examination Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey) |
| OASIS Alzheimer's Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/ninadaithal/imagesoasis) |
| Ocular Disease Recognition | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k) |
| OSMI Mental Health in Tech Survey 2016 | kaggle | [바로가기](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-2016) |
| Parkinson Disease Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/debasisdotcom/parkinson-disease-detection) |
| Parkinson's Disease Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/vikasukani/parkinsons-disease-data-set) |
| Pima Indians Diabetes Database | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) |
| pima-indians-diabetes.csv | kaggle | [바로가기](https://www.kaggle.com/datasets/kumargh/pimaindiansdiabetescsv) |
| Plant disease recognition dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset) |
| Predict Diabetes | kaggle | [바로가기](https://www.kaggle.com/datasets/whenamancodes/predict-diabities) |
| Raw mouse mammary RNA-Seq data (fastq) | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/electedindianwomeninpanchayats) |
| Remote Work and Mental Health | kaggle | [바로가기](https://www.kaggle.com/datasets/waqi786/remote-work-and-mental-health) |
| Retinal Disease Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification) |
| RNA-seq Airway Data | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/indian-women-in-defense) |
| Saccharomyces cerevisiae - Yeast Genome | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/floodsdamageindia) |
| SARS CORONAVIRUS ACCESSION | kaggle | [바로가기](https://www.kaggle.com/datasets/jamzing/sars-coronavirus-accession) |
| Sentiment Analysis for Mental Health | kaggle | [바로가기](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health) |
| Skin Cancer Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/farjanakabirsamanta/skin-cancer-dataset) |
| Skin Cancer ISIC | kaggle | [바로가기](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic) |
| Skin Cancer MNIST: HAM10000 | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000) |
| Skin cancer: HAM10000 | kaggle | [바로가기](https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification) |
| Skin Cancer: Malignant vs. Benign | kaggle | [바로가기](https://www.kaggle.com/datasets/fanconic/skin-cancer-malignant-vs-benign) |
| Sleep Data | kaggle | [바로가기](https://www.kaggle.com/datasets/mathurinache/sleep-dataset) |
| Sleep Efficiency Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/equilibriumm/sleep-efficiency) |
| Sleep Health and Lifestyle Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) |
| Social Media and Mental Health | kaggle | [바로가기](https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health) |
| sRNA sequencing - Brain (GSE75140) | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/crimeagainstwomen) |
| Structural Protein Sequences | kaggle | [바로가기](https://www.kaggle.com/datasets/shahir/protein-data-set) |
| Student Mental health | kaggle | [바로가기](https://www.kaggle.com/datasets/shariful07/student-mental-health) |
| Student Mental Health Survey | kaggle | [바로가기](https://www.kaggle.com/datasets/abdullahashfaqvirk/student-mental-health-survey) |
| Thyroid Disease Data | kaggle | [바로가기](https://www.kaggle.com/datasets/jainaru/thyroid-disease-data) |
| Tomato leaf disease detection | kaggle | [바로가기](https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf) |
| Turkey Covid 19 Vaccination Data | kaggle | [바로가기](https://www.kaggle.com/datasets/omercolakoglu/turkey-covid-19-vaccination-data) |
| U.S. Healthcare Data | kaggle | [바로가기](https://www.kaggle.com/datasets/maheshdadhich/us-healthcare-data) |
| UCI Heart Disease Data | kaggle | [바로가기](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data) |
| US counties COVID 19 dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fireballbyedimyrnmom/us-counties-covid-19-dataset) |
| US Health Insurance Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset) |
| World Bank WDI 2.12 - Health Systems | kaggle | [바로가기](https://www.kaggle.com/datasets/danevans/world-bank-wdi-212-health-systems) |
| World Health Statistics 2020 Complete Geo-Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/utkarshxy/who-worldhealth-statistics-2020-complete) |
| Zika Virus, Whole Genome | kaggle | [바로가기](https://www.kaggle.com/datasets/usharengaraju/child-labour-in-inida) |
| BNG(breast-cancer,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/77) |
| BNG(heart-c,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/136) |
| BNG(heart-h,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/138) |
| BNG(heart-statlog,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/140) |
| breast-cancer | openml | [바로가기](https://www.openml.org/d/13) |
| diabetes | openml | [바로가기](https://www.openml.org/d/37) |
| heart-c | openml | [바로가기](https://www.openml.org/d/49) |
| heart-h | openml | [바로가기](https://www.openml.org/d/51) |
| heart-statlog | openml | [바로가기](https://www.openml.org/d/53) |
| postoperative-patient-data | openml | [바로가기](https://www.openml.org/d/34) |
| Burden of Disease | ourworldindata | [바로가기](https://ourworldindata.org/burden-of-disease) |
| Cancer | ourworldindata | [바로가기](https://ourworldindata.org/cancer) |
| Child and Infant Mortality | ourworldindata | [바로가기](https://ourworldindata.org/child-mortality) |
| COVID-19 | ourworldindata | [바로가기](https://ourworldindata.org/coronavirus) |
| COVID-19 Explore global data on COVID-19 | ourworldindata | [바로가기](https://ourworldindata.org/explorers/covid) |
| Global Health | ourworldindata | [바로가기](https://ourworldindata.org/health-meta) |
| Global Health Explore data on child and maternal health, diseases, life expectancy, and health systems around the world | ourworldindata | [바로가기](https://ourworldindata.org/explorers/global-health) |
| Impacts of Energy Production Explore the environmental and health impacts of electricity sources | ourworldindata | [바로가기](https://ourworldindata.org/explorers/impacts-of-energy-sources) |
| Influenza Explore global data produced by the World Health Organization on influenza symptoms and cases | ourworldindata | [바로가기](https://ourworldindata.org/explorers/influenza) |
| Maternal Mortality | ourworldindata | [바로가기](https://ourworldindata.org/maternal-mortality) |
| Mental Health | ourworldindata | [바로가기](https://ourworldindata.org/mental-health) |
| Mpox Explore the data produced by the World Health Organization and Africa CDC on mpox (monkeypox) | ourworldindata | [바로가기](https://ourworldindata.org/explorers/monkeypox) |
| Breast Cancer | uci | [바로가기](https://archive.ics.uci.edu/dataset/14/breast+cancer) |
| Breast Cancer Wisconsin (Original) | uci | [바로가기](https://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original) |
| CDC Diabetes Health Indicators | uci | [바로가기](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators) |
| Chronic Kidney Disease | uci | [바로가기](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease) |
| Diabetes 130-US Hospitals for Years 1999-2008 | uci | [바로가기](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) |
| Heart Failure Clinical Records | uci | [바로가기](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records) |
| Thyroid Disease | uci | [바로가기](https://archive.ics.uci.edu/dataset/102/thyroid+disease) |
| Country Fiscal Measures in Response to the COVID-19 Pandemic | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_FPR) |
| COVID-19 Business Pulse Surveys | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_BPS) |
| Global Health Observatory Indicators | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WHO_GHO) |
| Health Nutrition and Population Statistics | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_HNP) |
| Ocean Health Index (OHI) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/OHI_OHI) |
| Universal Health Coverage (UHC) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_UHC) |

### finance (총 224개)

| dataset_name | source | link |
|---|---|---|
| End-Use Load Profiles for the U.S. Building Stock | aws_open_data | [바로가기](https://registry.opendata.aws/nrel-pds-building-stock/) |
| World Bank - Light Every Night | aws_open_data | [바로가기](https://registry.opendata.aws/wb-light-every-night/) |
| World Bank Climate Change Knowledge Portal (CCKP) | aws_open_data | [바로가기](https://registry.opendata.aws/wbg-cckp/) |
| 200+ Financial Indicators of US stocks (2014-2018) | kaggle | [바로가기](https://www.kaggle.com/datasets/cnic92/200-financial-indicators-of-us-stocks-20142018) |
| 400+ crypto currency pairs at 1-minute resolution | kaggle | [바로가기](https://www.kaggle.com/datasets/tencars/392-crypto-currency-pairs-at-minute-resolution) |
| A millennium of macroeconomic data | kaggle | [바로가기](https://www.kaggle.com/datasets/bank-of-england/a-millennium-of-macroeconomic-data) |
| Adidas Sales Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/heemalichaudhari/adidas-sales-dataset) |
| Africa Economic, Banking and Systemic Crisis Data | kaggle | [바로가기](https://www.kaggle.com/datasets/chirin/africa-economic-banking-and-systemic-crisis-data) |
| Airbnb Prices in European Cities | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities) |
| ALGO TRADING DATA - Nifty 500 intraday data (2026) | kaggle | [바로가기](https://www.kaggle.com/datasets/debashis74017/algo-trading-data-nifty-100-data-with-indicators) |
| All Lending Club loan data | kaggle | [바로가기](https://www.kaggle.com/datasets/wordsforthewise/lending-club) |
| Amazon Products Sales Dataset 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset) |
| Amazon Sales Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset) |
| Amazon_Sales_Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/aliiihussain/amazon-sales-dataset) |
| AMEX, NYSE, NASDAQ stock histories | kaggle | [바로가기](https://www.kaggle.com/datasets/qks1lver/amex-nyse-nasdaq-stock-histories) |
| Australian Vehicle Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/australian-vehicle-prices) |
| Automobile Sales data | kaggle | [바로가기](https://www.kaggle.com/datasets/ddosad/auto-sales-data) |
| Avocado Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/neuromusic/avocado-prices) |
| Bakery Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/hosubjeong/bakery-sales) |
| Bank Account Fraud Dataset Suite (NeurIPS 2022) | kaggle | [바로가기](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022) |
| Bank Churn | kaggle | [바로가기](https://www.kaggle.com/datasets/hardikgarg03/bank-churn) |
| Bank Customer Churn | kaggle | [바로가기](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn) |
| Bank Customer Churn Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset) |
| Bank Customer Segmentation (1M+ Transactions) | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/bank-customer-segmentation) |
| Bank Loan Status Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/zaurbegiev/my-dataset) |
| Bank Marketing | kaggle | [바로가기](https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing) |
| Bank marketing campaigns dataset Opening Deposit | kaggle | [바로가기](https://www.kaggle.com/datasets/volodymyrgavrysh/bank-marketing-campaigns-dataset) |
| Bank Marketing Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset) |
| Bank personal loan | kaggle | [바로가기](https://www.kaggle.com/datasets/ahmadrafiee/bank-personal-loan) |
| Bank Transaction Data | kaggle | [바로가기](https://www.kaggle.com/datasets/apoorvwatsky/bank-transaction-data) |
| Bank Transaction Dataset for Fraud Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection) |
| Bank Turnover Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/barelydedicated/bank-customer-churn-modeling) |
| Bank_Loan_modelling | kaggle | [바로가기](https://www.kaggle.com/datasets/itsmesunil/bank-loan-modelling) |
| Banking Customer Churn Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/saurabhbadole/bank-customer-churn-prediction-dataset) |
| Banking Dataset - Marketing Targets | kaggle | [바로가기](https://www.kaggle.com/datasets/prakharrathi25/banking-dataset-marketing-targets) |
| Bengaluru House price data | kaggle | [바로가기](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) |
| Big Mart Sales Data | kaggle | [바로가기](https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data) |
| Bike Sales in Europe | kaggle | [바로가기](https://www.kaggle.com/datasets/sadiqshah/bike-sales-in-europe) |
| Bitcoin Blockchain Historical Data | kaggle | [바로가기](https://www.kaggle.com/datasets/bigquery/bitcoin-blockchain) |
| Bitcoin Historical Data | kaggle | [바로가기](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data) |
| Bitcoin Historical Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd) |
| BITCOIN Historical Datasets 2018-2026 Binance API | kaggle | [바로가기](https://www.kaggle.com/datasets/novandraanugrah/bitcoin-historical-datasets-2018-2024) |
| Bitcoin Price Prediction (Light Weight CSV) | kaggle | [바로가기](https://www.kaggle.com/datasets/team-ai/bitcoin-price-prediction) |
| Bitcoin Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets) |
| BMW Global Automotive Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/dmahajanbe23/bmw-global-automotive-sales) |
| Boston House Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/vikrishnan/boston-house-prices) |
| Brent Oil Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/mabusalah/brent-oil-prices) |
| Cafe Sales - Dirty Data for Cleaning Training | kaggle | [바로가기](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training) |
| Car Insurance Claim Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/ifteshanajnin/carinsuranceclaimprediction-classification) |
| Car sales | kaggle | [바로가기](https://www.kaggle.com/datasets/gagandeep16/car-sales) |
| Car Sales Dataset: Model, Features, and Pricing | kaggle | [바로가기](https://www.kaggle.com/datasets/msnbehdani/mock-dataset-of-second-hand-car-sales) |
| Car Sales Report | kaggle | [바로가기](https://www.kaggle.com/datasets/missionjee/car-sales-report) |
| Chocolate Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/saidaminsaidaxmadov/chocolate-sales) |
| Chocolate Sales Data | kaggle | [바로가기](https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales) |
| Churn for Bank Customers | kaggle | [바로가기](https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers) |
| Coffee Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/ihelon/coffee-sales) |
| Coffee Sales Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/navjotkaushal/coffee-sales-dataset) |
| Coffee Shop Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales) |
| Complete Historical Cryptocurrency Financial Data | kaggle | [바로가기](https://www.kaggle.com/datasets/philmohun/cryptocurrency-financial-data) |
| Credit Card Approval Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction) |
| Credit Card customers | kaggle | [바로가기](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers) |
| Credit Card Customers Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/whenamancodes/credit-card-customers-prediction) |
| Credit Card Dataset for Clustering | kaggle | [바로가기](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata) |
| Credit Card Fraud | kaggle | [바로가기](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud) |
| Credit Card Fraud Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/mishra5001/credit-card) |
| Credit Card Fraud Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) |
| Credit Card Fraud Detection Dataset 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023) |
| Credit Card Spending Habits in India | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/analyzing-credit-card-spending-habits-in-india) |
| Credit Card Transactions | kaggle | [바로가기](https://www.kaggle.com/datasets/ealtman2019/credit-card-transactions) |
| Credit Card Transactions Fraud Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kartik2112/fraud-detection) |
| Credit Risk Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/ranadeep/credit-risk-dataset) |
| Credit Risk Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/laotse/credit-risk-dataset) |
| Credit Risk Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/credit-risk-dataset) |
| Credit score classification | kaggle | [바로가기](https://www.kaggle.com/datasets/parisrohan/credit-score-classification) |
| Cryptocurrency Historical Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory) |
| Daily and Intraday Stock Price Data | kaggle | [바로가기](https://www.kaggle.com/datasets/borismarjanovic/daily-and-intraday-stock-price-data) |
| Daily Financial News for 6000+ Stocks | kaggle | [바로가기](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests) |
| Daily Historical Stock Prices (1970 - 2018) | kaggle | [바로가기](https://www.kaggle.com/datasets/ehallmar/daily-historical-stock-prices-1970-2018) |
| Daily News for Stock Market Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/aaron7sun/stocknews) |
| Default of Credit Card Clients Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset) |
| Diamonds Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/nancyalaswad90/diamonds-prices) |
| DJIA 30 Stock Time Series | kaggle | [바로가기](https://www.kaggle.com/datasets/szrlee/stock-time-series-20050101-to-20171231) |
| Dummy Marketing and Sales Data | kaggle | [바로가기](https://www.kaggle.com/datasets/harrimansaragih/dummy-advertising-and-sales-data) |
| E-commerce Business Transaction | kaggle | [바로가기](https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business) |
| E-Commerce Sales Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data) |
| Economic calendar Invest Forex https://t.me/econos | kaggle | [바로가기](https://www.kaggle.com/datasets/devorvant/economic-calendar) |
| Egg Sales of a local shop for 30 years | kaggle | [바로가기](https://www.kaggle.com/datasets/kanchana1990/egg-sales-of-a-local-shop-for-30-years) |
| Electronic Products and Pricing Data | kaggle | [바로가기](https://www.kaggle.com/datasets/datafiniti/electronic-products-prices) |
| EOD data for all Dow Jones stocks | kaggle | [바로가기](https://www.kaggle.com/datasets/timoboz/stock-data-dow-jones) |
| Ethereum Classic Blockchain | kaggle | [바로가기](https://www.kaggle.com/datasets/bigquery/crypto-ethereum-classic) |
| EUR USD Forex Pair Historical Data (2002 - 2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/imetomi/eur-usd-forex-pair-historical-data-2002-2019) |
| Europe Bike Store Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/prepinstaprime/europe-bike-store-sales) |
| Every Cryptocurrency Daily Market Price | kaggle | [바로가기](https://www.kaggle.com/datasets/jessevent/all-crypto-currencies) |
| Finance and Accounting Courses - Udemy (13K+ course) | kaggle | [바로가기](https://www.kaggle.com/datasets/jilkothari/finance-accounting-courses-udemy-13k-course) |
| Finance Data | kaggle | [바로가기](https://www.kaggle.com/datasets/nitindatta/finance-data) |
| Financial Distress Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/shebrahimi/financial-distress) |
| Financial Sentiment Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis) |
| Financial Transactions Dataset: Analytics | kaggle | [바로가기](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets) |
| Financial Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/davidwallach/financial-tweets) |
| Flight Price Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction) |
| Ford Car Price Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/adhurimquku/ford-car-price-prediction) |
| Fraud Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/whenamancodes/fraud-detection) |
| Gas Prices in Brazil | kaggle | [바로가기](https://www.kaggle.com/datasets/matheusfreitag/gas-prices-in-brazil) |
| German Credit Risk | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/german-credit) |
| Global Food Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/jboysen/global-food-prices) |
| Gold Price 10 Years 2013-2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/farzadnekouei/gold-price-10-years-20132023) |
| Gold Price Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sid321axn/gold-price-prediction-dataset) |
| Gold Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/tunguz/gold-prices) |
| Healthcare Insurance | kaggle | [바로가기](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance) |
| HEALTHCARE PROVIDER FRAUD DETECTION ANALYSIS | kaggle | [바로가기](https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis) |
| Historical Sales and Active Inventory | kaggle | [바로가기](https://www.kaggle.com/datasets/flenderson/sales-analysis) |
| Home Loan Approval | kaggle | [바로가기](https://www.kaggle.com/datasets/rishikeshkonapure/home-loan-approval) |
| House Price | kaggle | [바로가기](https://www.kaggle.com/datasets/juhibhojani/house-price) |
| House Price dataset of India | kaggle | [바로가기](https://www.kaggle.com/datasets/mohamedafsal007/house-price-dataset-of-india) |
| House Price Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/hardikgarg03/house-price-prediction) |
| House price prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/shree1992/housedata) |
| House Sales in King County, USA | kaggle | [바로가기](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction) |
| Huge Stock Market Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs) |
| Insurance Data | kaggle | [바로가기](https://www.kaggle.com/datasets/moneystore/agencyperformance) |
| Insurance Premium Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction) |
| Internet Prices around 200+ countries in 2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/ramjasmaurya/1-gb-internet-price) |
| Iowa Liquor Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/residentmario/iowa-liquor-sales) |
| Laptop Price | kaggle | [바로가기](https://www.kaggle.com/datasets/muhammetvarl/laptop-price) |
| Laptop Price Prediction using specifications | kaggle | [바로가기](https://www.kaggle.com/datasets/arnabchaki/laptop-price-prediction) |
| Laptop Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/owm4096/laptop-prices) |
| Lending Club Loan Data | kaggle | [바로가기](https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv) |
| Loan Approval Classification Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data) |
| Loan Data | kaggle | [바로가기](https://www.kaggle.com/datasets/itssuru/loan-data) |
| Loan Data | kaggle | [바로가기](https://www.kaggle.com/datasets/zhijinzhai/loandata) |
| Loan Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/burak3ergun/loan-data-set) |
| Loan Default Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/loan-default-dataset) |
| Loan Default Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/nikhil1e9/loan-default) |
| Loan Predication | kaggle | [바로가기](https://www.kaggle.com/datasets/ninzaami/loan-predication) |
| Loan Prediction Based on Customer Behavior | kaggle | [바로가기](https://www.kaggle.com/datasets/subhamjain/loan-prediction-based-on-customer-behavior) |
| Loan Prediction Problem Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset) |
| Loan-Approval-Prediction-Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset) |
| Mobile Price Range | kaggle | [바로가기](https://www.kaggle.com/datasets/ybifoundation/mobile-price-range) |
| Netflix Stock Price Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/jainilcoder/netflix-stock-price-prediction) |
| Netflix subscription fee in different countries | kaggle | [바로가기](https://www.kaggle.com/datasets/prasertk/netflix-subscription-price-in-different-countries) |
| New Car Sales in Norway | kaggle | [바로가기](https://www.kaggle.com/datasets/dmi3kno/newcarsalesnorway) |
| New York Stock Exchange | kaggle | [바로가기](https://www.kaggle.com/datasets/dgawlik/nyse) |
| NIFTY-50 Stock Market Data (2000 - 2021) | kaggle | [바로가기](https://www.kaggle.com/datasets/rohanrao/nifty50-stock-market-data) |
| NIFTY-50 Stocks Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/nifty50-stocks-dataset) |
| NSE Stocks Data | kaggle | [바로가기](https://www.kaggle.com/datasets/minatverma/nse-stocks-data) |
| NYC Property Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/new-york-city/nyc-property-sales) |
| Online Business Sales 2017-2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/tylermorse/retail-business-sales-20172019) |
| Online Payment Fraud Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection) |
| Online Payments Fraud Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset) |
| Online Sales Dataset - Popular Marketplace Data | kaggle | [바로가기](https://www.kaggle.com/datasets/shreyanshverma27/online-sales-dataset-popular-marketplace-data) |
| Petrol/Gas Prices Worldwide | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/petrolgas-prices-worldwide) |
| Pharma sales data | kaggle | [바로가기](https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data) |
| Pizza Restaurant Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/shilongzhuang/pizza-sales) |
| Population and Net Migration Dataset World Bank | kaggle | [바로가기](https://www.kaggle.com/datasets/muhammadaammartufail/population-and-net-migration-dataset-world-bank) |
| Predicting Churn for Bank Customers | kaggle | [바로가기](https://www.kaggle.com/datasets/adammaus/predicting-churn-for-bank-customers) |
| Predicting Credit Card Customer Segmentation | kaggle | [바로가기](https://www.kaggle.com/datasets/thedevastator/predicting-credit-card-customer-attrition-with-m) |
| Real estate price prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction) |
| Restaurant Sales report | kaggle | [바로가기](https://www.kaggle.com/datasets/rajatsurana979/fast-food-sales-report) |
| Retail Sales Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset) |
| Retail Transaction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/fahadrehman07/retail-transaction-dataset) |
| S and P 500 stock data | kaggle | [바로가기](https://www.kaggle.com/datasets/camnugent/sandp500) |
| Sales and Satisfaction | kaggle | [바로가기](https://www.kaggle.com/datasets/matinmahmoudi/sales-and-satisfaction) |
| Sales Conversion Optimization | kaggle | [바로가기](https://www.kaggle.com/datasets/loveall/clicks-conversion-tracking) |
| sales dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vinothkannaece/sales-dataset) |
| Sales of summer clothes in E-commerce Wish | kaggle | [바로가기](https://www.kaggle.com/datasets/jmmvutu/summer-products-and-sales-in-ecommerce-wish) |
| Sample Sales Data | kaggle | [바로가기](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data) |
| Sentiment Analysis for Financial News | kaggle | [바로가기](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news) |
| Should This Loan be Approved or Denied? | kaggle | [바로가기](https://www.kaggle.com/datasets/mirbektoktogaraev/should-this-loan-be-approved-or-denied) |
| Sports Car Prices dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rkiattisak/sports-car-prices-dataset) |
| Stock Exchange Data | kaggle | [바로가기](https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data) |
| Stock Market Data (NASDAQ, NYSE, S and P500) | kaggle | [바로가기](https://www.kaggle.com/datasets/paultimothymooney/stock-market-data) |
| Stock Market Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset) |
| Stock Market Dataset (NIFTY-500) | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/nifty500-stocks-dataset) |
| Stock Market India | kaggle | [바로가기](https://www.kaggle.com/datasets/hk7797/stock-market-india) |
| Stock-Market Sentiment Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yash612/stockmarket-sentiment-dataset) |
| Supermarket Sales Data | kaggle | [바로가기](https://www.kaggle.com/datasets/yapwh1208/supermarket-sales-data) |
| Supermarket Sales Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales) |
| Supermarket store branches sales analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/surajjha101/stores-area-and-sales-data) |
| Supermart Grocery Sales - Retail Analytics Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mohamedharris/supermart-grocery-sales-retail-analytics-dataset) |
| Superstore Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/bhanupratapbiswas/superstore-sales) |
| Superstore Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/ishanshrivastava28/superstore-sales) |
| Synthetic data from a financial payment system | kaggle | [바로가기](https://www.kaggle.com/datasets/ealaxi/banksim1) |
| Synthetic Financial Datasets For Fraud Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/ealaxi/paysim1) |
| Tesla share price since it listed | kaggle | [바로가기](https://www.kaggle.com/datasets/surajjha101/tesla-share-price-for-last-5-years) |
| TESLA Stock Data | kaggle | [바로가기](https://www.kaggle.com/datasets/varpit94/tesla-stock-data-updated-till-28jun2021) |
| Tesla stock data from 2010 to 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/timoboz/tesla-stock-data-from-2010-to-2020) |
| Time Series Forecasting with Yahoo Stock Price | kaggle | [바로가기](https://www.kaggle.com/datasets/arashnic/time-series-forecasting-with-yahoo-stock-price) |
| TOP 50 Cryptocurrencies Historical Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/odins0n/top-50-cryptocurrency-historical-prices) |
| Toyota Motors Stock Data (1980-2025) | kaggle | [바로가기](https://www.kaggle.com/datasets/mhassansaboor/toyota-motors-stock-data-2980-2024) |
| Travel Insurance | kaggle | [바로가기](https://www.kaggle.com/datasets/mhdzahier/travel-insurance) |
| Travel Insurance Prediction Data | kaggle | [바로가기](https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data) |
| Turkish Market Sales Dataset With 9.000+Items | kaggle | [바로가기](https://www.kaggle.com/datasets/omercolakoglu/turkish-market-sales-dataset-with-9000items) |
| U.S. Gasoline and Diesel Retail Prices 1995-2021 | kaggle | [바로가기](https://www.kaggle.com/datasets/mruanova/us-gasoline-and-diesel-retail-prices-19952021) |
| Uber and Lyft Cab prices | kaggle | [바로가기](https://www.kaggle.com/datasets/ravi72munde/uber-lyft-cab-prices) |
| US Consumer Finance Complaints | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/us-consumer-finance-complaints) |
| US Funds dataset from Yahoo Finance | kaggle | [바로가기](https://www.kaggle.com/datasets/stefanoleone992/mutual-funds-and-etfs) |
| US historical stock prices with earnings data | kaggle | [바로가기](https://www.kaggle.com/datasets/tsaustin/us-historical-stock-prices-with-earnings-data) |
| US Stocks Fundamentals (XBRL) | kaggle | [바로가기](https://www.kaggle.com/datasets/usfundamentals/us-stocks-fundamentals) |
| Used Car Price Prediction Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset) |
| Used Cars Price Prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/avikasliwal/used-cars-price-prediction) |
| Vehicle Insurance Claim Fraud Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection) |
| Vehicle Insurance Data | kaggle | [바로가기](https://www.kaggle.com/datasets/imtkaggleteam/vehicle-insurance-data) |
| Vehicle Sales Data | kaggle | [바로가기](https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data) |
| Walmart Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/mikhail1681/walmart-sales) |
| Women's Shoe Prices | kaggle | [바로가기](https://www.kaggle.com/datasets/datafiniti/womens-shoes-prices) |
| World Bank: Education Data | kaggle | [바로가기](https://www.kaggle.com/datasets/theworldbank/world-bank-intl-education) |
| World Bank: International Debt Data | kaggle | [바로가기](https://www.kaggle.com/datasets/theworldbank/world-bank-intl-debt) |
| World Stock Prices (Daily Updating) | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/world-stock-prices-daily-updating) |
| XAU/USD Gold Price Historical Data (2004-2026) | kaggle | [바로가기](https://www.kaggle.com/datasets/novandraanugrah/xauusd-gold-price-historical-data-2004-2024) |
| ZARA Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/xontoloyo/data-penjualan-zara) |
| BNG(credit-a,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/124) |
| BNG(credit-g,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/126) |
| credit-approval | openml | [바로가기](https://www.openml.org/d/29) |
| credit-g | openml | [바로가기](https://www.openml.org/d/31) |
| Economic Inequality Explore key inequality indicators from the World Inequality Database and the World Bank | ourworldindata | [바로가기](https://ourworldindata.org/explorers/inequality) |
| Poverty Explore key poverty indicators from World Bank data | ourworldindata | [바로가기](https://ourworldindata.org/explorers/poverty-explorer) |
| Credit Approval | uci | [바로가기](https://archive.ics.uci.edu/dataset/27/credit+approval) |
| Financial Soundness Indicators (FSIs) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_FSI) |
| Financial Soundness Indicators: Reporting entities | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_FSIRE) |
| Government Finance Statistics (GFS), Expense | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_GFSE) |
| Government Finance Statistics (GFS), Financial Assets and Liabilities by Counterpart Sector | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_GFSFALCS) |
| Government Finance Statistics (GFS), Main Aggregates and Balances | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_GFSMAB) |
| Government Finance Statistics (GFS), Statement of Sources and Uses of Cash | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_GFSSSUC) |
| International Financial Statistics (IFS) | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IMF_IFS) |
| World Bank Group Corporate Scorecard | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/WB_CSC) |

### vision (총 195개)

| dataset_name | source | link |
|---|---|---|
| Agriculture Vision | aws_open_data | [바로가기](https://registry.opendata.aws/intelinair_agriculture_vision/) |
| Airborne Object Tracking Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/airborne-object-tracking/) |
| Amazon Bin Image Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/amazon-bin-imagery/) |
| Automated Segmentation of Intracellular Substructures in Electron Microscopy (ASEM) on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/asem-project/) |
| Can Elevation - LiDAR Point Clouds | aws_open_data | [바로가기](https://registry.opendata.aws/canelevation-pointcloud/) |
| Cell Organelle Segmentation in Electron Microscopy (COSEM) on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/janelia-cosem/) |
| Cell Painting Image Collection | aws_open_data | [바로가기](https://registry.opendata.aws/cell-painting-image-collection/) |
| Collection of open nation-scale LiDAR datasets | aws_open_data | [바로가기](https://registry.opendata.aws/open-lidar-data/) |
| Community coral reef image classification training data | aws_open_data | [바로가기](https://registry.opendata.aws/coralreef-image-classification-training/) |
| District of Columbia - Classified Point Cloud LiDAR | aws_open_data | [바로가기](https://registry.opendata.aws/dc-lidar/) |
| Homeland Security and Infrastructure US Cities | aws_open_data | [바로가기](https://registry.opendata.aws/hsip-lidar-us-cities/) |
| ICEYE Synthetic Aperture Radar (SAR) Open Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/iceye-opendata/) |
| IDEAM - Colombian Radar Network | aws_open_data | [바로가기](https://registry.opendata.aws/ideam-radares/) |
| Image classification - fast.ai datasets | aws_open_data | [바로가기](https://registry.opendata.aws/fast-ai-imageclas/) |
| Image localization - fast.ai datasets | aws_open_data | [바로가기](https://registry.opendata.aws/fast-ai-imagelocal/) |
| Indiana Statewide Digital Aerial Imagery Catalog | aws_open_data | [바로가기](https://registry.opendata.aws/in-imagery/) |
| Met Office UK Radar Observations on a 2-year rolling archive | aws_open_data | [바로가기](https://registry.opendata.aws/met-office-uk-radar-observations/) |
| Multiview Extended Video with Activities (MEVA) | aws_open_data | [바로가기](https://registry.opendata.aws/mevadata/) |
| New Jersey Statewide Digital Aerial Imagery Catalog | aws_open_data | [바로가기](https://registry.opendata.aws/nj-imagery/) |
| New Jersey Statewide LiDAR | aws_open_data | [바로가기](https://registry.opendata.aws/nj-lidar/) |
| New Zealand Imagery | aws_open_data | [바로가기](https://registry.opendata.aws/nz-imagery/) |
| Ohio State Cardiac MRI Raw Data (OCMR) | aws_open_data | [바로가기](https://registry.opendata.aws/ocmr_data/) |
| Prefeitura Municipal de Sao Paulo (PMSP) LiDAR Point Cloud | aws_open_data | [바로가기](https://registry.opendata.aws/pmsp-lidar/) |
| RSNA Abdominal Trauma Detection (RSNA-ABT) | aws_open_data | [바로가기](https://registry.opendata.aws/rsna-abdominal-trauma-detection/) |
| RSNA Cervical Spine Fracture Detection (RSNA-CSF) Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/rsna-cervical-spine-fracture-detection/) |
| RSNA Intracranial Aneurysm Detection Dataset (RSNA-ICA) | aws_open_data | [바로가기](https://registry.opendata.aws/rsna-intracranial-aneurysm-detection-dataset/) |
| RSNA Intracranial Hemorrhage Detection | aws_open_data | [바로가기](https://registry.opendata.aws/rsna-intracranial-hemorrhage-detection/) |
| RSNA Pulmonary Embolism Detection | aws_open_data | [바로가기](https://registry.opendata.aws/rsna-pulmonary-embolism-detection/) |
| Scottish Public Sector LiDAR Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/scottish-lidar/) |
| Sophos/Reversing Labs 20 Million malware detection dataset | aws_open_data | [바로가기](https://registry.opendata.aws/sorel-20m/) |
| State of Colorado Imagery | aws_open_data | [바로가기](https://registry.opendata.aws/colorado-imagery/) |
| The Massively Multilingual Image Dataset (MMID) | aws_open_data | [바로가기](https://registry.opendata.aws/mmid/) |
| Umbra Synthetic Aperture Radar (SAR) Open Data | aws_open_data | [바로가기](https://registry.opendata.aws/umbra-open-data/) |
| USGS 3DEP LiDAR Point Clouds | aws_open_data | [바로가기](https://registry.opendata.aws/usgs-lidar/) |
| Visual Anomaly (VisA) | aws_open_data | [바로가기](https://registry.opendata.aws/visa/) |
| Yale-CMU-Berkeley (YCB) Object and Model Set | aws_open_data | [바로가기](https://registry.opendata.aws/ycb-benchmarks/) |
| 100 Sports Image Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/gpiosenka/sports-classification) |
| 140k Real and Fake Faces | kaggle | [바로가기](https://www.kaggle.com/datasets/xhlulu/140k-real-and-fake-faces) |
| 200 Bird Species with 11,788 Images | kaggle | [바로가기](https://www.kaggle.com/datasets/veeralakrishna/200-bird-species-with-11788-images) |
| 300 images of squares, circles, and triangles | kaggle | [바로가기](https://www.kaggle.com/datasets/cactus3/basicshapes) |
| 3D MNIST | kaggle | [바로가기](https://www.kaggle.com/datasets/daavoo/3d-mnist) |
| 5 Celebrity Faces Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/dansbecker/5-celebrity-faces-dataset) |
| 60,000+ Images of Cars | kaggle | [바로가기](https://www.kaggle.com/datasets/prondeau/the-car-connection-picture-dataset) |
| A-Z Handwritten Alphabets in.csv format | kaggle | [바로가기](https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format) |
| Aerial Semantic Segmentation Drone Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/bulentsiyah/semantic-drone-dataset) |
| AGE, GENDER AND ETHNICITY (FACE DATA) CSV | kaggle | [바로가기](https://www.kaggle.com/datasets/nipunarora8/age-gender-and-ethnicity-face-data-csv) |
| Animal Crossing: New Horizons | kaggle | [바로가기](https://www.kaggle.com/datasets/prasertk/animal-crossing-new-horizons-with-image-url) |
| Animal Faces | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/animal-faces) |
| Animal Image Dataset (90 Different Animals) | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/animal-image-dataset-90-different-animals) |
| Animal Image Dataset(DOG, CAT and PANDA) | kaggle | [바로가기](https://www.kaggle.com/datasets/ashishsaxena2209/animal-image-datasetdog-cat-and-panda) |
| Animals Detection Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset) |
| Anime Face Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/splcher/animefacedataset) |
| Anime Faces | kaggle | [바로가기](https://www.kaggle.com/datasets/soumikrakshit/anime-faces) |
| Arabic Handwritten Characters Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mloey1/ahcd1) |
| Arabic Handwritten Digits Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mloey1/ahdd1) |
| Art Images: Drawing/Painting/Sculptures/Engravings | kaggle | [바로가기](https://www.kaggle.com/datasets/thedownhill/art-images-drawings-painting-sculpture-engraving) |
| Arthropod Taxonomy Orders Object Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mistag/arthropod-taxonomy-orders-object-detection-dataset) |
| AT and T Database of Faces | kaggle | [바로가기](https://www.kaggle.com/datasets/kasikrit/att-database-of-faces) |
| Blood Cell Images | kaggle | [바로가기](https://www.kaggle.com/datasets/paultimothymooney/blood-cells) |
| Bone Fracture Detection: Computer Vision Project | kaggle | [바로가기](https://www.kaggle.com/datasets/pkdarabi/bone-fracture-detection-computer-vision-project) |
| Breast Histopathology Images | kaggle | [바로가기](https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images) |
| Breast Ultrasound Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset) |
| Butterfly and Moths Image Classification 100 species | kaggle | [바로가기](https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species) |
| Butterfly Image Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification) |
| Caltech 256 Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jessicali9530/caltech256) |
| CAPTCHA Images | kaggle | [바로가기](https://www.kaggle.com/datasets/fournierp/captcha-version-2-images) |
| Car License Plate Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection) |
| Car Object Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/sshikamaru/car-object-detection) |
| Cards Image Dataset-Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification) |
| casting product image data for quality inspection | kaggle | [바로가기](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product) |
| Cats and Dogs image classification | kaggle | [바로가기](https://www.kaggle.com/datasets/samuelcortinhas/cats-and-dogs-image-classification) |
| Cattle Weight Detection Model + Dataset (12k) | kaggle | [바로가기](https://www.kaggle.com/datasets/sadhliroomyprime/cattle-weight-detection-model-dataset-12k) |
| Celeb Faces Attributes (CelebA) Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jessicali9530/celeba-dataset) |
| Chest CT-Scan images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images) |
| Chest X-ray Images | kaggle | [바로가기](https://www.kaggle.com/datasets/tolgadincer/labeled-chest-xray-images) |
| Chest X-Ray Images (Pneumonia) | kaggle | [바로가기](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) |
| Chest Xray Masks and Labels | kaggle | [바로가기](https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels) |
| Chinese MNIST | kaggle | [바로가기](https://www.kaggle.com/datasets/gpreda/chinese-mnist) |
| Cityscapes Image Pairs | kaggle | [바로가기](https://www.kaggle.com/datasets/dansbecker/cityscapes-image-pairs) |
| CNC Mill Tool Wear | kaggle | [바로가기](https://www.kaggle.com/datasets/shasun/tool-wear-detection-in-cnc-mill) |
| Colorectal Histology MNIST | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/colorectal-histology-mnist) |
| Construction Site Safety Image Dataset Roboflow | kaggle | [바로가기](https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow) |
| Corona Hack -Chest X-Ray-Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/praveengovi/coronahack-chest-xraydataset) |
| Customer Segmentation | kaggle | [바로가기](https://www.kaggle.com/datasets/vetrirah/customer) |
| Customer Segmentation Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/kaushiksuresh147/customer-segmentation) |
| Customer Segmentation Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/yasserh/customer-segmentation-dataset) |
| Cybersecurity Intrusion Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/dnkumars/cybersecurity-intrusion-detection-dataset) |
| deepfake and real images | kaggle | [바로가기](https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images) |
| Dogs and Cats Images | kaggle | [바로가기](https://www.kaggle.com/datasets/chetankv/dogs-cats-images) |
| Doom or Animal Crossing? (Image Classification) | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/doom-crossing) |
| Electrical Fault detection and classification | kaggle | [바로가기](https://www.kaggle.com/datasets/esathyaprakash/electrical-fault-detection-and-classification) |
| EMNIST (Extended MNIST) | kaggle | [바로가기](https://www.kaggle.com/datasets/crawford/emnist) |
| Emotion Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer) |
| English Handwritten Characters | kaggle | [바로가기](https://www.kaggle.com/datasets/dhruvildave/english-handwritten-characters-dataset) |
| Face Detection in Images | kaggle | [바로가기](https://www.kaggle.com/datasets/dataturks/face-detection-in-images) |
| Face expression recognition dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset) |
| Face Images with Marked Landmark Points | kaggle | [바로가기](https://www.kaggle.com/datasets/drgilermo/face-images-with-marked-landmark-points) |
| Face Mask Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection) |
| Face Mask Detection 12K Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ashishjangra27/face-mask-12k-images-dataset) |
| Face Mask Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/omkargurav/face-mask-dataset) |
| Face Mask Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/wobotintelligence/face-mask-detection-dataset) |
| Face Mask Lite Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/prasoonkottarathil/face-mask-lite-dataset) |
| Faces: Age Detection from Images | kaggle | [바로가기](https://www.kaggle.com/datasets/arashnic/faces-age-detection-dataset) |
| Facial Emotion Recognition Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tapakah68/facial-emotion-recognition) |
| Fashion MNIST | kaggle | [바로가기](https://www.kaggle.com/datasets/zalando-research/fashionmnist) |
| Fashion Product Images (Small) | kaggle | [바로가기](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small) |
| Fashion Product Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset) |
| Flickr Image dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset) |
| Flickr-Faces-HQ Dataset (FFHQ) | kaggle | [바로가기](https://www.kaggle.com/datasets/arnaud58/flickrfaceshq-dataset-ffhq) |
| Flower Color Images | kaggle | [바로가기](https://www.kaggle.com/datasets/olgabelitskaya/flower-color-images) |
| Food Images (Food-101) | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/food41) |
| Fruit Images for Object Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/mbkinaci/fruit-images-for-object-detection) |
| Fruits and Vegetables Image Recognition Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition) |
| Glaucoma Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/sshikamaru/glaucoma-detection) |
| Grapevine Leaves Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/grapevine-leaves-image-dataset) |
| HaGRID - HAnd Gesture Recognition Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kapitanov/hagrid) |
| Handwritten math symbols dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols) |
| handwritten signatures | kaggle | [바로가기](https://www.kaggle.com/datasets/divyanshrai/handwritten-signatures) |
| Helmet Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/helmet-detection) |
| Human Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset) |
| Human Faces | kaggle | [바로가기](https://www.kaggle.com/datasets/ashwingupta3012/human-faces) |
| Image Colorization | kaggle | [바로가기](https://www.kaggle.com/datasets/shravankumar9892/image-colorization) |
| Image Net 1000 (mini) | kaggle | [바로가기](https://www.kaggle.com/datasets/ifigotin/imagenetmini-1000) |
| Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/pavansanagapati/images-dataset) |
| Images of LEGO Bricks | kaggle | [바로가기](https://www.kaggle.com/datasets/joosthazelzet/lego-brick-images) |
| Indian Food Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/indian-food-images-dataset) |
| Intel Image Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/puneet6060/intel-image-classification) |
| Kuzushiji-MNIST | kaggle | [바로가기](https://www.kaggle.com/datasets/anokas/kuzushiji) |
| Labelled Faces in the Wild (LFW) Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset) |
| LFW - People (Face Recognition) | kaggle | [바로가기](https://www.kaggle.com/datasets/atulanandjha/lfwpeople) |
| Liver Tumor Segmentation | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/liver-tumor-segmentation) |
| Malaria Cell Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria) |
| Mall Customer Segmentation Data | kaggle | [바로가기](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) |
| Military Aircraft Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/a2015003713/militaryaircraftdetectiondataset) |
| MNIST as.jpg | kaggle | [바로가기](https://www.kaggle.com/datasets/scolianni/mnistasjpg) |
| MNIST Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/hojjatk/mnist-dataset) |
| MNIST in CSV | kaggle | [바로가기](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv) |
| Movies on Netflix, Prime Video, Hulu and Disney+ | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/movies-on-netflix-prime-video-hulu-and-disney) |
| MRI and Alzheimers | kaggle | [바로가기](https://www.kaggle.com/datasets/jboysen/mri-and-alzheimers) |
| Natural Images | kaggle | [바로가기](https://www.kaggle.com/datasets/prasunroy/natural-images) |
| Network Intrusion Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection) |
| NumtaDB: Bengali Handwritten Digits | kaggle | [바로가기](https://www.kaggle.com/datasets/BengaliAI/numta) |
| Open Images | kaggle | [바로가기](https://www.kaggle.com/datasets/bigquery/open-images) |
| Pet's Facial Expression Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/anshtanwar/pets-facial-expression-dataset) |
| Pistachio Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/pistachio-image-dataset) |
| Pokemon Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types) |
| Pokemon Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kvpratama/pokemon-images-dataset) |
| Popular Video Games 1980 - 2023 | kaggle | [바로가기](https://www.kaggle.com/datasets/arnabchaki/popular-video-games-1980-2023) |
| Pothole Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/atulyakumar98/pothole-detection-dataset) |
| Pulmonary Chest X-Ray Abnormalities | kaggle | [바로가기](https://www.kaggle.com/datasets/kmader/pulmonary-chest-xray-abnormalities) |
| Random Sample of NIH Chest X-ray Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/nih-chest-xrays/sample) |
| Real and Fake Face Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/ciplab/real-and-fake-face-detection) |
| Retinal OCT Images (optical coherence tomography) | kaggle | [바로가기](https://www.kaggle.com/datasets/paultimothymooney/kermany2018) |
| Rice Diseases Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/minhhuy2810/rice-diseases-image-dataset) |
| Rice Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset) |
| Road Sign Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/road-sign-detection) |
| Road Vehicle Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ashfakyeafi/road-vehicle-images-dataset) |
| Rock-Paper-Scissors Images | kaggle | [바로가기](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors) |
| RSNA Mammo PNGs 256px, 384px, 512px, 768px, 1024px | kaggle | [바로가기](https://www.kaggle.com/datasets/radek1/rsna-mammography-images-as-pngs) |
| Safety Helmet Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection) |
| SARS-COV-2 Ct-Scan Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/plameneduardo/sarscov2-ctscan-dataset) |
| Semantic segmentation of aerial imagery | kaggle | [바로가기](https://www.kaggle.com/datasets/humansintheloop/semantic-segmentation-of-aerial-imagery) |
| Shoe vs Sandal vs Boot Image Dataset (15K Images) | kaggle | [바로가기](https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images) |
| SIIM ACR Pneumothorax Segmentation Data | kaggle | [바로가기](https://www.kaggle.com/datasets/jesperdramsch/siim-acr-pneumothorax-segmentation-data) |
| Skin diseases image dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ismailpromus/skin-diseases-image-dataset) |
| Smoke Detection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/deepcontractor/smoke-detection-dataset) |
| Steam Video Games | kaggle | [바로가기](https://www.kaggle.com/datasets/tamber/steam-video-games) |
| STL-10 Image Recognition Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jessicali9530/stl10) |
| Suicide and Depression Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch) |
| Surface Crack Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/arunrk7/surface-crack-detection) |
| The Bee Image Dataset: Annotated Honey Bee Images | kaggle | [바로가기](https://www.kaggle.com/datasets/jenny18/honey-bee-annotated-images) |
| timm (Py Torch Image Models) | kaggle | [바로가기](https://www.kaggle.com/datasets/kozodoi/timm-pytorch-image-models) |
| Tiny Image Net | kaggle | [바로가기](https://www.kaggle.com/datasets/akash2sharma/tiny-imagenet) |
| Top Video Games 1995-2021 Metacritic | kaggle | [바로가기](https://www.kaggle.com/datasets/deepcontractor/top-video-games-19952021-metacritic) |
| Traffic Detection Project | kaggle | [바로가기](https://www.kaggle.com/datasets/yusufberksardoan/traffic-detection-project) |
| Traffic Signs Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/pkdarabi/cardetection) |
| Trending You Tube Video Statistics | kaggle | [바로가기](https://www.kaggle.com/datasets/datasnaek/youtube-new) |
| Trending You Tube Video Statistics and Comments | kaggle | [바로가기](https://www.kaggle.com/datasets/datasnaek/youtube) |
| Trending Youtube Video Statistics (113 Countries) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/trending-youtube-videos-113-countries) |
| Tuberculosis (TB) Chest X-ray Database | kaggle | [바로가기](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset) |
| Tufts Face Database | kaggle | [바로가기](https://www.kaggle.com/datasets/kpvisionlab/tufts-face-database) |
| TV shows on Netflix, Prime Video, Hulu and Disney+ | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/tv-shows-on-netflix-prime-video-hulu-and-disney) |
| Vegetable Image Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) |
| Vehicle Detection Image Set | kaggle | [바로가기](https://www.kaggle.com/datasets/brsdincer/vehicle-detection-image-set) |
| Vehicle Number Plate Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/dataturks/vehicle-number-plate-detection) |
| Video Game Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/anandshaw2001/video-game-sales) |
| Video Game Sales | kaggle | [바로가기](https://www.kaggle.com/datasets/gregorut/videogamesales) |
| Video Game Sales 2024 | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/video-game-sales-2024) |
| Video Game Sales with Ratings | kaggle | [바로가기](https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings) |
| Video Games Sales 2019 | kaggle | [바로가기](https://www.kaggle.com/datasets/ashaheedq/video-games-sales-2019) |
| Video Games Sales Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sidtwr/videogames-sales-dataset) |
| Wiki-Art: Visual Art Encyclopedia | kaggle | [바로가기](https://www.kaggle.com/datasets/ipythonx/wikiart-gangogh-creating-art-gan) |
| Yoga Pose Image classification dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/shrutisaxena/yoga-pose-image-classification-dataset) |
| You Tube Faces With Facial Keypoints | kaggle | [바로가기](https://www.kaggle.com/datasets/selfishgene/youtube-faces-with-facial-keypoints) |
| You Tube Trending Video Dataset (updated daily) | kaggle | [바로가기](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset) |

### ml (총 163개)

| dataset_name | source | link |
|---|---|---|
| CMS 2008-2010 Data Entrepreneurs' Synthetic Public Use File (DE-SynPUF) in OMOP Common Data Model | aws_open_data | [바로가기](https://registry.opendata.aws/cmsdesynpuf-omop/) |
| Gretel Synthetic Safety Alignment Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/gretel-synthetic-safety-alignment-en-v1/) |
| Phrase Clustering Dataset (PCD) | aws_open_data | [바로가기](https://registry.opendata.aws/pcd/) |
| RSNA Lumbar Spine Degenerative Classification Dataset (RSNA-LSDD) | aws_open_data | [바로가기](https://registry.opendata.aws/rsna-lumbar-spine-degenerative-classification-dataset/) |
| AAAMLP | kaggle | [바로가기](https://www.kaggle.com/datasets/abhishek/aaamlp) |
| Anime Recommendation Database 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020) |
| BI intro to data cleaning eda and machine learning | kaggle | [바로가기](https://www.kaggle.com/datasets/walekhwatlphilip/intro-to-data-cleaning-eda-and-machine-learning) |
| Book Recommendation (Good book api) | kaggle | [바로가기](https://www.kaggle.com/datasets/imtkaggleteam/book-recommendation-good-book-api) |
| Book Recommendation Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) |
| Boston House Prices-Advanced Regression Techniques | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/the-boston-houseprice-data) |
| Bottles Synthetic Images | kaggle | [바로가기](https://www.kaggle.com/datasets/vencerlanz09/bottle-synthetic-images-dataset) |
| Car Price Prediction Multiple Linear Regression | kaggle | [바로가기](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction) |
| Car vs Bike Classification Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/utkarshsaxenadn/car-vs-bike-classification-dataset) |
| Cat and Dog images for Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/ashfakyeafi/cat-dog-images-for-classification) |
| Cats and Dogs Breeds Classification Oxford Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/zippyz/cats-and-dogs-breeds-classification-oxford-dataset) |
| Cats and Dogs Classification Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset) |
| CIFAKE: Real and AI-Generated Synthetic Images | kaggle | [바로가기](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images) |
| Classification of Handwritten Letters | kaggle | [바로가기](https://www.kaggle.com/datasets/olgabelitskaya/classification-of-handwritten-letters) |
| Clothing Fit Dataset for Size Recommendation | kaggle | [바로가기](https://www.kaggle.com/datasets/rmisra/clothing-fit-dataset-for-size-recommendation) |
| Cooperative Patent Classification Codes Meaning | kaggle | [바로가기](https://www.kaggle.com/datasets/xhlulu/cpc-codes) |
| Cyberbullying Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification) |
| Dermatology Dataset (Multi-class classification) | kaggle | [바로가기](https://www.kaggle.com/datasets/olcaybolat1/dermatology-dataset-classification) |
| Drug Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/prathamtripathi/drug-classification) |
| Environmental Sound Classification 50 | kaggle | [바로가기](https://www.kaggle.com/datasets/mmoreaux/environmental-sound-classification-50) |
| eye_diseases_classification | kaggle | [바로가기](https://www.kaggle.com/datasets/gunavenkatdoddi/eye-diseases-classification) |
| Fruit Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/sshikamaru/fruit-recognition) |
| Fruit classification(10 Class) | kaggle | [바로가기](https://www.kaggle.com/datasets/karimabdulnabi/fruit-classification10-class) |
| Fruits fresh and rotten for classification | kaggle | [바로가기](https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification) |
| Garbage Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification) |
| Garbage Classification (12 classes) | kaggle | [바로가기](https://www.kaggle.com/datasets/mostafaabla/garbage-classification) |
| Garbage Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/sumn2u/garbage-classification-v2) |
| Genre Classification Dataset IMDb | kaggle | [바로가기](https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb) |
| Glass Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/glass) |
| GTZAN Dataset - Music Genre Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification) |
| Hotel Reservations Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset) |
| LEGO Minifigures | kaggle | [바로가기](https://www.kaggle.com/datasets/ihelon/lego-minifigures-classification) |
| Leukemia Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/leukemia-classification) |
| Linear Regression | kaggle | [바로가기](https://www.kaggle.com/datasets/andonians/random-linear-regression) |
| Linear Regression Data-set | kaggle | [바로가기](https://www.kaggle.com/datasets/tanuprabhu/linear-regression-dataset) |
| Linear Regression E-commerce Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/kolawale/focusing-on-mobile-app-or-website) |
| Logistic Regression | kaggle | [바로가기](https://www.kaggle.com/datasets/dragonheir/logistic-regression) |
| Machine Learning Job Postings in the US | kaggle | [바로가기](https://www.kaggle.com/datasets/ivankmk/thousand-ml-jobs-in-usa) |
| Machine Predictive Maintenance Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification) |
| Men/Women Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/playlist/men-women-classification) |
| Microsoft Azure Predictive Maintenance | kaggle | [바로가기](https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance) |
| Mobile Price Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification) |
| Movie Recommendation System | kaggle | [바로가기](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system) |
| Mushroom Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/mushroom-classification) |
| Mushrooms classification - Common genus's images | kaggle | [바로가기](https://www.kaggle.com/datasets/maysee/mushrooms-classification-common-genuss-images) |
| Online Retail II UCI | kaggle | [바로가기](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) |
| Pharmaceutical Drugs and Vitamins Synthetic Images | kaggle | [바로가기](https://www.kaggle.com/datasets/vencerlanz09/pharmaceutical-drugs-and-vitamins-synthetic-images) |
| Phishing Dataset for Machine Learning | kaggle | [바로가기](https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning) |
| Pokemon for Data Mining and Machine Learning | kaggle | [바로가기](https://www.kaggle.com/datasets/alopez247/pokemon) |
| Predictive Maintenance Dataset (AI4I 2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020) |
| Recyclable and Household Waste Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification) |
| Retailrocket recommender system dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset) |
| Revisiting a Concrete Strength regression | kaggle | [바로가기](https://www.kaggle.com/datasets/maajdl/yeh-concret-data) |
| Salary data - Simple linear regression | kaggle | [바로가기](https://www.kaggle.com/datasets/karthickveerakumar/salary-data-simple-linear-regression) |
| Salary Dataset - Simple linear regression | kaggle | [바로가기](https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression) |
| Skin Lesion Images for Melanoma Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/isic-2019) |
| Spotify Recommendation | kaggle | [바로가기](https://www.kaggle.com/datasets/bricevergnou/spotify-recommendation) |
| Stellar Classification Dataset - SDSS17 | kaggle | [바로가기](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17) |
| Waste Classification data | kaggle | [바로가기](https://www.kaggle.com/datasets/techsash/waste-classification-data) |
| Wine Dataset for Clustering | kaggle | [바로가기](https://www.kaggle.com/datasets/harrywang/wine-dataset-for-clustering) |
| Zoo Animal Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/zoo-animal-classification) |
| anneal | openml | [바로가기](https://www.openml.org/d/2) |
| arrhythmia | openml | [바로가기](https://www.openml.org/d/5) |
| audiology | openml | [바로가기](https://www.openml.org/d/7) |
| autos | openml | [바로가기](https://www.openml.org/d/9) |
| balance-scale | openml | [바로가기](https://www.openml.org/d/11) |
| BNG(anneal,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/70) |
| BNG(anneal.ORIG,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/71) |
| BNG(autos,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/75) |
| BNG(bridges_version1,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/116) |
| BNG(bridges_version2,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/117) |
| BNG(cmc,nominal,55296) | openml | [바로가기](https://www.openml.org/d/119) |
| BNG(colic,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/122) |
| BNG(colic.ORIG,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/121) |
| BNG(cylinder-bands,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/128) |
| BNG(dermatology,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/129) |
| BNG(glass,nominal,137781) | openml | [바로가기](https://www.openml.org/d/133) |
| BNG(hepatitis,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/142) |
| BNG(hypothyroid,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/144) |
| BNG(ionosphere) | openml | [바로가기](https://www.openml.org/d/146) |
| BNG(kr-vs-kp) | openml | [바로가기](https://www.openml.org/d/72) |
| BNG(letter,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/74) |
| BNG(lymph,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/76) |
| BNG(mfeat-fourier,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/78) |
| BNG(mfeat-karhunen,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/115) |
| BNG(mfeat-zernike,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/118) |
| BNG(mushroom) | openml | [바로가기](https://www.openml.org/d/120) |
| BNG(optdigits) | openml | [바로가기](https://www.openml.org/d/123) |
| BNG(page-blocks,nominal,295245) | openml | [바로가기](https://www.openml.org/d/125) |
| BNG(pendigits,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/127) |
| BNG(segment) | openml | [바로가기](https://www.openml.org/d/130) |
| BNG(sick,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/131) |
| BNG(sonar,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/132) |
| BNG(soybean) | openml | [바로가기](https://www.openml.org/d/134) |
| BNG(spambase) | openml | [바로가기](https://www.openml.org/d/135) |
| BNG(tic-tac-toe) | openml | [바로가기](https://www.openml.org/d/137) |
| BNG(trains) | openml | [바로가기](https://www.openml.org/d/139) |
| BNG(vehicle,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/141) |
| BNG(vote) | openml | [바로가기](https://www.openml.org/d/143) |
| BNG(waveform-5000,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/147) |
| BNG(zoo,nominal,1000000) | openml | [바로가기](https://www.openml.org/d/148) |
| breast-w | openml | [바로가기](https://www.openml.org/d/15) |
| cmc | openml | [바로가기](https://www.openml.org/d/23) |
| colic | openml | [바로가기](https://www.openml.org/d/25) |
| colic | openml | [바로가기](https://www.openml.org/d/27) |
| Cov Pok Elec | openml | [바로가기](https://www.openml.org/d/149) |
| covertype | openml | [바로가기](https://www.openml.org/d/150) |
| dermatology | openml | [바로가기](https://www.openml.org/d/35) |
| ecoli | openml | [바로가기](https://www.openml.org/d/39) |
| electricity | openml | [바로가기](https://www.openml.org/d/151) |
| glass | openml | [바로가기](https://www.openml.org/d/41) |
| haberman | openml | [바로가기](https://www.openml.org/d/43) |
| hepatitis | openml | [바로가기](https://www.openml.org/d/55) |
| Hyperplane_10_1E-3 | openml | [바로가기](https://www.openml.org/d/152) |
| hypothyroid | openml | [바로가기](https://www.openml.org/d/57) |
| ionosphere | openml | [바로가기](https://www.openml.org/d/59) |
| iris | openml | [바로가기](https://www.openml.org/d/61) |
| kr-vs-kp | openml | [바로가기](https://www.openml.org/d/3) |
| letter | openml | [바로가기](https://www.openml.org/d/6) |
| liver-disorders | openml | [바로가기](https://www.openml.org/d/8) |
| lymph | openml | [바로가기](https://www.openml.org/d/10) |
| mfeat-factors | openml | [바로가기](https://www.openml.org/d/12) |
| mfeat-fourier | openml | [바로가기](https://www.openml.org/d/14) |
| mfeat-karhunen | openml | [바로가기](https://www.openml.org/d/16) |
| mfeat-morphological | openml | [바로가기](https://www.openml.org/d/18) |
| mfeat-pixel | openml | [바로가기](https://www.openml.org/d/20) |
| mfeat-zernike | openml | [바로가기](https://www.openml.org/d/22) |
| mushroom | openml | [바로가기](https://www.openml.org/d/24) |
| nursery | openml | [바로가기](https://www.openml.org/d/26) |
| optdigits | openml | [바로가기](https://www.openml.org/d/28) |
| page-blocks | openml | [바로가기](https://www.openml.org/d/30) |
| pendigits | openml | [바로가기](https://www.openml.org/d/32) |
| segment | openml | [바로가기](https://www.openml.org/d/36) |
| sick | openml | [바로가기](https://www.openml.org/d/38) |
| sonar | openml | [바로가기](https://www.openml.org/d/40) |
| soybean | openml | [바로가기](https://www.openml.org/d/42) |
| spambase | openml | [바로가기](https://www.openml.org/d/44) |
| splice | openml | [바로가기](https://www.openml.org/d/46) |
| tae | openml | [바로가기](https://www.openml.org/d/48) |
| tic-tac-toe | openml | [바로가기](https://www.openml.org/d/50) |
| trains | openml | [바로가기](https://www.openml.org/d/52) |
| vehicle | openml | [바로가기](https://www.openml.org/d/54) |
| vote | openml | [바로가기](https://www.openml.org/d/56) |
| waveform-5000 | openml | [바로가기](https://www.openml.org/d/60) |
| zoo | openml | [바로가기](https://www.openml.org/d/62) |
| AI4I 2020 Predictive Maintenance Dataset | uci | [바로가기](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) |
| Concrete Compressive Strength | uci | [바로가기](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) |
| Dry Bean | uci | [바로가기](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset) |
| Electricity Load Diagrams20112014 | uci | [바로가기](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014) |
| Online Shoppers Purchasing Intention Dataset | uci | [바로가기](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) |
| Optical Recognition of Handwritten Digits | uci | [바로가기](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits) |
| Parkinsons | uci | [바로가기](https://archive.ics.uci.edu/dataset/174/parkinsons) |
| Phishing Websites | uci | [바로가기](https://archive.ics.uci.edu/dataset/327/phishing+websites) |
| Real Estate Valuation | uci | [바로가기](https://archive.ics.uci.edu/dataset/477/real+estate+valuation+data+set) |
| Seeds | uci | [바로가기](https://archive.ics.uci.edu/dataset/236/seeds) |
| Seoul Bike Sharing Demand | uci | [바로가기](https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand) |
| Spambase | uci | [바로가기](https://archive.ics.uci.edu/dataset/94/spambase) |
| Wholesale customers | uci | [바로가기](https://archive.ics.uci.edu/dataset/292/wholesale+customers) |
| Integrated Food Security Phase Classification | worldbank | [바로가기](https://data360.worldbank.org/en/dataset/IPC_IPC) |

### text (총 126개)

| dataset_name | source | link |
|---|---|---|
| Aristo Mini Corpus | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-aristo-mini/) |
| Automatic Speech Recognition (ASR) Error Robustness | aws_open_data | [바로가기](https://registry.opendata.aws/asr-error-robustness/) |
| Enriched Topical-Chat Dataset for Knowledge-Grounded Dialogue Systems | aws_open_data | [바로가기](https://registry.opendata.aws/topical-chat-enriched/) |
| Global Database of Events, Language and Tone (GDELT) | aws_open_data | [바로가기](https://registry.opendata.aws/gdelt/) |
| Humor Detection from Product Question Answering Systems | aws_open_data | [바로가기](https://registry.opendata.aws/humor-detection/) |
| Learning to Rank and Filter - community question answering | aws_open_data | [바로가기](https://registry.opendata.aws/ltrf-cqa-dataset/) |
| NLP - fast.ai datasets | aws_open_data | [바로가기](https://registry.opendata.aws/fast-ai-nlp/) |
| Sudachi Language Resources | aws_open_data | [바로가기](https://registry.opendata.aws/sudachi/) |
| Textbook Question Answering (TQA) | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-tqa/) |
| Variant Effect Predictor (VEP) and the Loss-Of-Function Transcript Effect Estimator (LOFTEE) Plugin | aws_open_data | [바로가기](https://registry.opendata.aws/hail-vep-pipeline/) |
| Wiki Sum: Coherent Summarization Dataset for Efficient Human-Evaluation | aws_open_data | [바로가기](https://registry.opendata.aws/wikisum/) |
| forecast-review | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/forecast-review) |
| trump-news | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/trump-news) |
| twitter-ratio | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/twitter-ratio) |
| (Sunset) Ukraine Conflict Twitter Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/bwandowando/ukraine-russian-crisis-twitter-dataset-1-2-m-rows) |
| 18,393 Pitchfork Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/nolanbconaway/pitchfork-data) |
| 20 Newsgroups | kaggle | [바로가기](https://www.kaggle.com/datasets/crawford/20-newsgroups) |
| 515K Hotel Reviews Data in Europe | kaggle | [바로가기](https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe) |
| 6.5k train examples for LLM Science Exam | kaggle | [바로가기](https://www.kaggle.com/datasets/radek1/additional-train-data-for-llm-science-exam) |
| 60k Stack Overflow Questions with Quality Rating | kaggle | [바로가기](https://www.kaggle.com/datasets/imoore/60k-stack-overflow-questions-with-quality-rate) |
| A Million News Headlines | kaggle | [바로가기](https://www.kaggle.com/datasets/therohk/million-headlines) |
| AI Vs Human Text | kaggle | [바로가기](https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text) |
| All Trump's Twitter insults (2015-2021) | kaggle | [바로가기](https://www.kaggle.com/datasets/ayushggarg/all-trumps-twitter-insults-20152021) |
| Amazon Alexa Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/sid321axn/amazon-alexa-reviews) |
| Amazon Books Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews) |
| Amazon Cell Phones Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/grikomsn/amazon-cell-phones-reviews) |
| Amazon Fine Food Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) |
| Amazon Musical Instruments Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/eswarchandt/amazon-music-reviews) |
| Amazon Product Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/saurav9786/amazon-product-reviews) |
| Amazon reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/kritanjalijain/amazon-reviews) |
| Amazon Reviews for Sentiment Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews) |
| Amazon reviews: Kindle Store Category | kaggle | [바로가기](https://www.kaggle.com/datasets/bharadwaj6/kindle-reviews) |
| Amazon Reviews: Unlocked Mobile Phones | kaggle | [바로가기](https://www.kaggle.com/datasets/PromptCloudHQ/amazon-reviews-unlocked-mobile-phones) |
| American Sign Language Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ayuraj/asl-dataset) |
| Animal Crossing Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/jessemostipak/animal-crossing) |
| Anime Dataset with Reviews - My Anime List | kaggle | [바로가기](https://www.kaggle.com/datasets/marlesson/myanimelist-dataset-animes-profiles-reviews) |
| Annotated Corpus for Named Entity Recognition | kaggle | [바로가기](https://www.kaggle.com/datasets/abhinavwalia95/entity-annotated-corpus) |
| BBC News Summary | kaggle | [바로가기](https://www.kaggle.com/datasets/pariza/bbc-news-summary) |
| Beer Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/rdoume/beerreviews) |
| Bible Corpus | kaggle | [바로가기](https://www.kaggle.com/datasets/oswinrh/bible) |
| Blog Authorship Corpus | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/blog-authorship-corpus) |
| Board Game Geek Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews) |
| Book-Crossing: User review ratings | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset) |
| CNN-Daily Mail News Text Summarization | kaggle | [바로가기](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail) |
| Customer Support on Twitter | kaggle | [바로가기](https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter) |
| Deep-NLP | kaggle | [바로가기](https://www.kaggle.com/datasets/samdeeplearning/deepnlp) |
| Disneyland Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/arushchillar/disneyland-reviews) |
| Douban Movie Short Comments Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/utmhikari/doubanmovieshortcomments) |
| Email Spam Classification Dataset CSV | kaggle | [바로가기](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) |
| Emoji sentiment | kaggle | [바로가기](https://www.kaggle.com/datasets/harriken/emoji-sentiment) |
| Emotion Detection from Text | kaggle | [바로가기](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text) |
| Emotions dataset for NLP | kaggle | [바로가기](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp) |
| Fake News Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification) |
| Fake News Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/bhavikjikadara/fake-news-detection) |
| Fake News detection | kaggle | [바로가기](https://www.kaggle.com/datasets/jruvika/fake-news-detection) |
| Fake News Detection Datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets) |
| fake-and-real-news-dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) |
| Fast Text Crawl 300d 2M | kaggle | [바로가기](https://www.kaggle.com/datasets/yekenot/fasttext-crawl-300d-2m) |
| First GOP Debate Twitter Sentiment | kaggle | [바로가기](https://www.kaggle.com/datasets/crowdflower/first-gop-debate-twitter-sentiment) |
| Fraudulent E-mail Corpus | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/fraudulent-email-corpus) |
| Getting Real about Fake News | kaggle | [바로가기](https://www.kaggle.com/datasets/mrisdal/fake-news) |
| Hacker News | kaggle | [바로가기](https://www.kaggle.com/datasets/hacker-news/hacker-news) |
| Hacker News Posts | kaggle | [바로가기](https://www.kaggle.com/datasets/hacker-news/hacker-news-posts) |
| Hate Speech and Offensive Language Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset) |
| Healthcare NLP: LLMs, Transformers, Datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/jpmiller/layoutlm) |
| Hillary Clinton and Donald Trump Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/benhamner/clinton-trump-tweets) |
| Hotel Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/datafiniti/hotel-reviews) |
| How ISIS Uses Twitter | kaggle | [바로가기](https://www.kaggle.com/datasets/fifthtribe/how-isis-uses-twitter) |
| Human vs. LLM Text Corpus | kaggle | [바로가기](https://www.kaggle.com/datasets/starblasters8/human-vs-llm-text-corpus) |
| IMDB dataset (Sentiment analysis) in CSV format | kaggle | [바로가기](https://www.kaggle.com/datasets/columbine/imdb-dataset-sentiment-analysis-in-csv-format) |
| IMDB Dataset of 50K Movie Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) |
| India News Headlines Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/therohk/india-headlines-news-dataset) |
| Irish Times - Waxy-Wany News | kaggle | [바로가기](https://www.kaggle.com/datasets/therohk/ireland-historical-news) |
| Large Sentiment Analysis Bangla Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/largesentimentdata) |
| LLM Generated Essays for the Detect AI Comp! | kaggle | [바로가기](https://www.kaggle.com/datasets/radek1/llm-generated-essays) |
| LLM: 7 prompt training dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/carlmcbrideellis/llm-7-prompt-training-dataset) |
| May 2015 Reddit Comments | kaggle | [바로가기](https://www.kaggle.com/datasets/kaggle/reddit-comments-may-2015) |
| Mc Donald's Store Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/nelgiriyewithana/mcdonalds-store-reviews) |
| Movie Dialog Corpus | kaggle | [바로가기](https://www.kaggle.com/datasets/Cornell-University/movie-dialog-corpus) |
| New York Times Comments | kaggle | [바로가기](https://www.kaggle.com/datasets/aashita/nyt-comments) |
| News Aggregator Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/news-aggregator-dataset) |
| News Category Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rmisra/news-category-dataset) |
| News Headlines Dataset For Sarcasm Detection | kaggle | [바로가기](https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection) |
| NEWS SUMMARY | kaggle | [바로가기](https://www.kaggle.com/datasets/sunnysai12345/news-summary) |
| Pfizer Vaccine Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/gpreda/pfizer-vaccine-tweets) |
| Phishing Email Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) |
| Python Questions from Stack Overflow | kaggle | [바로가기](https://www.kaggle.com/datasets/stackoverflow/pythonquestions) |
| Question Pairs Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/quora/question-pairs-dataset) |
| Question-Answer Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/questionanswer-dataset) |
| Russian Troll Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/vikasg/russian-troll-tweets) |
| Sentiment Analysis Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset) |
| Sentiment Labelled Sentences Data Set | kaggle | [바로가기](https://www.kaggle.com/datasets/marklvl/sentiment-labelled-sentences-data-set) |
| Sentiment Lexicons for 81 Languages | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/sentiment-lexicons-for-81-languages) |
| Sentiment140 dataset with 1.6 million tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/kazanova/sentiment140) |
| Sephora Products and Skincare Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews) |
| Sign Language Digits Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/ardamavi/sign-language-digits-dataset) |
| Sign Language MNIST | kaggle | [바로가기](https://www.kaggle.com/datasets/datamunge/sign-language-mnist) |
| SMS Spam Collection Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) |
| Source based Fake News Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/ruchi798/source-based-news-classification) |
| Spam email classification | kaggle | [바로가기](https://www.kaggle.com/datasets/ashfakyeafi/spam-email-classification) |
| Spam Mails Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/venky73/spam-mails-dataset) |
| Spam Text Message Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/team-ai/spam-text-message-classification) |
| Stack Overflow Data | kaggle | [바로가기](https://www.kaggle.com/datasets/stackoverflow/stackoverflow) |
| Stack Sample: 10% of Stack Overflow Q and A | kaggle | [바로가기](https://www.kaggle.com/datasets/stackoverflow/stacksample) |
| Stanford Question Answering Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/stanfordu/stanford-question-answering-dataset) |
| Steam Store 2024: Hot Picks and Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/kanchana1990/steam-store-2024-hot-picks-and-reviews) |
| Tamil NLP | kaggle | [바로가기](https://www.kaggle.com/datasets/sudalairajkumar/tamil-nlp) |
| Text Classification based on the BD newspaper | kaggle | [바로가기](https://www.kaggle.com/datasets/tahmidmir/text-classification-based-on-the-bd-newspaper) |
| Text Similarity | kaggle | [바로가기](https://www.kaggle.com/datasets/rishisankineni/text-similarity) |
| TextOCR - Text Extraction from Images Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/robikscube/textocr-text-extraction-from-images-dataset) |
| The Enron Email Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset) |
| Top 100 Bestselling Book Reviews on Amazon | kaggle | [바로가기](https://www.kaggle.com/datasets/anshtanwar/top-200-trending-books-with-reviews) |
| Trip Advisor Hotel Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews) |
| Trump Tweets | kaggle | [바로가기](https://www.kaggle.com/datasets/austinreese/trump-tweets) |
| Tweets about the Top Companies from 2015 to 2020 | kaggle | [바로가기](https://www.kaggle.com/datasets/omermetinn/tweets-about-the-top-companies-from-2015-to-2020) |
| Twitter and Reddit Sentimental analysis Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset) |
| Twitter Edge Nodes | kaggle | [바로가기](https://www.kaggle.com/datasets/mathurinache/twitter-edge-nodes) |
| Twitter Sentiment Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/arkhoshghalb/twitter-sentiment-analysis-hatred-speech) |
| Twitter Sentiment Analysis | kaggle | [바로가기](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis) |
| Twitter US Airline Sentiment | kaggle | [바로가기](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) |
| Twitter User Gender Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/crowdflower/twitter-user-gender-classification) |
| Ubuntu Dialogue Corpus | kaggle | [바로가기](https://www.kaggle.com/datasets/rtatman/ubuntu-dialogue-corpus) |
| Urdu /Hindi News Headlines | kaggle | [바로가기](https://www.kaggle.com/datasets/adnanzaidi/urdu-news-headlines) |
| Wine Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/zynicide/wine-reviews) |
| WLASL (World Level American Sign Language) Video | kaggle | [바로가기](https://www.kaggle.com/datasets/risangbaskoro/wlasl-processed) |
| Women's E-Commerce Clothing Reviews | kaggle | [바로가기](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews) |

### timeseries (총 46개)

| dataset_name | source | link |
|---|---|---|
| Amazon Seller Contact Intent Sequence | aws_open_data | [바로가기](https://registry.opendata.aws/amazon-seller-contact-intent-sequence/) |
| Animal Tracking - Acoustic Telemetry - Quality controlled detections | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_animal_acoustic_tracking_delayed_qc/) |
| ARPA-E PERFORM Forecast data | aws_open_data | [바로가기](https://registry.opendata.aws/arpa-e-perform/) |
| Aurora Multi-Sensor Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/aurora_msds/) |
| CRC-SAS/SISSA historical seasonal and subseasonal forecast database | aws_open_data | [바로가기](https://registry.opendata.aws/sissa-forecast-database-dataset/) |
| EPA Hourly Prognostic Meteorological Data | aws_open_data | [바로가기](https://registry.opendata.aws/epa-hourly-prognostic-meteorology/) |
| Inter-mission Time Series of Land Ice Velocity and Elevation (ITS_LIVE) | aws_open_data | [바로가기](https://registry.opendata.aws/its-live-data/) |
| Logan Unitigs and Contigs of the Sequence Read Archive (SRA) on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/pasteur-logan/) |
| Meta Graph Sequence Indexes | aws_open_data | [바로가기](https://registry.opendata.aws/metagraph/) |
| Moorings - Hourly time-series product | aws_open_data | [바로가기](https://registry.opendata.aws/aodn_mooring_hourly_timeseries_delayed_qc/) |
| Multi-robot, Multi-Sensor, Multi-Environment Event Dataset (M3ED) | aws_open_data | [바로가기](https://registry.opendata.aws/m3ed/) |
| NIH NCBI Sequence Read Archive (SRA) on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/ncbi-sra/) |
| Planette C3S Seasonal Forecast Data | aws_open_data | [바로가기](https://registry.opendata.aws/planette_c3s_seasonal_forecast_data/) |
| Pub Seq - Public Sequence Resource | aws_open_data | [바로가기](https://registry.opendata.aws/pubseq/) |
| Sonde Hub Radiosonde Telemetry | aws_open_data | [바로가기](https://registry.opendata.aws/sondehub-telemetry/) |
| daily-show-guests | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/daily-show-guests) |
| forecast-methodology | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/forecast-methodology) |
| governors-forecast-2018 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/governors-forecast-2018) |
| house-forecast-2018 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/house-forecast-2018) |
| senate-forecast-2018 | fivethirtyeight | [바로가기](https://github.com/fivethirtyeight/data/tree/master/senate-forecast-2018) |
| Air Passengers | kaggle | [바로가기](https://www.kaggle.com/datasets/rakannimer/air-passengers) |
| ATP Tennis 2000 - 2026 Daily update | kaggle | [바로가기](https://www.kaggle.com/datasets/dissfya/atp-tennis-2000-2023daily-pull) |
| Body signal of smoking | kaggle | [바로가기](https://www.kaggle.com/datasets/kukuroo3/body-signal-of-smoking) |
| Daily Happiness and Employee Turnover | kaggle | [바로가기](https://www.kaggle.com/datasets/harriken/employeeturnover) |
| Daily Power Generation in India (2017-2020) | kaggle | [바로가기](https://www.kaggle.com/datasets/navinmundhra/daily-power-generation-in-india-20172020) |
| Daily Public Opinion on Israel-Palestine War | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/reddit-on-israel-palestine-daily-updated) |
| Environmental Sensor Telemetry Data | kaggle | [바로가기](https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k) |
| Food Demand Forecasting | kaggle | [바로가기](https://www.kaggle.com/datasets/kannanaikkal/food-demand-forecasting) |
| Global Food Price Inflation | kaggle | [바로가기](https://www.kaggle.com/datasets/anshtanwar/monthly-food-price-estimates) |
| House Property Sales Time Series | kaggle | [바로가기](https://www.kaggle.com/datasets/htagholdings/property-sales) |
| Monkeypox Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/deepcontractor/monkeypox-dataset-daily-updated) |
| Motion Sense Dataset: Smartphone Sensor Data - HAR | kaggle | [바로가기](https://www.kaggle.com/datasets/malekzadeh/motionsense-dataset) |
| Movies Daily Update Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies) |
| pump_sensor_data | kaggle | [바로가기](https://www.kaggle.com/datasets/nphantawee/pump-sensor-data) |
| Retail Sales Forecasting | kaggle | [바로가기](https://www.kaggle.com/datasets/tevecsystems/retail-sales-forecasting) |
| S and P 500 Stocks (daily updated) | kaggle | [바로가기](https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks) |
| School Student Daily Attendance | kaggle | [바로가기](https://www.kaggle.com/datasets/sahirmaharajj/school-student-daily-attendance) |
| Smoking and Drinking Dataset with body signal | kaggle | [바로가기](https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset) |
| Spotify's Worldwide Daily Song Ranking | kaggle | [바로가기](https://www.kaggle.com/datasets/edumucelli/spotifys-worldwide-daily-song-ranking) |
| Store Sales Time Series Forecasting | kaggle | [바로가기](https://www.kaggle.com/datasets/hardikgarg03/store-sales-time-series-forecasting) |
| Superstore Sales Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) |
| Time Series Datasets | kaggle | [바로가기](https://www.kaggle.com/datasets/shenba/time-series-datasets) |
| Top 20 Play Store App Reviews (Daily Update) | kaggle | [바로가기](https://www.kaggle.com/datasets/odins0n/top-20-play-store-app-reviews-daily-update) |
| Top Spotify Songs in 73 Countries (Daily Updated) | kaggle | [바로가기](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated) |
| TOTAL SALE 2018 Yearly data of grocery shop | kaggle | [바로가기](https://www.kaggle.com/datasets/agatii/total-sale-2018-yearly-data-of-grocery-shop) |
| Walmart Sales Forecast | kaggle | [바로가기](https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast) |

### competition (총 45개)

| dataset_name | source | link |
|---|---|---|
| 2021 Amazon Last Mile Routing Research Challenge Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/amazon-last-mile-challenges/) |
| AI2 Reasoning Challenge (ARC) 2018 | aws_open_data | [바로가기](https://registry.opendata.aws/allenai-arc/) |
| Allen Institute for Neural Dynamics - Extracellular Electrophysiology Compression Benchmark | aws_open_data | [바로가기](https://registry.opendata.aws/allen-nd-ephys-compression/) |
| Astrophysics Division Galaxy Morphology Benchmark Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/apd_galaxymorph/) |
| Astrophysics Division Galaxy Segmentation Benchmark Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/apd_galaxysegmentation/) |
| Biological and Physical Sciences (BPS) Microscopy Benchmark Training Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/bps_microscopy/) |
| Biological and Physical Sciences (BPS) RNA Sequencing Benchmark Training Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/bps_rnaseq/) |
| DialoGLUE: A Natural Language Understanding Benchmark for Task-Oriented Dialogue | aws_open_data | [바로가기](https://registry.opendata.aws/dialoglue/) |
| Garvan Institute Long Read Sequencing Benchmark Data | aws_open_data | [바로가기](https://registry.opendata.aws/gtgseq/) |
| KITTI Vision Benchmark Suite | aws_open_data | [바로가기](https://registry.opendata.aws/kitti/) |
| LEarning bi Ochemical Prostate c Ancer Recurrence from histopathology sli Des challenge (LEOPARD) Dataset | aws_open_data | [바로가기](https://registry.opendata.aws/leopard/) |
| NASA SOHO/LASCO2 comet challenge on AWS | aws_open_data | [바로가기](https://registry.opendata.aws/nasa-soho-comet-challenge-on-aws/) |
| Oxford Nanopore Technologies Benchmark Datasets | aws_open_data | [바로가기](https://registry.opendata.aws/ont-open-data/) |
| Vesuvius Challenge - CT Scans of Herculaneum Papyri | aws_open_data | [바로가기](https://registry.opendata.aws/vesuvius-challenge-herculaneum-scrolls/) |
| Will Two Do? Varying Dimensions in Electrocardiography: The Physio Net/Computing in Cardiology Challenge 2021 | aws_open_data | [바로가기](https://registry.opendata.aws/challenge-2021/) |
| A 6-figure prize by soccer prediction | kaggle | [바로가기](https://www.kaggle.com/datasets/analystmasters/earn-your-6-figure-prize) |
| Adience Benchmark Gender And Age Classification | kaggle | [바로가기](https://www.kaggle.com/datasets/ttungl/adience-benchmark-gender-and-age-classification) |
| Amex Competition Data in Parquet Format | kaggle | [바로가기](https://www.kaggle.com/datasets/odins0n/amex-parquet) |
| Browse Comp: A Benchmark for Browsing Agents | kaggle | [바로가기](https://www.kaggle.com/datasets/openai/browsecomp-a-benchmark-for-browsing-agents) |
| Car Price Prediction Challenge | kaggle | [바로가기](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge) |
| Caravan Insurance Challenge | kaggle | [바로가기](https://www.kaggle.com/datasets/uciml/caravan-insurance-challenge) |
| COVID-19 Open Research Dataset Challenge (CORD-19) | kaggle | [바로가기](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge) |
| End ALS Kaggle Challenge | kaggle | [바로가기](https://www.kaggle.com/datasets/alsgroup/end-als) |
| FIFA - Football World Cup Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/iamsouravbanerjee/fifa-football-world-cup-dataset) |
| FIFA World Cup | kaggle | [바로가기](https://www.kaggle.com/datasets/abecklas/fifa-world-cup) |
| FIFA World Cup 2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/brenda89/fifa-world-cup-2022) |
| Fifa World Cup 2022: Complete Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/die9origephit/fifa-world-cup-2022-complete-dataset) |
| FIFA World Cup All Dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/abhijitdahatonde/fifa-world-cup-all-dataset) |
| Football - FIFA World Cup, 1930 - 2022 | kaggle | [바로가기](https://www.kaggle.com/datasets/piterfm/fifa-football-world-cup) |
| GTSRB - German Traffic Sign Recognition Benchmark | kaggle | [바로가기](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) |
| Gufhtugu Publications Dataset Challenge | kaggle | [바로가기](https://www.kaggle.com/datasets/zusmani/gufhtugu-publications-dataset-challenge) |
| House Price Prediction Challenge | kaggle | [바로가기](https://www.kaggle.com/datasets/anmolkumar/house-price-prediction-challenge) |
| jigsaw-toxic-comment-classification-challenge | kaggle | [바로가기](https://www.kaggle.com/datasets/julian3833/jigsaw-toxic-comment-classification-challenge) |
| kaggle_writeups For_Competition.pdf | kaggle | [바로가기](https://www.kaggle.com/datasets/marianadeem755/kaggle-writeupsfor-competition-pdf) |
| kaggle_writeups_For_Competition.csv | kaggle | [바로가기](https://www.kaggle.com/datasets/marianadeem755/kaggle-writeups-for-competition-csv) |
| MATH 500: Measuring Mathematical Problem Solving | kaggle | [바로가기](https://www.kaggle.com/datasets/open-benchmarks/math-500-measuring-mathematical-problem-solving) |
| Netflix Prize data | kaggle | [바로가기](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data) |
| Numenta Anomaly Benchmark (NAB) | kaggle | [바로가기](https://www.kaggle.com/datasets/boltzmannbrain/nab) |
| Pokemon- Weedle's Cave | kaggle | [바로가기](https://www.kaggle.com/datasets/terminus7/pokemon-challenge) |
| Restaurant Recommendation Challenge | kaggle | [바로가기](https://www.kaggle.com/datasets/mrmorj/restaurant-recommendation-challenge) |
| Sci Code | kaggle | [바로가기](https://www.kaggle.com/datasets/open-benchmarks/scicode) |
| Semantic Segmentation for Self Driving Cars | kaggle | [바로가기](https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge) |
| Ubiquant Competition Data in Parquet Format | kaggle | [바로가기](https://www.kaggle.com/datasets/robikscube/ubiquant-parquet) |
| UCI ML Drug Review dataset | kaggle | [바로가기](https://www.kaggle.com/datasets/jessicali9530/kuc-hackathon-winter-2018) |
| UNCOVER COVID-19 Challenge | kaggle | [바로가기](https://www.kaggle.com/datasets/roche-data-science-coalition/uncover) |

