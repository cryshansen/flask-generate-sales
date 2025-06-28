# 📸 Photography Sales Data Generator (Python + Flask + Faker)

This project generates realistic fake sales data for a photography business using Python and the `Faker` library. Originally designed as a lightweight API and CSV generator using Flask, it was later ported to a Drupal module for integration into a dynamic sales dashboard.

---

## 🎯 Purpose

To create believable and varied weekly photography sales data, supporting analytics dashboards, portfolio projects, and visualizations without relying on sensitive or real client data.

---

## 🔧 Technologies Used

- **Python 3**
- **Faker** – for generating names, emails, locations, etc.
- **Pandas** – for CSV output
- **Flask** (optional) – to serve generated data via API endpoint (for early demos)

---

## 🧪 Features

- Generates 2,000 rows of sales data
- Includes weighted categories:
  - Wedding
  - Portrait
  - Event
  - Real Estate
  - Product
  - Stock Photo License
- Assigns pricing ranges based on job type
- Dynamically creates:
  - Purchase date (realistic day-of-week distribution)
  - Shoot date and time (based on type)
  - Customer name, email, city, region, and country
  - Payment method
  - Referral source
  - Customer segment (with weights)

---

## 🗃️ Output Fields

| Field             | Description                        |
|------------------|------------------------------------|
| `customer_name`   | Random full name                   |
| `email`           | Random email address               |
| `industrytype`    | Type of photography job            |
| `purchasedate`    | Simulated date of purchase         |
| `month`           | Purchase month (YYYY-MM)           |
| `city`, `region`, `country` | Geographic metadata      |
| `price_USD`       | Estimated fee for the job          |
| `payment_method`  | How the job was paid               |
| `referral_source` | Lead source (e.g. Instagram)       |
| `customer_segment`| Type of buyer                      |
| `shoot_day`       | Scheduled shoot day                |
| `shoot_time`      | Scheduled shoot time               |

---

## 📄 Output File

The generated data is saved to:

