import telebot
import json
bot = telebot.TeleBot('7163634134:AAHGwXCdfRgvplwEVeFOFVF4lekHrUelJB0')
def notify_employee(telegram_id, message):
    try:
        kb = {
            "inline_keyboard": [
                [{"text": "Отправить сообщение", "callback_data": "send_message"}]
            ]
        }
        kb_json = json.dumps(kb)
        bot.send_message(telegram_id, message,reply_markup=kb_json)
    except Exception as e:
        print(f"Ошибка при отправке сообщения на Telegram: {e}")
def create_lead_message(action, lead):
    address = []

    if lead.country_id:
        address.append(lead.country_id.name)
    if lead.state_id:
        address.append(lead.state_id.name)
    if lead.city:
        address.append(lead.city)
    if lead.street:
        address.append(lead.street)
    if lead.street2:
        address.append(lead.street2)
    if lead.zip:
        address.append(lead.zip)

    return f'ID:{lead.id}\n{action} \"{lead.name}\"\nАдрес: ' + ", ".join(address)