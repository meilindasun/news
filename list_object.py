import newspaper

def buildSource(url):
  return newspaper.build(url, memoize_articles = False)

class KeyFreq:
  def __init__(self, word, freq):
    self.word = word
    self.freq = freq

keyInfo = [] # stores KeyFreq objects 
def appendKeyword(source):
  for article in source.articles:
    article.download()
    article.parse()
    article.nlp()
    for keyword in article.keywords:
      print (keyword)
      if len(keyInfo) <= 0:
        print("  CASE 1")
        lim = 1
      else:
        print("  CASE 2")
        lim = len(keyInfo)
      i = 0
      print("  LENGTH IS", len(keyInfo))
      print("  HERE")
      while i < lim:
        print ("  ", i)
        if (keyword == keyInfo[i].word):
          print("  CASE A")
          keyInfo[i].freq += 1
        else:
          print("  CASE B")
          keyInfo.append(KeyFreq(keyword, 1))
        i += 1

def printKeyInfo():
  print("trying to print Key Info")
  for i in range(len(keyInfo)):
    print(keyInfo[i].word, keyInfo[i].freq)

def quicksort(start, end):
  if start == end:
    return
  pivot = (start + end) / 2
  left = start
  right = end
  while (left < right):
    if (keyword_freq.values()[left] >= keyword_freq.values()[pivot]):
      left += 1
    if (keyword_freq.values()[right] >= keyword_freq.values()[pivot]):
      right -= 1

appendKeyword(buildSource('http://bbc.co.uk'))
print("source built")
printKeyInfo()
