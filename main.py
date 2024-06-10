import os
from PyPDF2 import PdfMerger

# Get the list of all PDF files in the current directory
pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]

# Generate the output file name based on the input file names
output_file_name = "_".join([os.path.splitext(f)[0] for f in pdf_files]) + "_MERGED.pdf"

# Ensure the file name is not too long
if len(output_file_name) > 255:
    output_file_name = output_file_name[:252] + "..."

# Print the list of PDF files and the generated output file name
print("PDF files:", pdf_files)
print("Output file name:", output_file_name)

# Create a PdfMerger object
merger = PdfMerger()

# Append all the PDF files to the merger object
for pdf in pdf_files:
    merger.append(os.path.join(os.getcwd(), pdf))

# Write the merged PDF to a file
merger.write(output_file_name)
merger.close()

# Delete the original files
for pdf in pdf_files:
    os.remove(pdf)

print(f"Merged PDF saved as {output_file_name}")
print("Original PDF files deleted.")
