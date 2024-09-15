
class CacheSimples(Memoria):
    def __init__(self, kc, ram):
        Memoria.__init__(self, ram.capacidade())
        self.ram = ram
        self.cache_sz = 2**kc
        self.dados = [0] * self.cache_sz
        self.bloco = -1
        self.modif = False

    def read(self, ender):
        if self.cache_hit(ender):
            print("cache hit:", ender)
        else:
            print("cache miss:", ender)
            bloco_ender = int(ender/self.cache_sz)
            if self.modif:
                # update ram
                for i in range(self.cache_sz):
                    self.ram.write(bloco_ender * self.cache_sz + i, self.dados[i])
            # update cache
            for i in range(self.cache_sz):
                self.dados[i] = self.ram.read(bloco_ender * self.cache_sz + i)
            self.bloco = bloco_ender
            self.modif = False
        return self.dados[ender % self.cache_sz]

    def write(self, ender, val):
        if self.cache_hit(ender):
            print("cache hit:", ender)
        else:
            print("cache miss:", ender)

            # complete!
            # ...

        self.dados[ender % self.cache_sz] = val
        self.modif = True

    def cache_hit(self, ender):
        bloco_ender = int(ender/self.cache_sz)
        return bloco_ender == self.bloco
