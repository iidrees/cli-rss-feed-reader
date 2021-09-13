import feedparser




rss_links = input("Kindly paste your RSS link here, if you have more than one link, kindly separate each link with a comma: ")

split_link = rss_links.split(",")




for link in split_link:
    # print(link, "\n\n")
    rss_response = feedparser.parse(link)

    # print("\n\n",rss_response['entries'][0],"\n\n", "link>>:" + rss_response['feed']['link'] )

    for value in rss_response['entries']:
        # print("New entry >>>>>>",value, "\n\n")

        if 'summary' in value:
            print(
                "Below are the recent feeds from your RSS Link.\n",
                "Title: " + value['title'] +"\n",
                "Link: " + value['id'] +"\n",
                "description: " + value['summary'] +"\n",

            )
        else:
            print(
                "Below are the recent feeds from your RSS Link.\n",
                "Title: " + value['title'] +"\n",
                "Link: " + value['id'] +"\n",
                "description: " + value['title_detail'].value +"\n",

            )


# links 
# http://rss.cnn.com/rss/edition.rss
# http://rss.cnn.com/rss/edition_africa.rss
# http://feeds.bbci.co.uk/news/rss.xml?edition=uk#
# https://feeds.skynews.com/feeds/rss/world.xml