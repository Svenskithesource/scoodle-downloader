# scoodle-saver
A Python program to save an online school book into a PDF

## How to use it
First of all add TamperMonkey to your browser. Then install [this](https://greasyfork.org/en/scripts/398781-scoodle-correctie) script. After all these steps you can go open the online book you wish to download. You need to open inspect element and go to the network tab. If you go to the next pages you'll see some activity on the network tab. If you look at the request url it will look something like this https://content.plantyn.com/CMS/CDS/Plantyn/Published%20Content/eBooks/xxx.pdf_/20.png if you cut the 20.png part out you need to input that to the program when you run it. For the cookie part visit the request url with the image and go to the Applications tab in the Developer tools. There you can find the cookies you need. This should be everything, if it doesn't work you'll need to debug it yourself. I won't give support for this.

## Installation
`pip install -r requirements.txt`

`python main.py`

## Disclaimer
This is for education purposes only. I am not responsible for anything done with this.
