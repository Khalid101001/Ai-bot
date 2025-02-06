from telethon import TelegramClient, events
import requests
import time

api_id = '25875948'  # ضع API_ID الخاص بك
api_hash = 'bbc8cd4753b320c932bd56254d2917a0'  # ضع API_HASH الخاص بك
bot_token = "7111720840:AAFcf5qbJ7h-yG0OFHIXUexu4eoU57r4l-A"  # تمت إضافة التوكن هنا

client = TelegramClient('ai_bot', api_id, api_hash).start(bot_token=bot_token)

AI_API = "https://atared.serv00.net/s/rq.php?text="

@client.on(events.NewMessage)
async def handle_message(event):
    try:
        if event.is_private:
            user_message = event.message.text
            response = requests.get(f"{AI_API}{user_message}")
            
            if response.status_code == 200:
                ai_reply = response.text
                await event.reply(ai_reply)
                print(f":الرد {event.sender_id}")
            else:
                await event.reply("خطأ بال API يمكن")
            
            time.sleep(2)

    except Exception as e:
        print(f"خطأ: {str(e)}")

print("اشتغل...")
client.run_until_disconnected()
