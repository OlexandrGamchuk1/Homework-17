def geometric_progressions(start, stop, law):
    while start < stop:
        product = start * law
        if product == 'exit':
            exit()
        else:
            yield product
        start *= law

def my_multiplier(multiplier):
    if isinstance(multiplier, int):
        return multiplier


my_function = my_multiplier(3)
prog = geometric_progressions(1, 19, my_function)
print(next(prog))
print(next(prog))
prog.send('exit')
print(next(prog))