import re

def is_valid_date(date_str):
    #Проверка корректности даты по регулярным выражениям
    try:
        day, month, year = map(int, date_str.split("."))

        if not (1900 <= year < 2026):
            return False

        # Определяем, високосный ли год
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            pattern = re.compile(r"""
            ^(?:
              (0?[1-9]|[12][0-9]|3[01])\.(0?[13578]|1[02])\.\d{4} |
              (0?[1-9]|[12][0-9]|30)\.(0?[469]|11)\.\d{4} |
              (0?[1-9]|1[0-9]|2[0-9])\.0?2\.\d{4}
            )$
            """, re.VERBOSE)

        else:
            pattern = re.compile(r"""
            ^(?:
              (0?[1-9]|[12][0-9]|3[01])\.(0?[13578]|1[02])\.\d{4} |
              (0?[1-9]|[12][0-9]|30)\.(0?[469]|11)\.\d{4} |
              (0?[1-9]|1[0-9]|2[0-8])\.0?2\.\d{4}
            )$
            """, re.VERBOSE)

        return bool(pattern.match(date_str))

    except ValueError:
        return False

def coincidence(text):  # Находит все корректные даты в тексте
    matches = re.findall(r"\b\d{1,2}\.\d{1,2}\.\d{4}\b", text)
    return [d for d in matches if is_valid_date(d)]


if __name__ == "__main__":
    pass
