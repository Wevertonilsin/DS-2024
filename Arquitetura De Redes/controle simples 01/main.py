from machine import Pin,I2C
import ssd1306
import machine

botao = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
botao1 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(27, machine.Pin.OUT)

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
while True:
    verde = botao.value()
    macaco = botao1.value()
    if verde == 0:
        led.value(1)
        led2.value(0)
        tela.fill(0)
        tela.text('A Temperatura', 0, 0)
        tela.text('E de:', 0, 10)
        tela.text('20 graus', 0, 20)
        tela.show()
    if macaco == 0:
        led2.value(1)
        led.value(0)
        tela.fill(0)
        tela.text('A umidade ', 0, 0)
        tela.text('E de:', 0, 10)
        tela.text('10', 0, 20)
        tela.show()




