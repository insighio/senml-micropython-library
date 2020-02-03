import kpn_senml.cbor_encoder as cbor_encoder
import kpn_senml.cbor_decoder as cbor_decoder

from kpn_senml.senml_pack import SenmlPack

class SenmlPackCbor(SenmlPack):
    naming_map = {'bn': -2, 'bt': -3, 'bu': -4, 'bv': -5, 'bs': -16,
                  'n': 0, 'u': 1, 'v': 2, 'vs': 3, 'vb': 4, 'vd': 8, 's': 5, 't': 6, 'ut': 7}

    def __init__(self, name, callback=None):
        super().__init__(name, callback)

    def from_cbor(self, data):
        '''
        parse a cbor data byte array to a senml pack structure.
        :param data: a byte array.
        :return: None
        '''
        records = cbor_decoder.loads(data)  # load the raw senml data

        self._process_incomming_data(records, self.naming_map)

    def to_cbor(self):
        '''
        render the content of this object to a cbor byte array
        :return: a byte array
        '''
        converted = []
        self._build_rec_dict(self.naming_map, converted)
        return cbor_encoder.dumps(converted)
