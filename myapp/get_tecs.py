import json

class Get_Techniques:
    def __init__(self, layer):
        self.layer = layer
        self.tecs = self.extraction()

    def extraction(self):
        result = []
        parsed = json.loads(self.layer)
        list = parsed.get("techniques")
        for l in list:
            if l.get("color") != "":
                if l.get("techniqueID") not in result:
                    result.append(l.get("techniqueID"))

        return result