import os
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# 1. تنظیمات اولیه (لود کردن کلید)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# لیست مقالاتی که آپلود کردید
pdf_files = [
    "AECM-6995-typeset+manuscript (2).pdf",
    "AECM5423-typeset+manuscript (1).pdf"
]

def analyze_catalyst(filename):
    print(f"\n📄 در حال خواندن فایل: {filename}...")
    
    try:
        # خواندن متن PDF
        reader = PdfReader(filename)
        text = ""
        # خواندن 8 صفحه اول (معمولاً نتایج در همین صفحات است)
        for page in reader.pages[:8]:
            text += page.extract_text()
            
        print("   🧠 هوش مصنوعی در حال استخراج داده‌ها...")
        
        # ارسال به GPT برای تحلیل
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert Electrochemist specializing in Hydrogen Evolution Reaction (HER)."},
                {"role": "user", "content": f"""
                Analyze this research paper text. Identify the BEST catalyst mentioned.
                Extract these specific metrics:
                
                1. **Catalyst Composition**: (e.g., MoS2, NiFe-LDH)
                2. **Overpotential**: (at 10 mA/cm², in mV)
                3. **Tafel Slope**: (mV/dec)
                4. **Stability**: (Duration in hours or cycles)
                
                If precise numbers are not found, state "Not found".
                
                Paper Text Snippet:
                {text[:12000]}
                """}
            ]
        )
        
        # نمایش نتیجه
        print("-" * 40)
        print(f"نتایج آنالیز برای: {filename}")
        print(response.choices[0].message.content)
        print("-" * 40)
        
    except FileNotFoundError:
        print(f"❌ خطا: فایل {filename} پیدا نشد! لطفاً اسم فایل را چک کنید.")
    except Exception as e:
        print(f"❌ خطای غیرمنتظره: {e}")

# اجرای برنامه
print("--- شروع جستجو برای بهترین کاتالیزور ---")
for f in pdf_files:
    analyze_catalyst(f)