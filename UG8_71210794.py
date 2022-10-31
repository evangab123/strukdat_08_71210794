class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 
    def __init__(self):
       self._data = []
       self._size = 0
       self._max = Kasir.DEFAULT_CAPACITY

    def __len__(self): 
        return self._size

    def is_empty(self):
        return self._size == 0

    def dequeue(self): 
        data = self._data[0]
        self._data.remove(data)
        print("### Pelanggan",data,"Selesai Membayar ### \n")

    def enqueue(self, namaPelanggan): 
        self._data.append(namaPelanggan)

    def resize(self, cap): 
        self._max = self._max * cap
        print("### Melakukan Rezise ###\n")
        
    
    def printAll(self): 
        if len(self._data) > self._max:
                self.resize(2)
        print("=== Kasir ===")
        panjang = len(self._data)-1
        count = 1
        for i in range(0, (self._max)):            
            if i <= panjang:
                print(str(count)+".",self._data[i], end=' ')
                print()
            else:
                print(str(count)+". Kosong")
            count += 1
        print(" ")

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

