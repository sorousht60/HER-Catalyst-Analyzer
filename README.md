# 🧪 HER Catalyst Analyzer AI

This project is an AI-powered agent designed to assist Nanotechnology researchers in analyzing **Hydrogen Evolution Reaction (HER)** catalysts.

It automates the extraction of critical electrochemical parameters from research manuscripts (PDFs), saving hours of manual data review.

## 🚀 Features
* **PDF Parsing:** automatically reads complex scientific manuscripts.
* **Data Extraction:** Identifies key metrics:
    * Overpotential (at 10 mA/cm²) ⚡
    * Tafel Slope (mV/dec) 📉
    * Stability Duration ⏱️
* **Comparison:** Helps select the best catalyst among multiple papers.

## 🛠️ Tech Stack
* Python 3.10+
* OpenAI API (GPT-4o)
* `pypdf` for document processing

## 💻 How to Run
1.  Clone the repository.
2.  Install dependencies: `pip install openai pypdf python-dotenv`
3.  Add your API key in a `.env` file.
4.  Run the agent: `python main.py`

## 🚀 Features (v2.0 Update)
* **Batch Processing:** Automatically scans and processes all PDF files in a folder. 📂
* **Excel Export:** Saves extracted data (Tafel slope, Overpotential, etc.) into a CSV file for easy plotting. 📊
* **Auto-Filtering:** Skips empty or unreadable files automatically.
---

*Created by a Micro- and Nanotechnology student at Hochschule München.*
