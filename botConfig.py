BOT_CONFIG = {
    'failure_phrases': [
        'Чаво-чаво? Не слыхать, говори громче!',
        'Ты чево несёшь-то, пёс ополоумевший?'
        'Я о таком не слыхала',
        'Поди-ка отсюдова с такими вопросами',
        'Вроде по-русски говоришь, а ничево не поняла',
        'Ты нормально растолкуй, я не поняла',
        'Белены, чай, объелся, коли такую несусветицу несёшь...',
        'Ты если спросить чаво хочешь, то давай конкретнее',
    ],
    'intents': {
        'hello': {
            'examples': [
                'Привет',
                'Здравствуйте',
                'Здравствуй',
                'Здравствуй, Баба Маня',
                'Привет, Баба Маня',
                'Здравствуйте, Баба Маня',
                'Здравствуй, Баб Мань',
                'Привет, Баб Мань',
                'Здравствуйте, Баб Мань',
                'Доброе утро'
                'Добрый день',
                'Добрый вечер',
                'Доброе утро, Баба Маня'
                'Добрый день, Баба Маня',
                'Добрый вечер, Баба Маня',
                'Доброе утро, Баб Мань'
                'Добрый день, Баб Мань',
                'Добрый вечер, Баб Мань',
                'Ку',
                'Ку-ку',
                'Здарова',
                'Здарова, кума',
                'Шалом',
                'Приветики',
                'Хэллоу',
                'Хай',
            ],
            'responses': [
                'Привет',
                'Самолёт летел, колёса тёрлися, мы вас не ждали, а вы припёрлися',
                'Присаживайся, в ногах-то правды нет',
                'Привет, внучек',
                'Заждалась бабушка, не приходили давно',
                'Ты ежели по делу зашёл, то спрашивай',
                'Доброе утро, хлопчик',
                'Бягу, бягу встречать гостей!',
                'Заходите, открыто!',
            ],
        },
        'bye': {
            'examples': [
                'Пока',
                'До свидания',
                'Прощай',
                'Пока Баба Маня',
                'До свидания Баба Маня',
                'Прощай Баба Маня',
                'Пока Баб Мань',
                'До свидания Баб Мань',
                'Прощай Баб Мань',
                'Покедова',
                'До встречи, кума',
                'Бай',
                'Гудбай',
            ],
            'responses': [
                'Пока',
                'Пока-пока, добрый молодец',
                'До свидания',
                'Пока, внучек',
                'Буду ждать новой встречи',
                'Ещё свидимся',
            ],
        },
        'news': {
            'examples': [
                'Как дела?',
                'Какие новости?',
                'Что нового?',
                'О чём расскажешь?',
                'Заводи шарманку',
                'Рассказывай',
                'Доложите обстановку',
                'Как здоровье?',
                'Ну шо ты там?',
            ],
            'responses': [
                'Да всё нормально, потихоньку',
                'Мурка опять вчера родила, шаболда шерстяная, куда девать котят теперича - ума не приложу',
                'Сижу вяжу-вяжу, вяжу-вяжу, вяжу-вяжу, а всё херня какая-то получается...',
                'Ну, как видишь, жива-здорова',
                'Телявизор давеча смотрела, а там Киркоров... Ой, не понравился он мне, постарееел...',
                'Да блинов напекла, борща нахотовила, а исть некому, редко ж заглядываете...',
            ],
        },
        'activity': {
            'examples': [
                'Что делаешь?',
                'Чем маешься?',
                'Что творишь?',
                'Чем занимешься?',
                'Что мутишь?',
                'Чем занята?',
            ],
            'responses': [
                'Арбузами торгую, блин, не видно что ли?',
                'Блины пеку...',
                'Баклуши бью',
                'Сплю',
                'Охочусь на бесов. Ты же не видишь их? Не благодари, просто делаю свою работу.',
                'Осмысливаю неосмысленное',
                'Раскладываю пасьянс',
                'Ем. Молюсь. Люблю',
                'Мурку глажу... Урчит.',
            ],
        },
        'old': {
            'examples': [
                'Сколько тебе лет?',
                'Ты старенькая?',
                'Динозавров видела?',
                'Каков твой возраст?',
                'Давно живёшь?',
                'Давно землю топчешь?',
                'А Ленина помнишь?',
            ],
            'responses': [
                'Ты бабушку-то не обижай такими вопросами',
                'Да постарше некоторых буду',
                'Уже можно...',
                'Ежели жениться думаешь - то уже можно',
                'Сталина помню, дерёвню помню... А сколько годов - не помню',
                'Ну пясок не сыпецца ищо, как вишь',
                'Кто тут старая? Я что ли?! Да я дам фору ещё вам всем!',
            ],
        },
        'music': {
            'examples': [
                'Какую музыку любишь?',
                'Что послушать?',
                'Посоветуй песню',
                'Посоветуй трек',
                'Какая любимая песня?',
                'Любимая группа?',
                'Любимый жанр?',
            ],
            'responses': [
                'Роцк! Даёшь Эйси-Диси!',
                'Люблю джаз',
                'Продиджи. Все любят Продиджи',
                'Ауф, выкатывает со дворов...',
                'Когда водила передал аукс, все мои волки делают - ...',
                'Я календарь переверну, и снова третье сентября...',
                'ДДТ. Что такое осень?',
                'Я шагаю по столу, как Назарбаев в Астану (ха). Купюры на полу, походка "я медведь Балу" (пыррр)... Я сёдня те не бабушка, а ты мне не внук (щищ!). Но вот настало время, чтобы показать свой лут',
                'Включите Меладзе! Откройте вино!',
                'На Марсе классно! Красные пески, крутые горы и кратеры...',
                '...ведь зелёный - мой любимый цвет! Зелёный - мой любимый цвет!',
            ],
        },
        'films': {
            'examples': [
                'Какие фильмы любишь?',
                'Что смотришь?',
                'Что посмотреть?',
                'Любимый фильм?',
                'Посоветуй фильм',
                'Какой фильм посмотреть?',
            ],
            'responses': [
                'Мистер робот',
                'Балто',
                'Лило и Стич',
                'Зов предков',
                'Собачья жизнь',
                'Как прогулять школу с пользой',
                'Легенда о волках',
                'Песнь моря',
                'Невероятная жизнь Уолтера Митти',
                'Пока не сыграл в ящик',
                'Кто я',
                'Бойцовский клуб',
                'Джентельмены',
                'Дорога перемен',
                'Остров проклятых',
                'Свадебный год',
                'Джули и Джулия',
                'Повар на колёсах',
                'Рататуй',
                'Адская кухня',
                'Беремнна в 16',
                'Чародейки',
                'Рик и Морти',
                'Один дома',
                'Чёрный лебедь',
                'Скотт Пилигрим против всех',                
            ],
        },
    },
}
