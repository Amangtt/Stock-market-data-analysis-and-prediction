import pandas as pd


# Function to count unique domains
def count_unique_domains(df):
    domain_count = {}

    for publisher in df["publisher"]:
        if "@" in publisher:  # Checking if its an email
            domain = publisher.split("@")[-1]
            domain_count[domain] = domain_count.get(domain, 0) + 1

    return domain_count


