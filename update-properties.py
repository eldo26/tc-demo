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
parser.add_argument("-action",  "-a",  help="add/update/remove properities", required=True)
parser.add_argument("-environment",    "-e",   help='select Environment',    required=True)
parser.add_argument("-application",  "-app",   help='select Application',    required=True)
parser.add_argument("-user",           "-u",   help='select user',           required=True)
parser.add_argument("-vaultpassword", "-v",   help='Ansible Vault Password', required=True)
parser.add_argument("-property",       "-p", help='Property name and value', required=True)
args = parser.parse_args()

vault_password = args.vaultpassword
action = args.action
property_name = args.property


if action == 'add':
    add_properties(property_name, args.environment, args.application, vault_password, args.user)
elif action == 'update':
    update_properties(property_name, args.environment, args.application, vault_password, args.user)
else:
    remove_properties(property_name, args.environment, args.application, vault_password, args.user)
