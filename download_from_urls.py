from urllib import request

sample_url = "https://bragland.wikispaces.com/file/view/Tuesdays+with+Morrie+full+text.pdf"
def download_data(url):
    response = request.urlopen(url)
    csv = str(response.read())
    lines = csv.split("\\n")
    saved_file = "goog.txt"
    fr = open(saved_file, "w")
    for line in lines:
        fr.write(line + "\n")
    fr.close()

download_data(sample_url)

