# Hermibox

This is my build of a [Phoniebox](https://phoniebox.de/) using a Raspberry Pi.

![Hermibox Photo](/photos/photo.jpg)

## Shopping list

* Police bus: [small foot 11459 Großer Polizeibus aus Holz](https://amzn.eu/d/8CYERZg)
* Raspberry Pi: I used a Raspberry Pi 3 model B
* RFID Module: [RC522](https://de.aliexpress.com/item/32672212005.html)
* Speakers: [Audiocore AC870 Kompakt Stereo-Lautsprecher 2.0 PC 2x3 Watt RMS](https://amzn.eu/d/bMhVWlB)
* Sound card: [JSAUX USB A auf 3.5mm Klinke Aux Adapter](https://amzn.eu/d/9CCRulK)
* Wooden figures: [Egurs Holzfiguren 10 Stück 75mm DIY Figuren](https://amzn.eu/d/erieEHS)
* NFC tags: [NFC Ntag215 Münze TAG Schlüssel 13,56 MHz 215 Kartenetikett RFID Ultraleichte Tags Etiketten 25 mm Durchmesser](https://de.aliexpress.com/item/1005002714885621.html)
* Buttons with LED: [LANBOO 16mm 1NO1NC 5Pin schwarz kunststoff push button switch mit LED 12V24V220V](https://de.aliexpress.com/item/4000350958846.html)
* Akku: USB Powerbank (10000mAh)

## Test RFID Reader

Connect the RFID-RC522 module and follow the instructions from [PiMyLifeUp](https://pimylifeup.com/raspberry-pi-rfid-rc522/).

Test out writing to a tag:

    python3 write.py

Test out reading a tag:

    python3 read.py

Test out reading just the id of a tag (certain tags give me an Auth error when trying to read/write text, but reading just the id works fine):

    python3 read_id.py

# GPIO (Button) configuration

According to: [Using GPIO hardware buttons](https://github.com/MiczFlor/RPi-Jukebox-RFID/wiki/Using-GPIO-hardware-buttons)

My settings: [gpio_settings.ini](gpio_settings.ini)

Note that I am using version 2 of the Phoniebox software (RPi-Jukebox-RFID), not the newer version 3.
