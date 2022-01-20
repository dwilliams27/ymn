import random

fname_pre = [
  'Jim',
  'Bri',
  'Bon',
  'Blip',
  'Glon',
  'Mip',
  'Shla',
  'Han',
  'Erm',
  'Blat'
]

fname_post = [
  'bo',
  'mus',
  'ton',
  'mack',
  'dan',
  'is',
  'bert',
  'ackle',
  'toose',
  'ible',
  'lop'
]

lname_pre = [
  'Will',
  'Tent',
  'Nob',
  'Lob',
  'Dob',
  'As',
  'Ash',
  'Pick',
  'Wat',
  'Crip',
  'Vit',
  'Man',
  'Flip',
  'Auck'
]

lname_post = [
  'ton',
  'son',
  'bourne',
  'bern',
  'stern',
  'ock',
  'eemus',
  'ent',
  'alty'
]

superlative = [
  'the Great',
  'the Cunning',
  'the Wise',
  'the Conquerer',
  'the Short',
  'the Pensive',
  'the Magnificent',
  'the Desperate',
  'the Triumphant',
  'the Elder',
  'the Warrior',
  'the Younger'
]

class NameFactory:
  @staticmethod
  def generateName():
    name = fname_pre[random.randrange(len(fname_pre))] + fname_post[random.randrange(len(fname_post))] + \
      ' ' + lname_pre[random.randrange(len(lname_pre))] + lname_post[random.randrange(len(lname_post))]
    if(random.randrange(100) > 90):
      name += f' {superlative[random.randrange((len(superlative)))]}'
    return name
