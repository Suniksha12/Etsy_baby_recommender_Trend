
# 🛒 Personalized Product Recommendation System for Etsy Baby Items 🎁

This Flask-based application recommends similar products based on user preferences such as price, favorites, and reviews. Ideal for users searching for personalized baby product recommendations on Etsy.

## 🚀 Features
- **Custom Preferences:** Filter products by price range, popularity, and number of reviews.
- **Data Analysis:** Uses cleaned dataset for accurate recommendations.
- **Machine Learning Models:** Random Forest, Gradient Boosting, and SVC models applied for precise predictions.

## 📁 Project Structure
```bash
Flask/
│
├── app.py                   # Main Flask application
├── Cleaned_data.csv          # Dataset used for recommendations
├── templates/
│   ├── index.html            # Homepage with preference input
│   ├── recommendations.html  # Displays recommendations
└── static/
    ├── background.jpg        # Background image
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone <repository-link>
   ```
2. Navigate to the project directory:
   ```bash
   cd flask
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## 💻 Usage
- Visit `http://127.0.0.1:5000/` in your browser.
- Enter preferences such as price, number of favorites, and reviews.
- View the list of recommended products.

## 🔍 Exploratory Data Analysis
- Price Distribution:
  ![Price Distribution](static/price_distribution.png)
  
- Correlation Heatmap:
  ![Heatmap](static/correlation_heatmap.png)

## 📊 Model Performance
- Random Forest achieved **100%** accuracy.
- Gradient Boosting and SVC yielded great results with accuracy and feature importance.

## 📸 Screenshots

### Homepage
![Homepage](static/homepage_screenshot.png)

### Recommendations
![Recommendations](static/recommendations_screenshot.png)

---

🌟 **Future Improvements:**
- Include additional user preferences.
- Improve UI for a better user experience.

🌐 Check out the live application [here](#).

👩‍💻 Made with ❤️ by [Your Name](#).
