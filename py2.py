# import smmrpy
# import asyncio
#
# s = smmrpy.SMMRPY('014E9A686E') # Instantiate the SMMRPY instance.
#
# # await
# article = asyncio.ensure_future(s.get_smmry('https://stackoverflow.com/questions/17049839/')) # Get the Article object.
# print(type(article))
# asyncio.wait(asyncio.Task.all_tasks())
# print(type(article))
# print(article.title) # Print the title of the found article.


# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 1


if __name__ == "__main__":
    #url = "http://www.cbc.ca/news/canada/kitchener-waterloo/justin-trudeau-hack-the-north-university-waterloo-tech-1.4292217"
    #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    parser = PlaintextParser.from_string("""Prime Minister Justin Trudeau will help open the Hack the North conference at the University of Waterloo Friday night.

Trudeau is scheduled to be part of the opening ceremonies and speak to the crowd at 8:30 p.m.

Hack the North brings more than 1,000 students from around the globe to the University of Waterloo campus for a 36 hour hack-a-thon.

Pokemon Go similar to game students created at UW competition in 2014
Health hack-a-thon in Kitchener to tackle problems faced by aging population
After the opening remarks by Trudeau there will be a fireside chat with Balaji Srinivasan, CEO of the website 21.co, which allows people to be paid with digital currency for doing small tasks, and Mike Gibson, an investor with the San Francisco-based 1517 Fund. They're expected to talk about the future of technology in Canada, Silicon Valley and beyond.

The event will also include a panel on diversity and inclusion in the tech sector.

The students will design hardware projects or mobile or web applications during the weekend and present them to a panel of industry experts Sunday morning. The top 14 teams will then present to an audience at 2 p.m. and compete for prizes.


""", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)