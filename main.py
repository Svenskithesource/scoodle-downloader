import requests, os, re, shutil
from PIL import Image


def save(book_url: str, correction_url: str, cookies: dict, path="pages"):
    if not os.path.exists(path):
        os.mkdir(path)
    with requests.Session() as s:
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        }

        s.headers.update(headers)
        s.cookies.update(cookies)

        n = 1

        while True:
            req = s.get(
                f"{book_url}{n}.png")
            if str(req.status_code).startswith("2"):
                with open(f"./pages/{n}.png", 'wb') as f:
                    f.write(req.content)
            else:
                print(f"Found {n} pages")
                break
            req = s.get(
                f"{correction_url}{n}.png")
            if str(req.status_code).startswith("2"):
                with open(f"./pages/{n}_correction.png", 'wb') as f:
                    f.write(req.content)
            n += 1


def merge(ext="_correction", suffix="_corrected", path="pages"):
    for f in os.listdir(path):
        if ext not in f:
            name, file_ext = os.path.splitext(f)
            if name + ext + file_ext in os.listdir(path):
                base_img = Image.open(os.path.join(path, f))
                correction_img = Image.open(os.path.join(path, name + ext + file_ext))
                base_img.paste(correction_img, (0, 0), correction_img)
                base_img.save(os.path.join(path, name + suffix + file_ext))

def convert_pdf(path="pages", suffix="_corrected", suffix_correction="_correction", fn="book.pdf", delete_img=True):
    images = []
    for f in sorted(os.listdir(path), key=lambda x: int(re.sub("\D", "", x))):
        name, file_ext = os.path.splitext(f)
        if suffix in f:
            img = Image.open(os.path.join(path, f))
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            images.append(img)
        elif suffix not in f and suffix_correction not in f and name + suffix + file_ext not in os.listdir("pages"):
            img = Image.open(os.path.join(path, f))
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            images.append(img)
    pdf = images[0]
    pdf.save(fn, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    if delete_img:
        shutil.rmtree(path)

book = input("The book pdf url (end with /): ")
correction = input("The correction pdf url (end with /): ")
pages = int(input("How many pages are there: "))
cookie_1 = input("Cookie 1 (Name: N%40TCookie): ")
cookie_2 = input("Cookie 2 (Name: _3sct): ")

save(
    book,
    correction,
    {
        "N%40TCookie": cookie_1,
        "_3sct": cookie_2
    }
)
print("Downloaded and saved all the pages of the book.")
print("Downloaded and saved the correction of all the pages.")
merge()
print("Merged the pages and the corrections")
convert_pdf()
print("Saved the all the pages in a pdf")