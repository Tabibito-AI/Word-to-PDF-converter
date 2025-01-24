# ==========================================
# Word to PDF Converter - Project Dependencies
# ==========================================
# This program requires the following Python packages:
# - python-docx==0.8.11: A library for creating and updating Microsoft Word (.docx) files.
# - docx2pdf==0.1.8: A tool to convert .docx files to .pdf format.
#
# To install these packages, run the following command:
#   pip install python-docx==0.8.11 docx2pdf==0.1.8


import os
from glob import glob
from docx2pdf import convert
from datetime import datetime
 
def convert_word_to_pdf(input_dir, output_dir=None):
    """
    Convert Word documents in the specified directory to PDF format.
   
    Args:
        input_dir (str): Path to the directory containing Word files
        output_dir (str, optional): Path to the directory where PDF files will be saved
    """
    # If output directory is not specified, create a new directory in the input location
    if output_dir is None:
        output_dir = os.path.join(input_dir, 'pdf_output')
   
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
 
    # Search for Word files (.docx)
    word_files = glob(os.path.join(input_dir, "*.docx"))
    total_files = len(word_files)
   
    if total_files == 0:
        print(f"Warning: No Word files (.docx) found in {input_dir}")
        return
 
    print(f"Starting conversion. Found {total_files} files.")
    start_time = datetime.now()
 
    # Convert each Word file
    for i, word_file in enumerate(word_files, 1):
        try:
            filename = os.path.basename(word_file)
            pdf_name = os.path.splitext(filename)[0] + '.pdf'
            pdf_path = os.path.join(output_dir, pdf_name)
           
            print(f"[{i}/{total_files}] Converting: {filename}")
            convert(word_file, pdf_path)
            print(f"✓ Completed: {pdf_name}")
           
        except Exception as e:
            print(f"❌ Error: Failed to convert {filename}")
            print(f"Error details: {str(e)}")
 
    end_time = datetime.now()
    duration = end_time - start_time
    print("\nConversion completed!")
    print(f"Processing time: {duration}")
    print(f"Output directory: {output_dir}")
 
if __name__ == "__main__":
    # Usage example
    input_directory = input("Enter the path to the directory containing Word files: ")
    output_directory = input("Enter the path for PDF output directory (leave empty for default): ").strip()
   
    if output_directory:
        convert_word_to_pdf(input_directory, output_directory)
    else:
        convert_word_to_pdf(input_directory)