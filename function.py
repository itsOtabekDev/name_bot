import json
with open('ismlar_baza.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
name_meaning_dict = {item['properties']['name'].lower(): item['properties']['meaning'] for item in data}

def handle_text(update, context):
    user_text = update.message.text.strip()
    user_text_lower = user_text.lower()
    if user_text_lower.lower() in name_meaning_dict:
        meaning = name_meaning_dict[user_text_lower]
        update.message.reply_text(f"bu '{user_text}' isimni manosi: {meaning}")
    else: update.message.reply_text(f'{user_text} - bu ism bazada topilmadi ❌')

    print(f"user text = : {user_text}")
