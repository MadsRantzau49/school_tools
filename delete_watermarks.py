import fitz  # PyMuPDF

def crop_and_delete_page(input_pdf_path, output_pdf_path, margin=20, page_to_delete=2):
    # Open the input PDF file
    pdf_document = fitz.open(input_pdf_path)
    
    # Delete the specified page
    if page_to_delete <= len(pdf_document) and page_to_delete >= 1:
        pdf_document.delete_page(page_to_delete - 1)  # Page numbers are 0-based
        
    # Iterate through each page in the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        
        # Get the current page's dimensions
        page_rect = page.rect
        
        # Define the new crop rectangle with margins
        new_rect = fitz.Rect(
            page_rect.x0 + margin,
            page_rect.y0 + margin,
            page_rect.x1 - margin,
            page_rect.y1 - margin
        )
        
        # Crop the page
        page.set_cropbox(new_rect)
    
    # Save the modified PDF to the output path
    pdf_document.save(output_pdf_path)
    
    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_file = "D:/code/PDF_cropper/Problem_solving_and_program_design_in_C.pdf"  # Replace with the path to your input PDF
    output_pdf_file = "Problem_solving_and_program_design_in_C_new.pdf"  # Replace with your output PDF file path
    margin_pixels = 20
    page_to_delete = 2
    
    crop_and_delete_page(input_pdf_file, output_pdf_file, margin_pixels, page_to_delete)
    print(f"PDF cropped, and page {page_to_delete} deleted. Saved to {output_pdf_file}")







    #input_pdf_path = "D:/code/PDF_into_text/Discrete_Mathematics_and_its_applications.pdf"  # Replace with the path to your input PDF