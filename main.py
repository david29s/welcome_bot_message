import telebot

id = '548881516'
bot = telebot.TeleBot ('534368752:AAFSKVroqATtUaKWRzB6J_XgMDvdsZTQ8W4')

@bot.message_handler(content_types=['new_chat_members'])
def send_message(message):
    bot.send_message(message.chat.id, text = 'Hello, {} {}! We are happy that you join {}!'.format(message.new_chat_member.first_name.encode('utf-8'),
                                                                                            message.new_chat_member.last_name.encode('utf-8'),
                                                                                            message.chat.title.encode('utf-8')))


bot.polling(none_stop=True)