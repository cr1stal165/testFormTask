# Тестовое

Команды для запуска:

1. ```docker build . -t test_app:latest ```
2. ```docker run -d -p 7329:8000 test_app ```

После переходим по адресу: http://localhost:7329/docs

Чтобы сделать запрос, выполните post запрос /get_form, передав query параметр fields

Пример выполнения запроса:

fields = "feedback=test_feedback&rating=5stars"

Если форма есть в бд, то ответ будет вида:
{
  "template_name": "Название формы"
}

Если такой формы нет, то вернуться переданные параметры, но с нужным типом:

{
  "feedback": "text",
  "rating": "text"
}
