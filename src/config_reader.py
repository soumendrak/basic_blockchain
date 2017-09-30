"""
Read customize.conf file
Author: Soumendra Kumar Sahoo
Date: 30 sep 2017
"""
import ConfigParser


config = ConfigParser.ConfigParser()
config.readfp(open('..\customize.config'))
hostname = config.get('GENERAL-SETTINGS', 'HOST')
port = config.get('GENERAL-SETTINGS', 'PORT')
print(hostname, port)
