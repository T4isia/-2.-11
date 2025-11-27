from url_work import ddmmyyyy_from_my_url, URL_GIST
from reg_exe import coincidence


# ------------------ГЛАВНОЕ МЕНЮ------------------
print("Если вы хотите сделать проверку "
      "на корректность даты через ввод с консоли — введите 1")
print("Если вы хотите сделать проверку "
      "на корректность даты через ввод с сайта — введите 2")

user_choice  = input("Введите 1 или 2: ")

if user_choice  == "1":  # Проверка через консоль
    data = input("Введите дату: ")
    dates = coincidence(data)
    if dates:
        print("Дата существует")
        print(*dates, sep="\n")
    else:
        print("Даты не существует")

elif user_choice  == "2":  # Проверка с сайта
    data = ddmmyyyy_from_my_url(URL_GIST)
    if data:
        results = coincidence(data)
        if results:
            print("Найденные даты на сайте:")
            print(*results, sep="\n")
        else:
            print("На сайте дат не найдено.")
    else:
        print("Не удалось получить данные с сайта.")

else:  # Если ошибка
    print("Некорректный ввод. Попробуйте заново")

if __name__ == "__main__":
    pass
