from led import Led

def test_init_led():
    led1 = Led(1)
    assert not led1.get_state()

def test_led_on():
    led1 = Led(1)
    led1.on()
    assert led1.get_state()

def test_led_toggle():
    led1 = Led(1)
    led1.toggle()
    assert led1.get_state()
    led1.toggle()
    assert not led1.get_state()
