# 📦 Product Inventory Management App

Welcome to the Product Inventory Management App – an interactive and beginner-friendly Streamlit dashboard for visualizing warehouse stock levels, restocking schedules, and product distribution across zones.

---

## 📌 Overview

This application helps warehouse managers and staff:

- 📊 View product quantities by category (bar plot)  
- 📈 Analyze restocking trends over time (line plot)  
- 🔥 Visualize stock distribution across zones (heatmap)  
- 📄 Preview raw inventory data  

---

## 🎯 Introduction

Inventory management is key to efficient warehouse operations. This app converts basic CSV inventory data into insightful visualizations for better stock control, restocking decisions, and zone monitoring.

---

## 🛠️ Tech Stack

Built using simple but powerful Python tools:

- 🐍 Python — Base programming language  
- 🧪 Pandas — For data handling and preprocessing  
- 📊 Matplotlib & Seaborn — For charts and heatmaps  
- 🌐 Streamlit — For building the interactive dashboard UI  

---

## 🧠 Why Use This App?

- ✅ Track inventory by category and zone  
- ✅ Monitor restock timelines  
- ✅ Understand stock allocation visually  
- ✅ Improve operational planning and reduce over/understocking  

---

## 🗂️ File Structure

```
product_inventory_app/
├── main.py                 # Streamlit application script
├── inventory_data.csv      # Sample inventory data
├── barplot.png             # (Auto-generated) bar chart
├── lineplot.png            # (Auto-generated) line chart
├── heatmap.png             # (Auto-generated) heatmap
└── README.md               # Project documentation
```

---

## 📄 Sample Dataset (inventory_data.csv)

| Product_ID | Product_Name   | Category    | Quantity | Restock_Date | Zone |
|------------|----------------|-------------|----------|--------------|------|
| P001       | Keyboard        | Electronics | 150      | 2025-05-25   | A1   |
| P002       | Mouse           | Electronics | 100      | 2025-05-30   | A2   |
| P004       | Chair           | Furniture   | 60       | 2025-05-27   | B1   |
| P006       | Whiteboard      | Stationery  | 40       | 2025-06-03   | C1   |
| ...        | ...             | ...         | ...      | ...          | ...  |

---

## 🚀 How to Run

### ✅ Clone the Repository

```bash
git clone https://github.com/your-username/product-inventory-app.git
cd product-inventory-app
```

### ✅ Install Required Libraries

```bash
pip install pandas matplotlib seaborn streamlit
```

### ✅ Launch the App

```bash
streamlit run main.py
```

Once launched, your browser will open the interactive dashboard automatically.

---

## 📦 Requirements

This project depends on:

- streamlit  
- pandas  
- matplotlib  
- seaborn  

Install all dependencies:

```bash
pip install streamlit pandas matplotlib seaborn
```

---

## 🤝 Contributing

Pull requests are welcome! Whether it’s a visual tweak, performance enhancement, or data formatting improvement — feel free to fork and open a PR.

---

## 📬 Contact

Made with ❤️ by Karthik Balaji S V
📧 Email: karthikbalaji0310@gmail.com
🌐 GitHub: https://github.com/KarthikBalaji-007

---

> Empowering Inventory Visibility Through Data 🚀
