# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://dpronline.delaware.gov/mylicense%20weblookup/Details.aspx?agency_id=1&license_id=240508&")


# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
name = root.cssselect("#_ctl21__ctl1_license_no")
#
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data={"name": name})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
