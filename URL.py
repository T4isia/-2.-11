import requests
from bs4 import BeautifulSoup


URL_GIST = (
    "https://gist.githubusercontent.com/T4isia/"
    "4c9540e947791a1c2a6755097b77ea4c/raw/"
    "6a8b9b2fb89e8fbd34bc07cb35d8e2d96d1b3c5c/gistfile1.txt"
)


def ddmmyyyy_from_my_url(url_web: str):
    # Возвращает текст страницы по URL в виде строки
    try:
        response = requests.get(url_web)
        data = response.content.decode("utf-8")
        soup = BeautifulSoup(data, "html.parser")
        full_data = soup.get_text(" ", strip=True)
        return full_data

    except requests.RequestException as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    print(ddmmyyyy_from_my_url(URL_GIST))
