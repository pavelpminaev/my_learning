##### Fixtures могут использоваться чтобы не создавать коллекцию в каждом тесте при этом тесты использующие коллекцию НЕ МЕНЯЛИ ЕË

```python
import pytest
```

##### Создаем фикстуру
##### Запускается перед каждым тестом
```python
@pytest.fixture
def coll(): # имя фикстуры выбирается произвольно
    return ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False]
```

##### Pytest сам прокидывает результат вызова функции там, где она указана в аргументе.
##### Имя параметра совпадает с именем фикстуры
```python
def test_compact(coll):
    result = compact(coll)
    assert result == # тут ожидаемое значение
```

##### Не важно, что предыдущий тест сделал с коллекцией.
##### Здесь она будет новая, так как pytest вызывает coll() заново

```python
def test_select(coll):
    result = select(coll, ...)
    assert result == # тут ожидаемое значение
```

@pytest.fixture – декоратор, который добавляет произвольную функцию в процесс выполнения тестов. Фикстура выполняется перед теми тестами, в которых ее запросили через параметры функции. Важно, что имя аргумента совпадает с именем фикстуры.

для изменения времени по тестам
```python
import pytest

@pytest.fixture
def current_time():
    return datetime.now()

def test_foo(current_time):
    print(current_time)

def test_bar(current_time):
    print(current_time)

# Видно, что время изменилось
# 2021-05-19 14:46:14.109220
# 2021-05-19 14:46:14.|\
```
https://docs.pytest.org/en/stable/explanation/fixtures.html