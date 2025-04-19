from pytrends.request import TrendReq

def get_trending_keywords(region="AE"):
    pytrends = TrendReq(hl='en-US', tz=300)

    seed_keywords = ["Dubai Real Estate", "Ras Al Khaimah Property"]
    keywords = []

    try:
        pytrends.build_payload(kw_list=seed_keywords, geo=region)
        data = pytrends.related_queries()

        for key in data:
            if data[key]['top'] is not None:
                keywords += [x['query'] for x in data[key]['top'].head(5).to_dict('records')]

        if not keywords:
            raise ValueError("No keywords found — using fallback.")

    except Exception as e:
        print(f"⚠️ Error fetching from Google Trends: {e}")
        keywords = [
            "Investing in Dubai Real Estate",
            "Luxury villas in Ras Al Khaimah",
            "Golden Visa properties UAE",
            "Off-plan projects in Dubai",
            "Beachfront apartments RAK"
        ]

    return list(set(keywords))
