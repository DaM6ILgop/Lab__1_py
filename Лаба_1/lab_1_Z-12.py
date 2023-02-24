def get_frames(signal, size, overlap):
    step = int(size * (1 - overlap))
    for i in range(0, len(signal) - size + 1, step):
        yield signal[i:i+size]


signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 4
overlap = 0.5

for frame in get_frames(signal, size, overlap):
    print(frame)


#Определяем функцию get_frames с параметрами signal, size и overlap.
#Рассчитываем шаг, используя значение size и overlap. Шаг равен целочисленному значению произведения size на (1 - overlap).
#Для всех фрагментов сигнала длиной size, начиная с 0-го элемента, увеличивая индекс на шаг до len(signal)-size+1, создаем срез сигнала, начиная с текущего индекса и заканчивая индексом + size.
#Срез добавляем в генератор yield, который возвращает текущий фрагмент сигнала.
#В основной программе определяем список сигнала signal, размер фрагмента size и степень перекрытия overlap.
#В цикле for проходим по фрагментам, возвращаемым из функции get_frames сигнала signal, размером size и перекрытием overlap, и выводим их на экран.