import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_business_card_info(thresh_img):

    text = pytesseract.image_to_string(thresh_img)
    
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phone_pattern = r'[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]'
    
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    detected_name = lines[0] if len(lines) > 0 else "Not detected"
    detected_org = lines[1] if len(lines) > 1 else "Not detected"
    
    return {
        "raw_text": text,
        "name": detected_name,
        "company": detected_org,
        "emails": emails if emails else ["Not detected"],
        "phones": phones if phones else ["Not detected"]
    }