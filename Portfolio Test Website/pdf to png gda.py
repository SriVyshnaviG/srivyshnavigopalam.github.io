from pdf2image import convert_from_path
import os

# Directory containing PDF files
pdf_dir = '/Users/srivyshnavigopalam/Desktop/portifolio website/images/AGDA/'
output_dir = '/Users/srivyshnavigopalam/Desktop/portifolio website/images/AGDA/converted/'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List of PDF files
pdf_files = [
    "1Foundations of Data Science.pdf",
    "2Get Started with Python.pdf",
    "3Go Beyond the Numbers: Translate Data into Insights.pdf",
    "4The Power of Statistics.pdf",
    "5Regression Analysis: Simplify Complex Data Relationships.pdf",
    "6The Nuts and Bolts of Machine Learning.pdf",
    "7Google Advanced Data Analytics Capstone.pdf",
    "GADA.pdf"
]

# Convert each PDF to images
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    if os.path.isfile(pdf_path):
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            image_name = f"{os.path.splitext(pdf_file)[0]}_page_{i + 1}.png"
            image_path = os.path.join(output_dir, image_name)
            image.save(image_path, 'PNG')
            print(f"Saved: {image_path}")
    else:
        print(f"File not found: {pdf_path}")

print("Conversion completed.")
