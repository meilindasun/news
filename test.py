import newspaper
bbc_paper = newspaper.build('http://bbc.co.uk', memoize_articles = False)
bbc_paper.articles[0].download()
bbc_paper.articles[0].parse()
bbc_paper.articles[0].nlp()
print(bbc_paper.articles[0].text)
print(bbc_paper.articles[0].keywords)
print("------")
for category in bbc_paper.category_urls():
  print(category)
