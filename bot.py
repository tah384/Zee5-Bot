from telegram.ext import Updater, CommandHandler
import requests

TOKEN = "7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To"

def download_ott(update, context):
    url = context.args[0]
    r = requests.get(url)

    with open("downloaded_ott_content.mp4", "wb") as f:
        f.write(r.content)

    update.message.reply_text("OTT content downloaded successfully! 🎥🔥")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("download_ott", download_ott))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()