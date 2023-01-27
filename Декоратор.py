def simple_decorator(func):
    def decorated_function(*args, **kwargs):
        print("Input:")
        print("Positional:", args)
        print("Named:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        
        return result
    return decorated_function

@simple_decorator
def root(value, n=2):
    result = value ** (1/n)
    return result    
print(root(32))    



from time import time
 
# Декоратор, который возвращает декоратор. Он принимает число
# запусков декорируемой функции для усреднения времени
def time_runs(n_runs):
    # Декоратор, который уже будет возвращать непосредственно
    # декорированную функцию
    def time_decorator(func):
        # Функция, в которой непосредственно
        # происходит запуск основной функции
        def decorated_func(*args, **kwargs):
            start = time()
            # Запускаем основную функцию столько раз,
            # сколько передано в n_runs
            for i in range(n_runs):
                result = func(*args, **kwargs)
            end = time()
            # Считаем разницу во времени
            delta = end - start
            # Делим разницу на число запусков, чтобы получить
            # среднее время одного запуска
            mean_time = delta / n_runs
            # Печатаем полученное среднее время
            print("Mean runtime:", mean_time)
            # Не забываем вернуть сам результат
            return result
        # Возвращаем функцию, в которой происходит запуск основной функции
        return decorated_func
    # Возвращаем декоратор, который будет применяться к функции
    return time_decorator


def logger (name):
    def decorator(func):
        def decorated_funk (*args, **kwargs):
            print(name + ':' , 'Function', func.__name__ , 'finished')
            result = func(*args , **kwargs)
            print(name + ':' , 'Function', func.__name__ , 'started')
            return result
        return decorated_funk
    return decorator    
   
@logger('MainLogger')
def root(val, n=2):
    res = val ** (1/n)
    return res
 
print(root(25))
