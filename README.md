# Hermibox

This is my build of a [Phoniebox](https://phoniebox.de/) using a Raspberry Pi.

![Hermibox Photo](/photo.jpg)

## Shopping list

* Police bus: [small foot 11459 Großer Polizeibus aus Holz](https://amzn.eu/d/8CYERZg)
* Raspberry Pi: I used a Raspberry Pi 3 model B
* TBD document the other parts

## Test RFID Reader

Connect the RFID-RC522 module and follow the instructions from [PiMyLifeUp](https://pimylifeup.com/raspberry-pi-rfid-rc522/).

Test out writing to a tag:

    python3 write.py

Test out reading a tag:

    python3 read.py

Test out reading just the id of a tag (certain tags give me an Auth error when trying to read/write text, but reading just the id works fine):

    python3 read_id.py

# GPIO (Button) configuration

According to: https://github.com/MiczFlor/RPi-Jukebox-RFID/blob/develop/components/gpio_control/README.md

My settings: [gpio_settings.ini](gpio_settings.ini)
