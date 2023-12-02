
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

  def __init__(self, bark_sound = '', bite_sound = '', sniff_sound = ''):
    self.suara_bark = bark_sound or self.suara_bark
    self.suara_bite = bite_sound or self.suara_bite
    self.suara_sniff = sniff_sound or self.suara_sniff
  
  def bark(self, bark_sound = ''):
    print(bark_sound or self.suara_bark)

  def change_bark_sound(self, new_bark_sound):
    self.suara_bark = new_bark_sound

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

# doggy.bark() # barking
# doggy.bark() # barking
# doggy.change_bark_sound('barking 2')
# doggy.bark() # barkinggggg
# doggy.bark() # barkinggggg
# doggy.bark() # barkinggggg
# doggy.bark() # barkinggggg
# doggy.bark() # barkinggggg

doggy.bark('asdadsads')
doggy.bark()
