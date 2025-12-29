import os
import glob
import csv
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# تنظیمات اولیه
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. پیدا کردن اتوماتیک تمام فایل‌های PDF در پوشه
pdf_files = glob.glob("*.pdf")
print(f"📂 تعداد {len(pdf_files)} مقاله PDF پیدا شد. شروع تحلیل...\n")

# اسم فایل خروجی اکسل
output_csv = "HER_Catalyst_Data.csv"

# 2. باز کردن فایل اکسل برای نوشتن
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # نوشتن سرستون‌های جدول
    writer.writerow(["File Name", "Catalyst Name", "Overpotential (mV)", "Tafel Slope (mV/dec)", "Summary"])

    for filename in pdf_files:
        print(f"🔄 در حال پردازش: {filename}...")
        try:
            # خواندن PDF
            reader = PdfReader(filename)
            text = ""
            # خواندن 8 صفحه اول (معمولاً نتایج اصلی اینجاست)
            for page in reader.pages[:8]:
                text += page.extract_text()

            # اگر فایل خالی بود رد شو
            if len(text) < 100: continue

            # ارسال به هوش مصنوعی با دستور خاص برای فرمت CSV
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a data extractor. Output ONLY comma-separated values."},
                    {"role": "user", "content": f"""
                    Analyze this text about HER catalysts. Find the BEST catalyst.
                    Output the response in this EXACT format (one line only):
                    CatalystName, Overpotential_Value_Only, Tafel_Value_Only, Very_Short_Conclusion

                    Example:
                    Ni-Mo-S, 120, 45, Good acidic stability
                    
                    If specific number is not found, write "N/A".
                    
                    Text:
                    {text[:12000]}
                    """}
                ]
            )
            
            # تمیز کردن جواب و تبدیل به لیست
            ai_output = response.choices[0].message.content.strip()
            data_parts = ai_output.split(',')
            
            # ذخیره در فایل اکسل
            # (اسم فایل PDF را هم اولش اضافه می‌کنیم که بدانید این داده مال کدام مقاله است)
            writer.writerow([filename] + data_parts)
            print(f"   ✅ داده‌ها ذخیره شد.")

        except Exception as e:
            print(f"   ❌ خطا در فایل {filename}: {e}")

print(f"\n🎉 تمام شد! فایل '{output_csv}' را باز کنید.")