### Локальный запуск автотестов на эмуляторе
1. Склонировать репозиторий на свой локальный компьютер при помощи git clone
2. Создать и активировать виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установить зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Установить все, что необходимо для эмуляции андроида на PC
  ```bash
  appium --base-path /wb/hub
  ```
5. ЗАпустить эмулятор через Android Studio

6. Для запусков тестов локально ввести команду
  ```bash
  pytest -sv tests/android_app/test_wikipedia.py --context='local'
  ```
7. Получение отчёта allure:
```bash
allure serve allure-results
```
 
### Локальный запуск автотестов на bs

1. Выполнить
```bash
 pytest -sv tests/android_app/test_wikipedia.py --context='bs'
```
2. Получение отчёта allure:
```bash
allure serve allure-results