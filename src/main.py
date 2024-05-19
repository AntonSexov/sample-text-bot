from image_processing import add_text_to_image

from config import API_TOKEN
import telebot
import sys



if __name__ == "__main__":
    bot = telebot.TeleBot(API_TOKEN)
    
    @bot.message_handler(commands=['start'])
    def start(msg):
        bot.send_message(msg.from_user.id, "just send the photo and write top and bottom text in description(top and bottom text is split by | )")

    @bot.message_handler(content_types=['photo'])
    def do_the_funny(msg):
        fid = msg.photo[-1].file_id
        finfo = bot.get_file(fid)
        downloaded_file = bot.download_file(finfo.file_path)
        with open(f"images/{msg.from_user.id}.jpg", "wb") as nf:
            nf.write(downloaded_file)
        
        if msg.caption != None:
            captions = msg.caption.split("|")
            top, bottom = captions[0], captions[1]
            add_text_to_image(f"images/{msg.from_user.id}.jpg", f"images/{msg.from_user.id}_funny.jpg", top, bottom)
            bot.send_photo(msg.from_user.id, open(f"images/{msg.from_user.id}_funny.jpg", "rb"))
        else:
            add_text_to_image(f"images/{msg.from_user.id}.jpg", f"images/{msg.from_user.id}_funny.jpg")
            bot.send_photo(msg.from_user.id, open(f"images/{msg.from_user.id}_funny.jpg", "rb"))
    
    

    bot.polling(none_stop=True, interval=0)