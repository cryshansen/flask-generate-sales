#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 15:23:58 2025

@author: crystalhansen
"""
import requests
#Send back proojections to drupal



data = [
    {'sales_date': '2025-04-06', 'projected_sales': 1234.56},
    {'sales_date': '2025-04-07', 'projected_sales': 1300.78},
    # ...
]

response = requests.post(
    'https://your-drupal-site.com/api/projected-sales',
    json=data,
    headers={'Authorization': 'Bearer YOUR_API_TOKEN'}
)

print(response.status_code)