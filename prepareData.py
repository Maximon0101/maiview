def prepareScheduleDay(day: dict):
    day["date"]["month"] = prepareMonth(day["date"]["month"])
    day["day"] = prepareDayOfWeek(day["day"])
    day["lessons"] = list(map(prepareLesson, day["lessons"]))
    return day


def prepareMonth(num: int):
    months = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября',
              'Декабря']
    return months[num - 1]


def prepareDayOfWeek(day: str):
    days = {'Пн': 'Понедельник', 'Вт': 'Вторник', 'Ср': 'Среда', 'Чт': 'Четверг', 'Пт': 'Пятница', 'Сб': 'Суббота',
            'Вс': 'Воскресенье'}
    return days[day]

def prepareLesson(lesson: dict):
    lesson['time_start']['time'] = lesson['time_start']['time'][:-3]
    lesson['time_end']['time'] = lesson['time_end']['time'][:-3]
    return lesson