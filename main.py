import machine
import utime
import gc
from sys import stdin
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
# ========== HARDWARE SETUP ==========
I2C_ADDR = 0x27 
I2C_SDA_PIN = 0
I2C_SCL_PIN = 1
LED_PIN = 15
UNIT_TIME = 200  # Morse code timing base (ms)

# ========== MORSE CODE SYSTEM ==========
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': ' '
}
        
def text_to_morse(text):
    converted = []
    for char in text.upper():
        if char in MORSE_CODE:
            converted.append(MORSE_CODE[char])
    return ' '.join(converted)

def pad_string(s, length):
    # Custom string padding replacement for ljust()
    if len(s) < length:
        return s + ' ' * (length - len(s))
    return s[:length]

def transmit_morse(code):
    for symbol in code:
        if lcd:
            display_text = "morse is " + pad_string(code, 12)
            lcd.move_to(0, 1)
            lcd.putstr(display_text)
            
        if symbol == '.':
            led.on()
            utime.sleep_ms(UNIT_TIME)
            led.off()
            utime.sleep_ms(UNIT_TIME)
        elif symbol == '-':
            led.on()
            utime.sleep_ms(UNIT_TIME * 3)
            led.off()
            utime.sleep_ms(UNIT_TIME)
        elif symbol == ' ':
            utime.sleep_ms(UNIT_TIME * 3)

# ========== MAIN PROGRAM ==========
print("Morse Code Translator Ready")
if lcd:
    lcd.clear()
    lcd.putstr("i'm TARS")
    lcd.move_to(0, 1)
    lcd.putstr("waiting for i/p")

while True:
    try:
        message = stdin.readline().strip()
        if message:
            if lcd:
                lcd.clear()
                lcd.putstr(pad_string(message[:16], 16))
                lcd.move_to(0, 1)
                lcd.putstr("converting i swear")
            
            morse = text_to_morse(message)
            
            if lcd:
                lcd.clear()
                lcd.putstr(pad_string(message[:16], 16))
                lcd.move_to(0, 1)
                lcd.putstr(pad_string(morse[:16], 16))
            
            for code in morse.split(' '):
                transmit_morse(code)
                utime.sleep_ms(UNIT_TIME * 2)
            
            utime.sleep_ms(UNIT_TIME * 4)
            if lcd:
                lcd.clear()
                lcd.putstr("i'm ready for")
                lcd.move_to(0, 1)
                lcd.putstr("next word nerd")
                
    except KeyboardInterrupt:
        if lcd:
            lcd.clear()
            lcd.putstr("bye.")
            utime.sleep(2)
            lcd.hal_backlight_off()
        break
    except Exception as e:
        print("error:", e)
        if lcd:
            lcd.clear()
            lcd.putstr("oops, error occurred")
        break
