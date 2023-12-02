
# Initialize Class
class Hewan:
  def nafas(self):
    print('hufft')

  def tidur(self):
    print('Zzzzz')

  def makan(self):
    print('Nyam nyam')
  
  def minum(self):
    print('Gluk gluk')

class Anjing(Hewan):
  suara_bark = 'woof'
  suara_bite = 'Rabies'
  suara_sniff = 'Emmmm'
  
  def bark(self):
    print(self.suara_bark)

  def bite(self):
    self.bark()
    self.sniff()
    print(self.suara_bite)

  def sniff(self):
    print(self.suara_sniff)

class Kucing(Hewan):
  def meow(self):
    print('Meowwwww')


# Running
doggy = Anjing()
miawaug = Kucing()

doggy.bite()
