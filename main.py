import os
from PyPDF2 import PdfMerger

# Get the list of all PDF files in the current directory
pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]
# put all names of pdfs in a string

output_file_name = "_".join([os.path.splitext(f)[0] for f in pdf_files]) + " MERGED.pdf"

# Print the list of PDF files
print(pdf_files)


# Create a PdfMerger object
merger = PdfMerger()


# Append all the PDF files to the merger object
for pdf in pdf_files:
    merger.append(pdf)

# Write the merged PDF to a file give it the name of all the files
# merger.write(pdf_files + '.pdf')
# # Close the PdfFileWriter object
# merger.close()

# Write the merged PDF to a file
merger.write(output_file_name)
merger.close()

# delete the original files
for pdf in pdf_files:
    os.remove(pdf)


# Path: main.py

