# QA Guru: Дипломный проект
Реализация набора автотестов (UI, Mobile, API) для сервиса <code>Last.FM</code>

# Инструменты и технологии, используемые в проекте
<p align="center">
<a href="https://www.python.org/"><img src="files/readme_images/python.svg" width="50" height="50"  alt="PYTHON"/></a>
<a href="https://www.selenium.dev/"><img src="files/readme_images/selenium.svg" width="50" height="50"  alt="SELENIUM"/></a>
<a href="https://docs.pytest.org/en/"><img src="files/readme_images/pytest.svg" width="50" height="50"  alt="SELENIUM"/></a>
<a href="https://www.jetbrains.com/ru-ru/pycharm/"><img src="files/readme_images/pycharm.svg" width="50" height="50"  alt="PYCHARM"/></a>
<a href="https://docs.pydantic.dev/latest/"><img src="files/readme_images/pydantic.svg" width="50" height="50"  alt="PYDANTIC"/></a>
<a href="https://pypi.org/project/python-dotenv/"><img src="files/readme_images/dotenv.svg" width="50" height="50"  alt=".ENV"/></a>
<a href="https://www.jenkins.io/"><img src="files/readme_images/jenkins.svg" width="50" height="50"  alt="JENKINS"/></a>
<a href="https://python-poetry.org/"><img src="files/readme_images/poetry.svg" width="50" height="50"  alt="POETRY"/></a>
<a href="https://www.last.fm/api"><img src="files/readme_images/lastdotfm.svg" width="50" height="50"  alt="LAST.FM"/></a>
</p>

Весь проект выполнен на языке <code>Python</code>, а также дополнительно:
 - для UI-тестов применялись: <code>Selene</code>
 - для API-тестов применялись: <code>Requests</code>, <code>JSONSchema</code>
 - для мобильных тестов на Android: <code>Appium</code>

Запуск тестов и формирование отчетов о запусках формируется с помощью:
 - <code>Jenkins</code>
 - <code>Selenoid</code>
 - <code>Browserstack</code>

# Покрытый функционал

## <a href='https://github.com/marcelinleen/qa_guru_diploma/tree/main/tests/web'>UI-тесты</a>
 - авторизация пользователя;
 - поиск исполнителя, альбома и трека;
 - подписка на другого юзера (добавление в друзья);
 - просмотр понравившихся треков;
 - выход из учетной записи

## <a href='https://github.com/marcelinleen/qa_guru_diploma/tree/main/tests/api'>API-тесты</a>
 - авторизация пользователя;
 - поиск исполнителя, альбома и трека (успешный и неуспешный);
 - добавить трек в **Понравившиеся**;
 - получить список треков из **Понравившихся**

## <a href='https://github.com/marcelinleen/qa_guru_diploma/tree/main/tests/mobile'>Мобильные тесты</a>
 - авторизация пользователя;
 - получение истории чартов юзера за определенный период (30 дней);
 - выход из учетной записи

## <a href='https://jenkins.autotests.cloud/job/marcelinleen_UI_diploma_project/'>Jenkins job для UI-тестов</a>
<img src="files/readme_images/jenkins_job_ui.jpg" alt="JENKINS JOB FOR UI"/></a>

## <a href='https://jenkins.autotests.cloud/job/marcelinleen_API_diploma_project/'>Jenkins job для API-тестов</a>
<img src="files/readme_images/jenkins_job_api.jpg" alt="JENKINS JOB FOR API"/></a>

## <a href='https://jenkins.autotests.cloud/job/marcelinleen_mobile_diploma_project/'>Jenkins job для мобильных тестов</a>
<img src="files/readme_images/jenkins_job_mobile.jpg" alt="JENKINS JOB FOR MOBILE"/></a>

## Удаленный запуск
Удаленный запуск происходит по команде:

### UI-тесты:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest --browser=${BROWSER} --browser_version=${BROWSER_VERSION} tests/web
```

### API-тесты:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests/api
```

