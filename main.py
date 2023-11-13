import os
import qrcode
from qrcode import QRCode


def qr_code_generator(input_string):
    QR = qrcode.make(input_string)
    QR.save("qrcode.png")

    os.startfile("D:\PROJECTS\Project- QRcode Generator\qrcode.png")


if __name__ == "__main__":
    print("***********************************")
    print("Hello! Wellcome to QR code genrator")
    print("***********************************\n")
    
    while(True):
        choice = int(input("Enter 1 to continue and 0 to exit: "))

        if choice == 1:
            input_str = input("Enter a string or a link that you want to convert into a qrcode: ")
            qr_code_generator(input_str)

        if choice == 0:
            break
        
        else:
            print("Please enter a valid choice.")
