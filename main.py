from datetime import datetime


def path_logger(path):
    def logger(function):
        def new_function(*args, **kwargs):
            result = f'Время вызова функции: {datetime.now()}\n'\
                     f'Имя функции: {function.__name__}\n'\
                     f'Аргументы: {args}, {kwargs}\n'\
                     f'Возвращаемое значение: {function(*args, **kwargs)}'
            with open(path, 'w', encoding='utf-8') as file:
                file.write(result)
            return result
        return new_function
    return logger


