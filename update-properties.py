#!/usr/bin/env python
import argparse
from ansible.parsing.vault import VaultLib
from ansible_vault import Vault
import string
import os
import getpass

def add_properties(property_name, app_environment, application_name, vault_password, user_name):
    get_repo(user_name)
    change_branch(app_environment)
    data = read_from_vault(app_environment, application_name, vault_password)
    if property_name not in data:
        data = data+property_name
    write_to_vault(data, app_environment, application_name, vault_password)    

def update_properties(property_name_old, property_name_new, app_environment, application_name, vault_password, user_name):
    get_repo(user_name)
    change_branch(app_environment)
    data = read_from_vault(app_environment, application_name, vault_password)
    data = string.replace(data, property_name_old, property_name_new)
    write_to_vault(data, app_environment, application_name, vault_password)  

def remove_properties(property_name, app_environment, application_name, vault_password, user_name):
    get_repo(user_name)
    change_branch(app_environment)
    data = read_from_vault(app_environment, application_name, vault_password)
    data = string.replace(data, property_name, '')
    write_to_vault(data, app_environment, application_name, vault_password)

def get_repo(user_name):
    remove_repo()
    os.system('git clone git@github.pie.apple.com:{}/ds-private.git'.format(user_name))

def change_branch(dest_environment):
    os.chdir('ds-private')
    os.system('git checkout {}'.format(dest_environment))

def remove_repo():
    try:
        os.system('rm -rf ds-private')
    except OSError:
        pass

def read_from_vault(app_environment, application_name, vault_password):
    vault = VaultLib(vault_password)
    return(vault.decrypt(open('{}/{}.properties'.format(app_environment, application_name)).read()))

def write_to_vault(data, app_environment, application_name, vault_password):
    vault = Vault(vault_password)
    vault.dump_raw(data, open('{}/{}.properties'.format(app_environment, application_name), 'w'))

parser = argparse.ArgumentParser(description="Script can be used to add/update/remove properities defined under ds-private")
restricted_operations = parser.add_mutually_exclusive_group()
restricted_operations.add_argument("-add",     "-a",  help="Add properities")
restricted_operations.add_argument("-update",  "-u",  help="Update properities", nargs=2)
restricted_operations.add_argument("-remove",  "-r",  help="Remove properities")
parser.add_argument("-environment",    "-e",   help='select Environment', required=True)
parser.add_argument("-application",  "-app",   help='select Application', required=True)
parser.add_argument("-user",           "-U",   help='select user', required=True)
args = parser.parse_args()

vault_password = getpass.getpass("\n\tEnter vault password:  ")

if args.add:
    add_properties(args.add, args.environment, args.application, vault_password, args.user)
elif args.update:
    update_properties(args.update[0], args.update[1], args.environment, args.application, vault_password, args.user)
else:
    remove_properties(args.remove, args.environment, args.application, vault_password, args.user)
