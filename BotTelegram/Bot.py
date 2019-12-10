import requests

BOT_API_TOKEN = "1007041613:AAF0hQTrpaw-PREqTqnSbfAD9HKvolZVgVA"


def send_response(user_id, text):
    print("SEND MESSAGE")
    SEND_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
    CHAT_ID = user_id
    url = SEND_URL.format(
        BOT_API_TOKEN,
        CHAT_ID,
        text
    )
    requests.get(url)


if __name__ == '__main__':
    READ_URL = "https://api.telegram.org/bot{}/getUpdates"
    url = READ_URL.format(BOT_API_TOKEN)
    response = requests.get(url)
    updates = response.json().get("result", [])
    for msg in updates:
        text = msg["message"]["text"]
        user_id = msg["message"]["from"]["id"]

        if "погода" not in text.lower():
            continue
        send_response(user_id, "Сейчас в Якутске холодно.")