### Мобильные тесты:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest --env=${ENV} tests/mobile
```

# Локальный запуск
Для локального запуска с значениями по умолчанию необходимо произвести команду:
```
pytest tests
```

## Локальный запуск мобильных тестов

Мобильные тесты могут быть запущены как в <code>BrowserStack</code>, так и локально. 
Для запуска в BrowserStack необходимо указать команду:
```
pytest --env=browserstack tests/mobile/
```

Тогда как для локального запуска:
```
pytest --env=local tests/mobile/
```

При этом, для запуска мобильных тестов локально, необходимо убедиться, что:
 - <code>Appium Server</code> запущен;
 - эмулятор и/или реальный девайс подключен;
 - созданы настройки для запуска в _.env-файл_, расположенные в директории <code>tests/mobile</code>. Пример настроек можно найти в файле <a href='https://github.com/marcelinleen/qa_guru_diploma/blob/main/tests/mobile/.env.mobile.local.example'>.env.mobile.local.example</a>

Пример такого параметризованного запуска можно увидеть на <a href="https://www.loom.com/share/a35e74b30d6a4edf976cac0692f16e62?sid=eb825c54-55ef-4223-8cda-25e3dbe1f011">видео</a>.
По умолчанию запуск тестов происходит на <code>BrowserStack</code>.

# Подготовка к удаленному запуску
### Удаленный запуск UI-тестов
Для запуска UI-тестов, в разделе **Сборка**, необходимо добавить шаг по созданию/изменению .env-файл с данными тестовой учетной записи (**LOGIN**, **PASSWORD**), а также указать данные для авторизации на стороне Selenoid (**SELENOID_LOGIN**, **SELENOID_PASSWORD**).
В проекте все чувствительные данные хранятся в файле <code>.env.personal_data</code> - его пример можно найти в проекте в файле <a href='https://github.com/marcelinleen/qa_guru_diploma/blob/main/.env.personal_data.example'>.env.personal_data.example</a>

<img src="files/readme_images/env_setting.jpg" alt=".ENV FILE CREATE"/></a>

### Удаленный запуск API-тестов
Для запуска API-тестов, в тот же файл <code>.env.personal_data</code> необходимо добавить данные тестовые учетной записи (**LOGIN**, **PASSWORD**), а также API-данные учетной записи (**API_KEY**, **API_SECRET**) - пример таких данных также можно найти в файле <a href='https://github.com/marcelinleen/qa_guru_diploma/blob/main/.env.personal_data.example'>.env.personal_data.example</a>.

Актуальные для юзера данные можно найти на [странице API-подключений](https://www.last.fm/api/accounts) после авторизации на сервисе.
<img src="files/readme_images/api_data.jpg" alt="API LAST.FM DATA"/></a>

<img src="files/readme_images/env_setting.jpg" alt=".ENV FILE CREATE"/></a>

### Удаленный запуск мобильных тестов
Для запуска мобильных тестов, в разделе **Сборка**, необходимо добавить шаг по созданию/изменению .env-файл с данными тестовой учетной записи (**LOGIN**, **PASSWORD**).

<img src="files/readme_images/env_setting.jpg" alt=".ENV FILE CREATE"/></a>

Также необходимо добавить шаг по созданию/изменению .env-файл в директории <code>tests/mobile</code> с указанием следующих настроек, необходимых для подключению к **BrowserStack**:

<img src="files/readme_images/mobile_env.jpg" alt="MOBILE .ENV FILE CREATE"/></a>

Пример данного файла есть в проекте - <a href='https://github.com/marcelinleen/qa_guru_diploma/blob/main/tests/mobile/.env.mobile.browserstack.example'>.env.mobile.browserstack.example</a>.

# Отчеты о запусках

### Allure для UI-тестов

<img src="files/readme_images/allure_report_ui.jpg" alt="ALLURE REPORT FOR UI TESTS"/></a>

### Allure для API-тестов

<img src="files/readme_images/allure_report_api.jpg" alt="ALLURE REPORT FOR API TESTS"/></a>

### Allure для мобильных тестов

<img src="files/readme_images/allure_report_mobile.jpg" alt="ALLURE REPORT FOR MOBILE TESTS"/></a>