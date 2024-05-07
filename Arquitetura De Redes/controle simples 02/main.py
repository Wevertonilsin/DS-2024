import machine
import time 
import ssd1306

# botões de controle
btn_vermelho = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
btn_verde = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# botões de navegação
btn_cima = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
btn_baixo = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# LEDs
led_desligado = machine.Pin(26, machine.Pin.OUT)
led_ligado = machine.Pin(27, machine.Pin.OUT)

# Tela
largura = 128
altura = 64
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
tela = ssd1306.SSD1306_I2C(largura, altura, i2c)

qual_tela = 1
status_iluminacao = "OFF"
status_arcondicionado = "OFF"
status_portaoprincipal = "OFF"
status_cameras = "OFF"

while True:

    if btn_cima.value() == 0 and qual_tela >= 2:
        qual_tela -= 1
        print("Botão Cima OK")
    
    if btn_baixo.value() == 0 and qual_tela <= 3:
        qual_tela += 1
        print("Botão Baixo OK")

    print(qual_tela)
    
    if qual_tela == 1:
        
        if btn_vermelho.value() == 0:
            status_iluminacao = "OFF"
            print("Botão vermelho OK")
    
        if btn_verde.value() == 0:
            status_iluminacao = "ON"
            print("Botão Verde OK")
        
        tela.fill(0)
        tela.text("ILUMINACAO", 0, 0)
        #tela.text("STATUS:", 0, 25)
        if status_iluminacao == "OFF":
            tela.text("STATUS: OFF", 0, 25)
            led_desligado.value(1)
            led_ligado.value(0)
        elif status_iluminacao == "ON":
            tela.text("STATUS: ON", 0, 25)
            led_desligado.value(0)
            led_ligado.value(1)
        tela.text("[1/4]", 0, 50)
        tela.show()
    
    elif qual_tela == 2:

        if btn_vermelho.value() == 0:
            status_arcondicionado = "OFF"
            print("Botão vermelho OK")
    
        if btn_verde.value() == 0:
            status_arcondicionado = "ON"
            print("Botão Verde OK")

        tela.fill(0)
        tela.text("AR CONDICIONADO", 0, 0)
        #tela.text("STATUS:", 0, 25)
        if status_arcondicionado == "OFF":
            tela.text("STATUS: OFF", 0, 25)
            led_desligado.value(1)
            led_ligado.value(0)
        elif status_arcondicionado == "ON":
            tela.text("STATUS: ON", 0, 25)
            led_desligado.value(0)
            led_ligado.value(1)
        tela.text("[2/4]", 0, 50)
        tela.show()

    elif qual_tela == 3:

        if btn_vermelho.value() == 0:
            status_portaoprincipal = "OFF"
            print("Botão vermelho OK")
    
        if btn_verde.value() == 0:
            status_portaoprincipal = "ON"
            print("Botão Verde OK")

        tela.fill(0)
        tela.text("Portao P", 0, 0)
        #tela.text("STATUS:", 0, 25)
        if status_portaoprincipal == "OFF":
            tela.text("STATUS: OFF", 0, 25)
            led_desligado.value(1)
            led_ligado.value(0)
        elif status_portaoprincipal == "ON":
            tela.text("STATUS: ON", 0, 25)
            led_desligado.value(0)
            led_ligado.value(1)
        tela.text("[3/4]", 0, 50)
        tela.show()
    
    elif qual_tela == 4:

        if btn_vermelho.value() == 0:
            status_cameras = "OFF"
            print("Botão vermelho OK")
    
        if btn_verde.value() == 0:
            status_cameras = "ON"
            print("Botão Verde OK")

        tela.fill(0)
        tela.text("Cameras", 0, 0)
        #tela.text("STATUS:", 0, 25)
        if status_cameras == "OFF":
            tela.text("STATUS: OFF", 0, 25)
            led_desligado.value(1)
            led_ligado.value(0)
        elif status_cameras == "ON":
            tela.text("STATUS: ON", 0, 25)
            led_desligado.value(0)
            led_ligado.value(1)
        tela.text("[4/4]", 0, 50)
        tela.show()
    time.sleep(0.1)