# 📚 Book Recommendation System
---

 ## 🚀 Overview

✨ A content-based book recommendation system built with Python, pandas, scikit-learn, and Streamlit.

🔍 Helps you discover books similar to your favorites — now with support for Hindi and English books! 🇮🇳🌍

---

This project reads book data from a simple CSV file, calculates similarity using TF-IDF + cosine similarity, and lets users:

✅ Search for books by title

✅ Filter books by language

✅ See recommended books with covers, ratings, and descriptions

---

## 🔥 Features

📚 Content-based filtering: recommends books by analyzing their title, author, genre & description.

🌐 Language filter: choose to browse All, English, or Hindi books.

🖼 Covers & ratings: shows book images, star ratings, and summaries.

⚡ Blazing fast: uses cached vectorization for instant recommendations.

🖱 Interactive UI: built with Streamlit, deploy anywhere in minutes.

---

## 📂 Dataset
All data comes from a CSV file named book.csv.
Here’s a sample structure:

| book\_id | title      | author         | genre          | description                | cover\_url        | rating | language |
| -------- | ---------- | -------------- | -------------- | -------------------------- | ----------------- | ------ | -------- |
| 1        | The Hobbit | J.R.R. Tolkien | Fantasy        | Bilbo goes on adventure... | covers/hobbit.jpg | 4.8    | English  |
| 11       | गोदान      | मुंशी प्रेमचंद | हिन्दी साहित्य | होरी की गरीबी की कहानी...  | covers/godan.jpg  | 4.7    | Hindi    |


## ⚙️ Installation

📦 Clone this repo

git clone https://github.com/yourusername/book-recommendation-app.git

cd book-recommendation-app

## 🐍 Install requirements

pip install -r requirements.txt

## 🚀 Run the app locally

streamlit run app.py

Then open your browser at 👉 http://localhost:8501.

 ## 🛠 Tech Stack
| Tool            | Usage                         |
| --------------- | ----------------------------- |
| 🐍 Python       | Core programming language     |
| 📊 pandas       | Data loading & manipulation   |
| 🤖 scikit-learn | TF-IDF vectorizer, cosine sim |
| 🚀 Streamlit    | Web app interface             |

## 📜 License

This project is open source under the MIT License.

Feel free to fork, improve, and use it in your own projects!

🙌 Contributing
Have ideas for new features or improvements?

PRs and ⭐ stars are always welcome!

🥳 Happy reading! 📚
