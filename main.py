import pyfiglet
import pyAesCrypt
import zipfile
from colorama import Fore, init
import os
import shutil

init()

banner = pyfiglet.figlet_format("FileCrypt v1")
print(Fore.LIGHTBLACK_EX + banner)

opinion = str(input(Fore.GREEN + "[!]" + Fore.WHITE + ' encrypt/decrypt: '))

if opinion == "encrypt":
    input(Fore.GREEN + "[!]" + Fore.WHITE + ' Please put your files in "files". After putting it press the enter key.')

    zip_name = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " Enter a name for your file: "))

    password = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " Password: "))

    with zipfile.ZipFile("%s.zip" % zip_name, "w") as z:
        files = os.listdir(os.getcwd() + "\\files")
        for file in files:
            z.write("files/%s" % file)
        z.close()

    buffer = 64 * 1024
    pyAesCrypt.encryptFile("%s.zip" % zip_name, zip_name, password, buffer)
    os.remove("%s.zip" % zip_name)
    shutil.rmtree("files")
    os.mkdir("files")
    print(Fore.GREEN + "[+]" + Fore.WHITE + ' Successful crypted !')
elif opinion == "decrypt":
    zip_name = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " File name: "))
    if os.path.isfile(zip_name):
        password = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " Password: "))

        buffer = 64 * 1024

        try:
            pyAesCrypt.decryptFile(zip_name, "%s.zip" % zip_name, password, buffer)
            os.remove(zip_name)
        except:
            print(Fore.RED + "[X]" + Fore.WHITE + ' Wrong password.')
            exit()

        print(Fore.GREEN + "[+]" + Fore.WHITE + ' True password...')

        with zipfile.ZipFile("%s.zip" % zip_name, "r") as z:
            shutil.rmtree("files")
            z.extractall()
        os.remove("%s.zip" % zip_name)
        print(Fore.GREEN + "[+]" + Fore.WHITE + ' Successful decrypted !')
    else:
         print(Fore.RED + "[X]" + Fore.WHITE + ' File not found.')