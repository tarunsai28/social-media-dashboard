# 📊 Social Media Analytics Dashboard

An interactive web dashboard built using **Python, Streamlit, and Plotly** to visualize and analyze key performance indicators (KPIs) from a social media marketing dataset.

> This project reflects practical analytics work applied in tools like Power BI and Streamlit, and demonstrates data preprocessing, KPI computation, and interactive data storytelling.

---

## 📁 Project Structure
social-media-dashboard/
├── app.py # Streamlit application code
├── cleaned_data.xlsx # Cleaned dataset with no missing values
├── README.md # Project documentation (this file)

---

## 📊 KPIs Implemented

| KPI | Description |
|-----|-------------|
| **Engagement Rate (%)** | `(likes + comments + shares) / reach * 100` |
| **Virality Rate (%)** | `shares / impressions * 100` |
| **Average Reach by Platform** | `groupby(platform)['reach'].mean()` |
| **Follower Growth Trend** | `post_date` vs `follower_count_at_time_of_post` |
| **Engagement by Post Type** | `groupby(post_type)['engagement_rate'].mean()` |

---

## 🛠️ Tools & Technologies

- **Python 3.11+**
- **Pandas** for data preprocessing
- **Plotly Express** for interactive visualizations
- **Streamlit** for building the dashboard interface
- **OpenPyXL** to read Excel files

---

## 🚀 How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/social-media-dashboard.git
cd social-media-dashboard
2. Create Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or manually install:

bash
Copy
Edit
pip install streamlit pandas plotly openpyxl
4. Run the App
bash
Copy
Edit
streamlit run app.py
5. View in Browser
The app will launch at: http://localhost:8501

🌐 Deployment (Optional)
You can deploy this project to Streamlit Cloud:

Push this project to a public GitHub repository

Log in to Streamlit Cloud

Click "New app" → Select your repo and app.py

Click Deploy

📸 Dashboard Previews
You can include screenshots here:

pgsql
Copy
Edit
📈 Follower Growth Over Time
📊 Engagement by Post Type
📣 Reach by Platform
✍️ Author
Tarun Sai Tirumala
Graduate Student – Computer Science
📧 tarunsaitirumala@gmail.com
