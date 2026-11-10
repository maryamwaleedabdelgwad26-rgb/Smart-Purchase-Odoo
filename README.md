# Smart Purchase – Odoo 19

**Smart Purchase** is a custom Odoo module designed to improve the purchasing and inventory replenishment process.

It helps businesses monitor stock levels, identify products that need replenishment, compare supplier offers, and create purchase requests from the best available supplier.

## Features

- **Reorder Alerts:** Automatically identify products whose forecasted stock reaches or falls below the minimum quantity.
- **Reorder Settings:** Define minimum stock quantities and suggested reorder quantities for each product.
- **Supplier Comparison:** Compare supplier offers based on price and delivery time.
- **Currency Conversion:** Display supplier prices in the company currency (EGP).
- **Best Supplier Selection:** Highlight the best supplier based on the lowest converted price, then the shortest delivery time.
- **Purchase Request Creation:** Create an RFQ directly from the selected supplier offer.
- **Pending Purchase Warnings:** Warn users when there are existing purchase orders with quantities that have not yet been fully received.

## Technologies Used

- Python
- Odoo 19
- XML
- PostgreSQL
- Odoo ORM
- Git & GitHub

## Odoo Dependencies

- Purchase
- Inventory (Stock)

## Installation

1. Clone this repository into your custom Odoo addons directory:

   ```bash
   git clone https://github.com/maryamwaleedabdelgwad26-rgb/Smart-Purchase-Odoo.git
   ```

2. Make sure the parent directory containing `Smart_Purchase` is included in your Odoo `addons_path`.

3. Restart the Odoo server.

4. Open Odoo and enable Developer Mode.

5. Go to **Apps** and click **Update Apps List**.

6. Search for **Smart Purchase** and install the module.

## How It Works

1. Configure minimum and reorder quantities for your products.
2. Add supplier offers with their prices, currencies, and delivery times.
3. Make sure the required currency exchange rates are configured in Odoo.
4. The scheduled action checks product stock levels hourly.
5. View products that need replenishment in **Smart Reorder → Reorder Alerts**.
6. Compare supplier offers in **Smart Reorder → Supplier Comparison**.
7. Create a purchase request from the best available supplier.

## Project Structure

```text
Smart_Purchase/
│
├── __init__.py
├── __manifest__.py
│
├── data/
│   └── cron.xml
│
├── models/
│   ├── __init__.py
│   ├── product_template.py
│   ├── supplier_info.py
│   └── order_warning.py
│
├── security/
│   └── ir.model.access.csv
│
└── views/
    ├── menu.xml
    ├── product_views.xml
    ├── supplierinfo_views.xml
    └── order_warning_views.xml
```

## Screenshots & Demo

Screenshots and a demonstration video will be added soon.

## License

This project is licensed under the LGPL-3 license.
