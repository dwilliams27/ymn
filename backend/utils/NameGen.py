import random

vowels = [
  'a',
  'e',
  'i',
  'o',
  'u'
]

doublers = [
  'r',
  't',
  'p',
  'd',
  'g',
  'l',
  'z',
  'c',
  'b',
  'n',
  'm'
]

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
  'alty',
  'ustaus',
  'umber',
  'atto'
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
  'the Younger',
  'the Traitor',
  'the Vile',
  'the Beloved',
  'the Hated',
  'the Terrible',
  'the Diseased',
  'the Generous',
  'the Unlucky'
]

class NameFactory:
  @staticmethod
  def generateName():
    fname1 = fname_pre[random.randrange(len(fname_pre))]
    fname2 = fname_post[random.randrange(len(fname_post))]
    if(fname1[-1] in doublers and fname2[0] in vowels):
      fname1 += fname1[-1]

    name = fname1 + fname2 + \
      ' ' + lname_pre[random.randrange(len(lname_pre))] + lname_post[random.randrange(len(lname_post))]
    if(random.randrange(100) > 80):
      name += f' {superlative[random.randrange((len(superlative)))]}'
    return name
