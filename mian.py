import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def add_border(pdf, x, y, width, height, border_width):
    # Set the line color and width
    pdf.setStrokeColorRGB(0, 0, 0)  # Black color
    pdf.setLineWidth(border_width)  # Line width in points

    # Draw the border rectangle
    pdf.rect(x, y, width, height)

def image_to_pdf(image_path, pdf_path, margin, line_width, line_space, border_width):
    # Open the image using Pillow
    image = Image.open("C:\\Users\\Kamali V M\\Desktop\\python project\\sece.jpg")

    # Convert the image to grayscale
    gray_image = image.convert("L")

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(gray_image)

    # Create a new PDF file
    pdf = canvas.Canvas(pdf_path, pagesize=letter)

    # Set the font and font size
    pdf.setFont("Helvetica", 12)

    # Add the extracted text to the PDF
    lines = text.split("\n")

    # Initial y-coordinate
    y = 700

    for line in lines:
        pdf.drawString(60, y, line)
        y -= 16  # Decrease y-coordinate for the next line

    # Calculate the position and size of the border rectangle
    page_width, page_height = letter
    x = margin
    y = margin
    width = page_width - 2 * margin
    height = page_height - 2 * margin

    # Add border around the extracted text
    add_border(pdf, x, y, width, height, border_width)

    # Save and close the PDF file
    pdf.save()

# Set the desired margin size, line width, line space, and border width
margin = 10
line_width = 1.5
line_space = 20
border_width = 2  # Adjust the value to increase or decrease the border width

# Provide the path to your image and the desired output PDF path
image_path = "C:\\Users\\Kamali V M\\Desktop\\python project\\sece.jpg"
pdf_path = "C:\\Users\\Kamali V M\\Desktop\\python project\\Finaloutput.pdf"

# Call the function to perform OCR and convert to PDF with border
image_to_pdf(image_path, pdf_path, margin, line_width, line_space, border_width)
