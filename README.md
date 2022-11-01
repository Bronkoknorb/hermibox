# Hermibox

I am building my own Phoniebox using a Raspberry Pi.

## Test RFID Reader

Connect the RFID-RC522 module and follow the instructions from [PiMyLifeUp](https://pimylifeup.com/raspberry-pi-rfid-rc522/).

Test out writing to a tag:

    python3 write.py

Test out reading a tag:

    python3 read.py

Test out reading just the id of a tag (certain tags give me an Auth error when trying to read/write text, but reading just the id works fine):

    python3 read_id.py
