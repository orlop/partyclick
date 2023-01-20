# Daniel Severa, Jr., TWK 2023
# a part of the Diffusionbooth/Partyclick project
# https://github.com/orlop/partyclick.git

# upload-image.py takes the generated image, uploads it and returns a QR code

import pyqrcode
import png
from pyqrcode import QRCode

import ftplib

# set up image filenames and server variables
filename = "img2img.png"

ftp = "ftp.tweakpost.cz"
username = "tweakpost.cz"
password = "nEa30q49QSjA"
ftp_domain = "tweakpost_cz"
ftp_subdomain = "partyclick"

local_subdirectory = "images"


local_path = local_subdirectory + "/" + filename
remote_path = "/" + ftp_subdomain + "/" + filename
url = ftp_subdomain + "." + username + "/" + filename


# generateqr() takes url and spits back a QR code as a PNG
def generateqr(url):
    QRstring = url
    url = pyqrcode.create(QRstring)
    url.png('images/qrcodepartyclick.png', scale=8)


# uploadtoftp() takes a filename and uploads it to a predefined ftp server
def uploadtoftp():
    session = ftplib.FTP(ftp,username,password)
    session.cwd(ftp_domain)
    session.cwd(ftp_subdomain)
    print(session.pwd())
    file = open(local_path,'rb')                  # file to send
    session.storbinary("STOR " + filename, file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()

uploadtoftp()
generateqr(url)