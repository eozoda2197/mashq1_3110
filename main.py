class Talaba:
    def __init__(self, ism, id, kurs):
        self.ism = ism
        self.id = id
        self.kurs = kurs


class Universitet:
    def __init__(self):
        self.talabalar = []

    def talaba_qosh(self, talaba):
        self.talabalar.append(talaba)

    def kurs_talabalari(self, kurs):
        return [t for t in self.talabalar if t.kurs == kurs]
