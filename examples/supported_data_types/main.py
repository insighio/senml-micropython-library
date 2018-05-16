# _  __  ____    _   _ 
# | |/ / |  _ \  | \ | |
# | ' /  | |_) | |  \| |
# | . \  |  __/  | |\  |
# |_|\_\ |_|     |_| \_|
# 
# (c) 2018 KPN
# License: GNU General Public License v3.0.
# Author: Jan Bogaerts
# 
# supported datatypes example

from kpn_senml import *
import utime as time
#import cbor2

pack = SenmlPack("device_name")

double_val = SenmlRecord("double", value=23.5)
int_val = SenmlRecord("int", value=23)
bool_val = SenmlRecord("bool", value=True)
str_val = SenmlRecord("str val", value="test")
bytes_val = SenmlRecord("bytes", value= bytearray(b'00 1e 05 ff'))

#invalid value
try:
    invalid = SenmlRecord("invalid", value={'a': 1})
except Exception as error:
    print(error)


pack.add(double_val)
pack.add(int_val)
pack.add(bool_val)
pack.add(str_val)
pack.add(bytes_val)

while True:
    print(pack.to_json())
    time.sleep(1)
#cbor_val = pack.to_cbor()
#print(cbor_val)
#print(cbor2.loads(cbor_val))