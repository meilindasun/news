import newspaper

def buildSource(url):
  return newspaper.build(url, memoize_articles = False)

keyword_freq = {} # dictionary <keyword, frequency>
def appendKeyword(source):
  for article in source.articles:
    # print(article.url)
    article.download()
    article.parse()
    article.nlp()
    for keyword in article.keywords:
      if keyword in keyword_freq.keys():
        # print("old")
        keyword_freq[keyword] += 1
      else:
        # print("new")
        keyword_freq[keyword] = 1 

def printKeywordFreq():
  for k, v in keyword_freq.items():
    print(k, v)

# quicksort keyword_freq in descending order by frequency
# so we can display the top X most frequent topics
def quicksort(start, end): # start, end inclusive
  pivot = (start + end) / 2
  left = start
  right = end
  while (left < right):
    if (keyword_freq.values()[left] >= keyword_freq.values()[pivot]):
      left += 1
    if (keyword_freq.values()[right] >= keyword_freq.values()[pivot]):
      right -= 1
  swap


appendKeyword(buildSource('http://bbc.co.uk'))
print("done")
printKeywordFreq()
