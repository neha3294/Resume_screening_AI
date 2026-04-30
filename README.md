# 📄 Resume Screening AI Tool (HR Analytics)

## 🚀 Overview

This project is an AI-powered Resume Screening Tool that helps recruiters automatically evaluate and rank candidates based on their resumes and a given job description.

It uses Natural Language Processing (NLP) techniques to:

* Compare resumes with job descriptions
* Calculate similarity scores
* Extract relevant skills
* Rank candidates based on match percentage

---

## 🎯 Features

* 📂 Upload multiple resumes (.txt, .docx)
* 📊 Automatic candidate ranking
* 🧠 Skill extraction from resumes
* 📈 Match score calculation using TF-IDF & Cosine Similarity
* ⚡ Fast and simple UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* NLTK
* python-docx

---

## 📁 Project Structure

```
resume-screening-ai/
│── app.py              # Main Streamlit app
│── utils.py            # Core logic (NLP, similarity, skill extraction)
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/resume-screening-ai.git
cd resume-screening-ai
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📄 How It Works

1. User enters a **Job Description**
2. Uploads resumes
3. System:

   * Extracts text from resumes
   * Cleans and processes text
   * Computes similarity score
   * Extracts skills
4. Displays:

   * Candidate ranking
   * Match score
   * Skills found

---

## 🧠 Example Output

```
Candidate: John_Doe.txt
Match Score: 78%
Skills: Python, SQL, Excel
```

---

## 🔮 Future Improvements

* 📑 Support PDF resumes
* 🤖 AI-based semantic matching (LLM integration)
* 📊 Advanced dashboard & analytics
* 🎯 Skill gap analysis (missing skills)
* 🌐 Deploy as web app

---

## 💡 Use Cases

* HR Resume Screening
* Internship Candidate Filtering
* Automated Hiring Assistance

---

## 👩‍💻 Author

Neha Kumari

---

## ⭐ If you found this useful, consider giving a star!
