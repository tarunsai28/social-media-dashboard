# 📊 Social Media Analytics Dashboard

This project presents an interactive dashboard built with Python, Pandas, Plotly, and Streamlit to analyze social media post performance and visualize key marketing KPIs. It includes full data preprocessing, KPI computation, and user-friendly interactive insights.

---

## 📸 Dashboard Preview

### 🔹 Full Dashboard Overview
![Dashboard Overview](Screenshot%202025-07-23%20220631.jpg)

### 🔹 Visuals in Detail
![Platform Reach, Engagement, Growth](Screenshot%202025-07-23%20220650.jpg)

---

## 🚀 Features

- Cleaned and processed raw post data
- Calculated engagement and virality metrics
- Built an interactive web dashboard using Streamlit
- Visualized metrics by platform, post type, and over time

---

## 🔄 Data Processing Summary

The raw data required significant preprocessing, all of which was done using Pandas in Jupyter Notebook (`Data Processing.ipynb`):

- The **`post_date`** column had inconsistent formats (e.g., `"2025-06-01"` and `"05-May-2025"`). All dates were parsed and converted to a standard datetime format.
- The **`likes`** column contained commas (e.g., `"1,200"`) which prevented numeric operations. These commas were removed and the values were converted to floats.
- Missing values in `likes` and `shares` were filled using the **median** of their respective columns to avoid distortion from outliers.
- Derived new KPI columns:
  - **`total_engagement`** = likes + comments + shares
  - **`engagement_rate`** = (total_engagement / reach) × 100
  - **`virality_rate`** = (shares / impressions) × 100
- Exported the final cleaned dataset as `cleaned_data.xlsx` for use in the Streamlit app.

---

## 📊 Key Performance Indicators

- **Engagement Rate (%)** = `(likes + comments + shares) / reach × 100`
- **Virality Rate (%)** = `shares / impressions × 100`
- **Follower Growth Over Time**
- **Average Reach by Platform**
- **Engagement Rate by Post Type**

---

## 📂 Project Structure

- social-media-dashboard/
- ├── Data Processing/
- │ └── Data Processing.ipynb
- ├── app.py
- ├── cleaned_data.xlsx
- ├── requirements.txt
- ├── README.md
- ├── Screenshot 2025-07-23 220631.jpg
- ├── Screenshot 2025-07-23 220650.jpg

## 💻 How to Run the App Locally

### 🧰 Prerequisites

- Python 3.9+
- Streamlit
- Pandas
- Plotly
- OpenPyXL

## 🔧 Setup

```bash
# Clone the repository
git clone https://github.com/tarunsai28/social-media-dashboard.git
cd social-media-dashboard

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

## 👤 Author
Tarun Sai Tirumala
M.S. Computer Science