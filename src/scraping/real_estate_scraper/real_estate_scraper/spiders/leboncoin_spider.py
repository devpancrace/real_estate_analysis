import scrapy


# Define the spider class for scraping Leboncoin listings
class LeboncoinSpider(scrapy.Spider):
    name = "leboncoin"  # The name of the spider (used to run it from the command line)
    start_urls = [
        "https://www.leboncoin.fr/immobilier/offres"
    ]  # The URL to start the scraping process

    # The parse method will be called to handle the response from the start URL
    def parse(self, response):
        # Iterate over each listing element found on the current page
        for listing in response.css("div._2h9yZ"):
            yield {
                # Extract the title of the listing
                "title": listing.css("p._2tubl::text").get(),
                # Extract the price of the listing
                "price": listing.css("span._1Cf1Z::text").get(),
                # Extract the location of the listing
                "location": listing.css("p._2VAnh::text").get(),
                # Extract the URL of the listing
                "url": listing.css("a::attr(href)").get(),
            }

        # Look for the "Next" button on the page to fetch the next page's URL
        next_page = response.css('a[rel="next"]::attr(href)').get()

        # If a "Next" page exists, follow the link and call the parse method again
        if next_page:
            yield response.follow(next_page, self.parse)
