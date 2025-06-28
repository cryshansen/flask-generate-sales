#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 14:35:30 2025

@author: crystalhansen
"""
from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta


def get_seasonal_weights(month):
    # Simplified month-to-season map
    spring = ['03', '04', '05']
    summer = ['06', '07', '08']
    fall   = ['09', '10', '11']
    winter = ['12', '01', '02']

    if month in spring:
        return [0.35, 0.25, 0.15, 0.10, 0.10, 0.05]  # Weddings & Portraits
    elif month in summer:
        return [0.40, 0.20, 0.20, 0.05, 0.10, 0.05]  # Peak Wedding/Event season
    elif month in fall:
        return [0.30, 0.30, 0.15, 0.10, 0.10, 0.05]  # Portrait/Real Estate
    else:  # Winter
        return [0.10, 0.35, 0.10, 0.15, 0.20, 0.10]  # Studio/Product shoots


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




# Initialize Faker and seed
fake = Faker()
Faker.seed(42)
random.seed(42)

# Photo categories and weights for NA
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
payment_methods_na = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash', 'Apple Pay']
referral_sources = ['Google Search', 'Instagram', 'Facebook', 'Referral', 'Direct Visit', 'Email Campaign']
customer_segments = ['New Customer', 'Returning Customer', 'Business Client', 'Occasional Buyer']

purchase_date = fake.date_between(start_date='-7d', end_date='today')
month_str = purchase_date.strftime('%m')


seasonal_weights = get_seasonal_weights(month_str)
# Generate enhanced dataset (same as before)
na_data = []
for _ in range(2000):
    category = random.choices(categories, weights=seasonal_weights, k=1)[0]
    price_range = category_price_map[category]
    price = round(random.uniform(*price_range), 2)
    purchase_date = fake.date_between(start_date='-1y', end_date='today')
    shoot_day, shoot_time = get_shoot_day_and_time(category)
    na_data.append({
        'Customer Name': fake.name(),
        'Email': fake.email(),
        'Photo Type': category,
        'Purchase Date': purchase_date,
        'Month': purchase_date.strftime('%Y-%m'),
        'Price USD': price,
        'Country': random.choice(countries_na),
        'Payment Method': random.choice(payment_methods_na),
        'Referral Source': random.choice(referral_sources),
        'Customer Segment': random.choices(
            customer_segments, weights=[0.5, 0.2, 0.2, 0.1], k=1
        )[0],
        'Shoot Day': shoot_day,
        'Shoot Time': shoot_time
    })

df_na = pd.DataFrame(na_data)

realistic_weekly_path = "projected_monthly_sales_data.csv"
df_na.to_csv(realistic_weekly_path, index=False)

print("Generated projected monthly weekly sales:", realistic_weekly_path)



"""
How to Use in Drupal:
Run that Python script weekly (e.g., cron job).

Store the JSON in a table or file.

Load into drupalSettings.dashboard_sales_prediction.

Display it as another graph (Projected Weekly Sales).


# Group by month and sum the sales
monthly_sales = df_na.groupby('Month')['Price USD'].sum().sort_index()

# Calculate month-over-month growth rates
growth_rates = monthly_sales.pct_change().dropna()
average_growth = growth_rates.mean()

# Project next month's sales
last_month_sales = monthly_sales.iloc[-1]
next_month_sales = last_month_sales * (1 + average_growth)

# Distribute projected sales across 4 weeks
weeks = 4
weekly_projection = next_month_sales / weeks
projected_weekly = [round(weekly_projection, 2)] * weeks

# Create a DataFrame with projected dates starting from today
today = datetime.today()
projected_dates = [today + timedelta(weeks=i) for i in range(1, weeks + 1)]
projected_data = pd.DataFrame({
    'Projected Week': [date.strftime('%Y-%m-%d') for date in projected_dates],
    'Projected Sales (USD)': projected_weekly
})

projected_data

# todo 

growth_rates = []
months = list(monthly_sales.keys())
values = list(monthly_sales.values())

for i in range(1, len(values)):
    growth = (values[i] - values[i-1]) / values[i-1]
    growth_rates.append(growth)


average_growth = sum(growth_rates) / len(growth_rates)
#projected
last_month_sales = values[-1]
next_month_sales = last_month_sales * (1 + average_growth)


#distributedd weekly
weeks = 4
weekly_projection = next_month_sales / weeks
projected_weekly = [round(weekly_projection, 2)] * weeks




"""

"""
"""