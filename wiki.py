import wikipediaapi

def get_city_info (city="marrakech"):
	wiki_wiki = wikipediaapi.Wikipedia('en')
	page_py = wiki_wiki.page(city)
	return page_py.summary[0:300]