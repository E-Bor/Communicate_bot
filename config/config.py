TOKEN = "5360699267:AAERB5v0pSG9ngWeJX2BlO3gSlZmjskpmxE"

text_in_start_new_user = '☀️*Доброго времени суток*, бот создан, чтобы обрабатывать заявки и обращения пользователей\. Чтобы воспользоваться этим, пришлите для начала Ваше *Имя* и *Фамилию*'

text_in_start_old_user = '✈️ *Добро пожаловать* _в главное меню чат\-бота Управляющей компании "УЭР\-ЮГ"\._ Здесь вы можете оставить заявку для управляющей компании или направить свое предложение по управлению домом\. Просто воспользуйтесь кнопками _*меню*_, чтобы взаимодействовать с функциями бота:'
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

categories = {
    "⛔ Оставить заявку": {
        "⛔Оставить заявку": "",
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
    "10": "*Это ваш верный номер телефона?* \|phone\| ? _Если да, то нажмите соответствующую кнопку, *если нет*_ впишите свой актуальный номер телефона здесь",
    "100": "✅*Отлично\!* Наш диспетчер перезвонит Вам в ближайшее время\.",
    "11": "✅📞✅ Добрый день\! Я \- диспетчер управляющей компании \"УЭР\-ЮГ\", готов помочь Вам\. Напишите пожалуйста, интересующий Вас вопрос и ожидайте",
    "110": "❌📞*Диалог с администратором завершен\.\.\.*"
}
