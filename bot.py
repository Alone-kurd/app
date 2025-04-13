### کۆدی بۆت

```python
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# گەشەی لاگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# فەرمان بەرزکردنەوە
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سڵاو! بۆ نوێکردنەوەی فایلی IPA، دەتوانیت فایلی خۆت ناردن.')

# فەرمان بۆ نوێکردنەوە
def update_ipa(update: Update, context: CallbackContext) -> None:
    # چەند کۆدەکی تایبەتی پێویست بۆ نوێکردنەوە ئەوا دانراوە
    if update.message.document:
        file = update.message.document.get_file()
        file.download('uploaded_file.ipa')
        # لێرەدا پەیوەندیدانی ساین کردنی فایلی IPA بیکە
        # بەرزکردنەوەی پەیام:
        update.message.reply_text('فایلەکە بە سەرکەوتوویی دانرا!')
    else:
        update.message.reply_text('تکایە فایلی IPA ناردن.')

def main():
    # گرتنی توکەنی بۆت
    updater = Updater("7859344629:AAHG_LZfvHfIgF03Y8fszj4dr6tV4oYobeI")

    # گرتنی دیاریکردن
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.document.mime_type("application/octet-stream"), update_ipa))

    # ئەم کۆدە بەرەوپێش گەرانەوە
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

### ڕوونی کۆد

- Import کردنەکان: 
  - `logging`: بۆ گەشەی لاگ بەکاردێت.
  - `telegram` و `telegram.ext` بۆ بەکارهێنانی APIی تیلیگرام.

- فەرمانی `start`: 
  - فەرمانێکی سادە کە کاتی پەیوەند کردنی باشتر بڵاو دەکات.

- فەرمانی `update_ipa`: 
  - ئەم فەرمانە فایلی IPAی ناردنی بە کاربەر وەرگرتن و پەیوەندیدانی فایلی ناردراوی دانا دەکات.
  - بەرزکردنەوەی فایلی زیاد بە شێوەی وە تکنیکی تایبەتی تەنها شتە تایبەتی پەیوەندیدابن.

- Main function (`main()`): 
  - کۆمەڵە فەرمانە بەرز دەکات و botەکە بەرەوپێش گەرانەوە سەری ڕووداوەکان دەبەوێت.

### بەرزکردنەوە

- تۆ پێویستە توکەنی بۆتەکە لە شوێنی "YOUR_BOT_TOKEN_HERE" بگۆری.

###
