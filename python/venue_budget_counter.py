venues = [
    {"name": "Fort Santiago", "price_tier": "Free"},
    {"name": "Manila Ocean Park", "price_tier": "$$$"},
    {"name": "Rizal Park", "price_tier": "Free"},
    {"name": "National Museum", "price_tier": "Free"},
    {"name": "Binondo Food Crawl", "price_tier": "$$"},
    {"name": "Intramuros Cafe", "price_tier": "$$"},
    {"name": "Intramuros Cafe", "price_tier": "$$$$"},
    {"name": "Intramuros Cafe", "price_tier": "$$$$"},
]

# Initialize an empty dictionary to store our category tallies
counts = {}

# Iterate through each venue dictionary inside the venues list
for venue in venues:
    # Isolate the target metric we want to count (the price tier)
    tier = venue["price_tier"]

    # IF the tier is already a key in our 'counts' dictionary...
    if tier in counts:
        # Increment its existing tally by 1
        counts[tier] += 1
    # ELSE, this is the first time we are seeing this tier...
    else:
        # Create the key in the dictionary and initialize its value to 1
        counts[tier] = 1

# Output the final dictionary showing the accumulated totals
print(counts)