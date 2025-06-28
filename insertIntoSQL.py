#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 14:35:50 2025

@author: crystalhansen
"""

INSERT INTO drqd_usca_sales_data_regional_pricing (
`customer_name`,
`email`,
`industrytype`,
`purchasedate`,
`month`,
`city`,
`region`,
`country`,
`price_USD`,
`payment_method`,
`referral_source`,
`customer_segment`,
`shoot_day`,
`shoot_time`  
    
) 
SELECT 
`customer_name`,
`email`,
`industrytype`,
`purchasedate`,
`month`,
`city`,
`region`,
`country`,
`price_USD`,
`payment_method`,
`referral_source`,
`customer_segment`,
`shoot_day`,
`shoot_time`
FROM realistic_weekly_sales_data_last_week;

#INSERT INTO drqd_usca_sales_data_regional_pricing SELECT * FROM realistic_weekly_sales_data; //realistic_weekly_sales_data_last_weekrealistic_weekly_sales_data_last_week


