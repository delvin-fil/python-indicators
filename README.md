# python-indicators
<hr>
Индикатор раскладки и клавиш Num и Caps для Conky

![Screenshot](https://github.com/delvin-fil/python-indicators/blob/master/screenshot.png)

Для нормальной работы индиктора требуются программы **skb** и **xsetleds**

Работает в python2.7 и python3.4

Установка
1. git clone https://github.com/delvin-fil/python-indicators.git
<br>Или<br>
Скачать и распаковывать архив в произвольный каталог.
2. Добавть в .conkyrc в блоке conky.text следующее:
    ${execp /patch_to_progs/num.py}
3. Настроить значение image
