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
5. Запустить эмулятор через Android Studio

6. Для запусков тестов локально ввести команду
  ```bash
  pytest -m local_real
  ```
7. Получение отчёта allure:
```bash
allure serve allure-results
```
8. Для запуска тестов локально через эмулятор ввести команду
  ```bash
  pytest -m local_emulator
  ```

### Локальный запуск автотестов на bs

1. Выполнить
```bash
  pytest -m bs
```
2. Получение отчёта allure:
```bash
allure serve allure-results
