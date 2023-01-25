name: githab-actions

on:
  - push

jobs:
  build:
    runs-on: ${{matrix.os}}
    strategy:
      matrix:
        # we want to test our package on several versions of Python
        python-version: [3.8, 3.9]
        # several OS
        os: [ ubuntu-latest, macos-latest ]

    steps:
      # Клонируем репозиторий
      - uses: actions/checkout@v2
      # Setup several versions of Python
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}

      # make depends on poetry
      - name: Install dependencies
        run: |
          pip install poetry
          make install

      # Запускаем линтер
      - name: Run linter
        run: |
          make lint

      # Запускаем тесты
      - name: Run tests
        run: |
          make tests