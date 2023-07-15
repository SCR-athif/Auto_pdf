import requests

def download_pdf(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {url}")

# Path to the text file containing the URLs
url_file = 'pdf_list.txt'


# Read URLs from the text file
with open(url_file, 'r') as file:
    pdf_urls = file.read().splitlines()

# Download PDFs from each URL
for index, url in enumerate(pdf_urls, start=1):
    file_name = f"file{index}.pdf"
    destination = f"/path/to/save/file/{file_name}"
    download_pdf(url, destination)