import re
import telebot

tok = "8834585615:AAFqJO5-iBp0lxRtAJ8qeA52RotqPI5V-nc"
bot = telebot.TeleBot(tok)

# ပုံနဲ့ စာသား နှစ်မျိုးလုံး လက်ခံနိုင်အောင် content_types ကို ထည့်ပေးလိုက်ပါပြီ
@bot.message_handler(content_types=['text', 'photo'])
def handle_group_message(msg):
    # စာသားက msg.text မှာလား သို့မဟုတ် ပုံနဲ့တွဲတဲ့ caption မှာလားဆိုတာကို စစ်ခြင်း
    text = msg.text if msg.text else msg.caption
    
    if not text:
        return

    match = re.search(r"\d+\s*\(\s*\d+\s*\)\s*\d*", text)

    if match:
        raw_id = match.group(0).replace(" ", "")

        reply_text = f"💎 <b>Copyer Polaroid Bot</b>\n\n<code>{raw_id}</code>"

        bot.reply_to(msg, reply_text, parse_mode="HTML")

bot.infinity_polling()
