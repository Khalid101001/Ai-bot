from telethon import TelegramClient, events
import requests
import time

api_id = '25875948'  # ضع API_ID الخاص بك
api_hash = 'bbc8cd4753b320c932bd56254d2917a0'  # ضع API_HASH الخاص بك
client = TelegramClient('ai_bot', api_id, api_hash)


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
                print(f":الرد {event.sender_id} ")
            else:
                await event.reply("خطأ بال api يمكن")
            
            time.sleep(2)  

    except Exception as e:
        print(f"خطأ: {str(e)}")

print("اشتغل...")
client.start()
client.run_until_disconnected()
