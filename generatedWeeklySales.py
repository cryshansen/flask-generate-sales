#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 15:44:03 2025
App creates fake data saves to realistic_weekly_sales_data.csv v1 final
@author: crystalhansen
"""
from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta




def get_shoot_day_and_time(photo_type):
    if photo_type == 'Wedding':
        day = random.choices(['Saturday', 'Friday', 'Sunday'], weights=[0.7, 0.2, 0.1])[0]
        time = random.choice(['11:00', '14:00', '17:00', '19:00'])
    elif photo_type == 'Portrait':
        day = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        time = random.choice(['10:00', '13:00', '16:30', '18:30'])  # Include golden hour
    elif photo_type == 'Event':
        day = random.choice(['Thursday', 'Friday', 'Saturday', 'Sunday'])
        time = random.choice(['12:00', '15:00', '19:00'])
    elif photo_type == 'Real Estate':
        day = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        time = random.choice(['09:30', '11:00', '13:30'])
    elif photo_type == 'Product':
        day = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        time = random.choice(['10:00', '12:00', '14:00'])
    else:  # Stock License
        day = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        time = random.choice(['11:00', '15:00', '17:00'])

    return day, time




# Setup
fake = Faker()
Faker.seed(42)
random.seed(42)

# Weekly range
today = datetime.today()
start_of_week = today - timedelta(days=today.weekday())  # Monday

# Weights by weekday (Mon=0, Sun=6)
weekday_weights = [0.08, 0.10, 0.10, 0.12, 0.15, 0.25, 0.20]

# Photo type setup
photo_types_na = [
    ('Wedding', (1500, 3000), 0.30),
    ('Portrait', (150, 400), 0.25),
    ('Event', (300, 1200), 0.20),
    ('Real Estate', (100, 600), 0.10),
    ('Product', (200, 800), 0.10),
    ('Stock Photo License', (25, 75), 0.05)
]
categories, price_ranges, weights = zip(*photo_types_na)
category_price_map = {cat: price_range for cat, price_range, _ in photo_types_na}
countries_na = ['United States', 'Canada']

# Regenerate 2000 rows of data focused on North America (U.S. and Canada)
us_states = [
    "California", "Texas", "Florida", "New York", "Illinois", "Pennsylvania", "Ohio",
    "Georgia", "North Carolina", "Michigan", "New Jersey", "Virginia", "Washington",
    "Arizona", "Massachusetts", "Tennessee", "Indiana", "Missouri", "Maryland", "Wisconsin"
]

canadian_provinces = [
    "Ontario", "Quebec", "British Columbia", "Alberta", "Manitoba", "Saskatchewan", "Nova Scotia"
]




payment_methods_na = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash', 'Apple Pay']
referral_sources = ['Google Search', 'Instagram', 'Facebook', 'Referral', 'Direct Visit', 'Email Campaign']
customer_segments = ['New Customer', 'Returning Customer', 'Business Client', 'Occasional Buyer']

# Generate records
na_data = []
for _ in range(2000):
    category = random.choices(categories, weights=weights, k=1)[0]
    price_range = category_price_map[category]
    price = round(random.uniform(*price_range), 2)

    # Pick a day of the week using realistic weights
    day_offset = random.choices(range(7), weights=weekday_weights, k=1)[0]
    purchase_date = start_of_week + timedelta(days=day_offset)
    shoot_day, shoot_time = get_shoot_day_and_time(category)
    country = random.choice(['United States', 'Canada'])
    if country == 'United States':
        region = random.choice(us_states)
        city = fake.city()
    else:
        region = random.choice(canadian_provinces)
        city = fake.city()

    
    
    
    
    
    na_data.append({
        'customer_name': fake.name(),
        'email': fake.email(),
        'industrytype': category,
        'purchasedate': purchase_date.date(),
        'month': purchase_date.strftime('%Y-%m'),
        'city': city,
        'region': region,
        'country': country,
        'price_USD': price,
        'payment_method': random.choice(payment_methods_na),
        'referral_source': random.choice(referral_sources),
        'customer_segment': random.choices(
            customer_segments, weights=[0.5, 0.2, 0.2, 0.1], k=1
        )[0],
        'shoot_day': shoot_day,
        'shoot_time': shoot_time
    })

#customer_name,email,industrytype,purchasedate,month,city,region,country,price_USD,payment_method,referral_source,customer_segment,shoot_day,shoot_time

# Save it
df_na = pd.DataFrame(na_data)
realistic_weekly_path = "realistic_weekly_sales_data.csv"
df_na.to_csv(realistic_weekly_path, index=False)

print("Generated realistic weekly sales:", realistic_weekly_path)

