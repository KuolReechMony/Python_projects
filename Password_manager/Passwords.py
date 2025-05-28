# service: email/username, password/google passwords/screenshots, backup email/phone number, 2FA app, accessed services(addreses, debit cards, )

import sys, os
from cryptography.fernet import Fernet
import xml.etree.ElementTree as ET

emails = ("kuol2reech@gmail.com", "kuolreechbu@gmail.com", "kuolreech@outlook.com", "rkuol@iu.edu")
two_factor_authentications = ("microsoft", "google", "duo")

wd = os.getcwd()
with open(f"{wd}\Password_manager\password.txt", "rt") as file:
    master = file.readlines()
    key = master[0]
f = Fernet(key[2:-1])


def write_to_xml(service, email_username, passwd, backup, TwoFA, allowed_permissions):
    xml_path = os.path.join(wd, "Password_manager", "configs.xml")

    # Try to parse the file or create root if not exists
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except FileNotFoundError:
        root = ET.Element("configs")
        tree = ET.ElementTree(root)

    # Create a new config entry
    config = ET.Element("config")  # Create a separate tag for each service
    
    service_tag = ET.SubElement(config, "service")
    service_tag.text = service  # Plain text

    email_tag = ET.SubElement(config, "email_or_username")
    email_tag.text = email_username.decode() if isinstance(email_username, bytes) else email_username

    pass_tag = ET.SubElement(config, "password_googlePasswords_Screenshots")
    pass_tag.text = passwd.decode() if isinstance(passwd, bytes) else passwd

    backup_tag = ET.SubElement(config, "backupEmail_phoneNumber")
    backup_tag.text = backup.decode() if isinstance(backup, bytes) else (backup if backup else "")

    fa_tag = ET.SubElement(config, "twoFactorAuthentication")
    fa_tag.text = TwoFA

    perm_tag = ET.SubElement(config, "permissions")
    perm_tag.text = allowed_permissions.decode() if isinstance(allowed_permissions, bytes) else allowed_permissions

    # Append the new config
    root.append(config)

    # Write back to XML
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)


def username_or_email(service, code):
    print(f"Email/username >> {service}")

    match code:
        case 1:
            choice = input("Menu: 1 - username, 2 - email: ")
            match choice.strip().lower():
                case '1':
                    username = input("Username: ")
                    return f.encrypt(username.encode())
                case '2':
                    email = input("Email: ")
                    if email.strip().lower() in emails:
                        return f.encrypt(email.encode())
                    else:
                        print(f"{email} >> invalid email!!")

def passwords(service, code):
    print(f"Password >> {service}")
    choice = input("Menu: 1 - google passwords, 2 - screenshots, 3 - password: ")
    match choice.strip().lower():
        case '1':
            return 'GooglePasswords'
        case '2':
            return 'Screenshots'
        case '3':
            try:
                password = input("Password: ")
                if (input("Verify password: ") == password):
                    return f.encrypt(password.encode())
            except:
                print("Error!")
    
def backupEmail_or_Phone(service, code):
    choice = input("Menu: 1 - Phone, 2 - Backup email, 3 - Both: ")
    match choice.strip():
        case '1':
            return 'Phone'
        case '2':
            backupEmail = input(f"Backup email for {service}: ")
            if backupEmail.strip() in emails:
                return f.encrypt(backupEmail.encode())

def two_factor(service, code):
    app = input(f"Two factor authentication app for {service}: ")
    if app.strip().lower() in two_factor_authentications:
        return app.strip().lower()

def permissions(service, code):
    choice = input(f"Permissions for {service}: Address? Banking? Emergency contact? ")
    return f.encrypt(choice.replace(" ", "").encode())

 
def menu(choice, Service_name):
    xml_path = os.path.join(wd, "Password_manager", "configs.xml")
    match choice:
        case '1':  # CREATE config
            try:
                if Service_name.strip() != '':
                    email_username = username_or_email(Service_name, 1)
                    passwd = passwords(Service_name, 1)
                    backup = backupEmail_or_Phone(Service_name, 1)
                    TwoFA = two_factor(Service_name, 1)
                    allowed_permissions = permissions(Service_name, 1)

                    write_to_xml(Service_name, email_username, passwd, backup, TwoFA, allowed_permissions)
                    print(f"[+] Config for {Service_name} saved.")
            except Exception as e:
                print("Menu Error (Create):", e)

        case '2':  # READ config
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                found = False

                for config in root.findall("config"):
                    service = config.find("service").text.strip()
                    if service.lower() == Service_name.strip().lower():
                        found = True
                        print(f"\n[+] Config for {service}")
                        for tag in ["email_or_username", "password_googlePasswords_Screenshots", "backupEmail_phoneNumber", "permissions"]:
                            value = config.find(tag).text
                            decrypted = f.decrypt(value.encode()).decode() if value else ""
                            print(f"{tag}: {decrypted}")
                        print(f"twoFactorAuthentication: {config.find('twoFactorAuthentication').text}")
                        break

                if not found:
                    print(f"[!] No config found for '{Service_name}'.")

            except Exception as e:
                print("Menu Error (Read):", e)

        case '3':  # DELETE config
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                found = False

                for config in root.findall("config"):
                    service = config.find("service").text.strip()
                    if service.lower() == Service_name.strip().lower():
                        root.remove(config)
                        found = True
                        tree.write(xml_path, encoding="utf-8", xml_declaration=True)
                        print(f"[-] Config for '{Service_name}' deleted.")
                        break

                if not found:
                    print(f"[!] No config found for '{Service_name}'.")

            except Exception as e:
                print("Menu Error (Delete):", e)

        case _:  # INVALID choice
            print("[!] Invalid menu option.")



menu(input("Menu: 1 - create new config, 2 - read config, 3 - delete old config: "), input("Name of service: "))