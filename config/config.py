TOKEN = "5360699267:AAERB5v0pSG9ngWeJX2BlO3gSlZmjskpmxE"

text_in_start_new_user = '☀️*Доброго времени суток*, бот создан, чтобы обрабатывать заявки и обращения пользователей\. Чтобы воспользоваться этим, пришлите для начала Ваше *Имя* и *Фамилию*'
bad_name_in_reg = "⛔📛 *Имя* и *Фамилия* должны быть введены через один _пробел_, и должны быть написаны через _кириллицу_\. Также должны быть _заглваные буквы_\. *Учтите формат и попробуйте снова:*"
text_in_start_phone_number = "📞 Теперь отправьте Ваш *номер телефона* через *\+7* следующим сообщением:"
bad_phone_in_reg = "⛔📛⛔ *Номер телефона* должен содержать 11 цифр и должен обязательно содержать в начале *\+7\. Учтите формат и попробуйте снова*"
bad_message_in_report = "⛔📛 В данном пункте нужно обязательно отправить *фотографию* или *видео* в виде медиа\-сообщения\. _*Попробуйте еще раз:*_ "
report_success_message = "✅ *Жалоба отправлена администрации\.* _Спасибо за Ваше обращение\!_"
bad_offer_message = "⛔📛 Предложение должно содержать только текст"
text_in_start_old_user = '✈️ *Добро пожаловать* _в главное меню чат\-бота Управляющей компании "УЭР\-ЮГ"\._ Здесь вы можете оставить заявку для управляющей компании или направить свое предложение по управлению домом\. Просто воспользуйтесь кнопками _*меню*_, чтобы взаимодействовать с функциями бота:'
offer_success_message = "*✅💡Идея принята и передана администрации\.* _Спасибо за Ваше обращение\!_"

answer_in_telephone_call = "✅*Отлично\!* Наш диспетчер перезвонит Вам в ближайшее время\."
phone_update_settings_success = "🛠✅🛠Настройки *номера* успешно применены\!"
name_update_settings_success = "🛠✅🛠Настройки *имени* успешно применены\!"


contacts_in_start = """__Управляющая компания:__
*Диспетчерская служба 000 «УЭР\-ЮГ»*
\+7 4722 35\-5005
*Инженеры 000 «УЭР\-ЮГ»*
\+7 920 565\-28\-86
*Бухгалтерия 000 «УЭР\-ЮГ»*
\+7 4722 35\-5006
_Белгороа, Сеято\-Троицкий 6\-р, д\. 15, подъезд
№ 1_

__Телефоны для открытия вороти
шлагбауме:__
*Шлагбаум «Набережная»*
\+7 920 554\-8774\.
*Ворота «Харьковские»*
\+7 920 554\-87\-40
*Ворота «Мост»*
\+7 920 554\-64\-05
*Калитка 1 «Мост»*
\+7 920 554\-42\-10
*Калитка 2 «Мост»*
\+7 920 554\-89\-04
*Калитка 3 «Харьковская»*
\+7 920 554\-87\-29
*Калитка 4 «Харьковская»*
\+7 920 554\-85\-02

*Охрана*
\+7 915 57\-91\-457

*Участковый*
Куленцова Марина Владимировне
\+7 999 421\-53\-72"""

text_in_start_subbmit_application = "⛔👇⛔ _Выберите категорию, по которой Вы хотите оставить заявку в УК_"
text_in_start_settings = "👇 _Выберите способ связи из нижеперечисленного списка:_"
text_in_start_connection= "⚙️ Тут Вы сможете поменять *Имя* и *Фамилию* в Базе данных нашего бота или же можете поменять Ваш *номер телефона*, если Вы изначально вводили что\-то неверно\. Выберите, что хотите поменять или вернитесь назад в _*главное меню*_: "
first_text_in_create_report = "first"
second_text_in_create_report = "second"
third_text_in_create_report = "third"

categories = {
    "⛔ Оставить заявку": {
        "⛔Оставить заявку": {
            "▶️Пропустить": {
                "▶️Пропустить": ""
            }
        },
        "💡Поделиться предложением": ""
    },
    "📞 Связаться": {
        "📞 Перезвоните мне": {"✅Да": "go to main",
                                "🔙 Оставить номер телефона": ""
                              },
        "📞 Свяжитесь со мной в чат-боте": {"❌📞Завершить диалог": ""}
    },
    "⚙️ Настройки": {
        "🛠Поменять имя": "",
        "🛠Сменить номер": ""
    },
    }

categories_messages = {
    "0": "⛔👇⛔ _Выберите категорию, по которой Вы хотите оставить заявку в УК_",
    "2": "⚙️ Тут Вы сможете поменять *Имя* и *Фамилию* в Базе данных нашего бота или же можете поменять Ваш *номер телефона*, если Вы изначально вводили что\-то неверно\. Выберите, что хотите поменять или вернитесь назад в _*главное меню*_: ",
    "1": "👇 _Выберите способ связи из нижеперечисленного списка:_",
    "10": "*Это ваш верный номер телефона* \|phone\| ? _Если да, то нажмите соответствующую кнопку, *если нет*_ впишите свой актуальный номер телефона здесь",
    "100": "✅*Отлично\!* Наш диспетчер перезвонит Вам в ближайшее время\.",
    "11": "✅📞✅ Добрый день\! Я \- диспетчер управляющей компании \"УЭР\-ЮГ\", готов помочь Вам\. Напишите пожалуйста, интересующий Вас вопрос и ожидайте",
    "110": "❌📞*Диалог с администратором завершен\.\.\.*",
    "00": "_*Шаг 1/3\.*_ 📝Напишите Адрес или ориентри проблемы \(улицу, номер дома, подъезд, этаж и квартиру\) или пропустите этот пункт:",
    "000": "_*Шаг 2/3\.*_ 🖼Прикрепите фотографию или видео к своей заявке или пропустите этот пунк:",
    "0000": "_*Шаг 3/3\.*_ 📛Напишите причину обращения в подробностях:",
    "01": "💡 _*Распишите Ваше предложение в подробностях*_",
    "20": "_Отправьте свое Имя и фамилию\, чтобы поменять настройки\:_",
    "21": "_Отправьте свой номер телефона\, чтобы поменять настройки\:_"
}
