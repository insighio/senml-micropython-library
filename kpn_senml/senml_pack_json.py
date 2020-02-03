import ujson
from kpn_senml.senml_pack import SenmlPack

class SenmlPackJson(SenmlPack):
    naming_map = {'bn': 'bn', 'bt': 'bt', 'bu': 'bu', 'bv': 'bv', 'bs': 'bs',
                      'n': 'n', 'u': 'u', 'v': 'v', 'vs': 'vs', 'vb': 'vb', 'vd': 'vd', 's': 's', 't': 't', 'ut': 'ut'}

    def __init__(self, name, callback=None):
        super().__init__(name, callback)


    def from_json(self, data):
        '''
        parse a json string and convert it to a senml pack structure
        :param data: a string containing json data.
        :return: None, will r
        '''
        records = ujson.loads(data)                                              # load the raw senml data
        self._process_incomming_data(records, self.naming_map)


    def to_json(self):
        '''
        render the content of this object to a string.
        :return: a string representing the senml pack object
        '''
        converted = []
        self._build_rec_dict(self.naming_map, converted)
        return ujson.dumps(converted)
