#! /usr/bin/python

from getpass import getpass
from optparse import OptionParser
from urllib.parse import urlparse

import psycopg2
# python3-bcrypt comes from EPEL
import bcrypt


def process_cmdline():
    parser = OptionParser()
    parser.add_option('--dbname', dest='db_name',
                      help='database')
    parser.add_option('--dbuser', dest='db_user',
                      help='database user')
    parser.add_option('--dbhost', dest='db_host',
                      help='database host')
    parser.add_option('--dbpassword', dest='db_passwd',
                      help='database_passwd')
    parser.add_option('--dburi', dest='db_uri',
                      help='database URI, if used, other parameters are ignored')
    parser.add_option('-u', '--user', dest='username',
                      help='quay user')
    parser.add_option('-p', '--password', dest='password',
                      help='new password')
    (options, args) = parser.parse_args()
    
    if parser.get_option('db_uri') is None:
        result = urlparse(options.db_uri)
        options.db_name = result.path[1:]
        options.db_user = result.username
        options.db_passwd = result.password
        options.db_host = result.hostname
    return options


if __name__ == '__main__':
    options = process_cmdline()
    with psycopg2.connect(dbname=options.db_name, user=options.db_user,
                          host=options.db_host, password=options.db_passwd) as db:
        with db.cursor() as cur:
            salt = bcrypt.gensalt()
            pw_hash = bcrypt.hashpw(options.password.encode('utf-8'), salt).decode('ascii')

            cur.execute("UPDATE public.user set password_hash = '{}', \
            invalid_login_attempts = 0 where username = '{}'".format(pw_hash, options.username))
    db.close()



