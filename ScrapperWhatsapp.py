#!/usr/bin/env python3


import argparse
import sys
import os
import logging

parser = argparse.ArgumentParser(
    description='An OSINT tool to extract contacts and chats of Contact and Groups Whatsapp')

subparsers = parser.add_subparsers(help='commands')

contactos_parser = subparsers.add_parser(
    'contacts', help='scrape online list members groups')

contactos_parser.add_argument(
    "-a", dest="lista", action="store_true", help="use for list contacts")

grupos_parser = subparsers.add_parser(
    'groups', help='scrape online list contacts')

grupos_parser.add_argument(
    "-g", required=True, metavar="MEMBERS", dest="members", help="List Member Group")

chat_parser = subparsers.add_parser(
    'chats', help="extract chats")

chat_parser.add_argument("-c", required=True, metavar="CONTACT",
                              dest="contact", help="need nanme contact")


args = parser.parse_args()
# Add missing param
try:
    vars(args)["action"] = sys.argv[1]
except IndexError as e:
    #logger.error("Please, add an option to execute")
    parser.print_help()
    sys.exit()

if args.action == "contacts":
    #start_scrapping(args.email, args.quiet)
    print("A sin argumentos")
    print (args.lista)

elif args.action == "groups":
    print (args.members)
    #if not re.match("^[0-9X]{10}", args.mask):
     #    exit()
    #if args.proxies:
    #    set_proxy_list()
    #possible_phone_number = get_possible_phone_numbers(args.mask)

elif args.action == "chats":
    print (args.contact)
    #if not re.match("^[0-9X]{10}", args.mask):
     #    exit()
    #if args.proxies:
    #    set_proxy_list()
    #possible_phone_number = get_possible_phone_numbers(args.mask)
