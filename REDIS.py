import redis  # импортируем библиотеку

red = redis.Redis(
    host='redis-15184.c268.eu-west-1-2.ec2.cloud.redislabs.com',
    # ваш хост, если вы поставили Redis к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь
    # на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
    port=15184,
    # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт
    # всегд разный, по этому его надо копировать оттуда же, что и host.
    password='BqVisj5K9R06hAyK95j2C6LwoqkHQyKb'
    # для локальной машины пароль не требуется (если вы устанавливали Redis к себе на
    # компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей
    # облачного сервиса пароль находится в вашей облачной базе данных в поле password.
)
# red.set('var1','value')
print(red.get('var1'))