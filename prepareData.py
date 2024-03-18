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
    lessonStartTimeList = ['9:00', '10:45', '13:00', '14:45', '16:30', '18:15', '20:00']
    lessonTypeList = {'ЛК': 'ЛЕКЦИЯ', 'ПЗ': 'СЕМИНАР', 'ЛР': 'ЛАБОРАТОРНАЯ', 'Экзамен': 'ЭКЗАМЕН'}
    lesson['time_start']['time'] = lesson['time_start']['time'][:-3]
    lesson['time_end']['time'] = lesson['time_end']['time'][:-3]
    lesson['number'] = lessonStartTimeList.index(lesson['time_start']['time']) + 1
    lesson['type'] = lessonTypeList[lesson['type']]
    lesson['rooms'] = ' / '.join(list(map(lambda x: x['name'], lesson['rooms'])))
    return lesson