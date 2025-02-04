# TARS

**about:** a minimalist project that converts typed text into morse code

**hardware:** raspberry pi pico, 16x2 I2C LCD, jumper wires
 
**setup:**<br>
<img height='200' width="280" alt="Screenshot 2025-02-03 at 23 59 07" src="https://github.com/user-attachments/assets/e9e14705-2bf2-4bf2-85bd-de426e02260c" /><br>
upload `main.py` and `pico_i2c_lcd.py` to the pico

**usage:**
type any text in the console, the first line of the LCD shows your i/p, while the second line displays the morse code translation & the LED blinks **dots(200ms)**, **dashes(600ms)** accordingly
