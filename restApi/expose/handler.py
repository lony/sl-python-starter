from __future__ import print_function

import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

# this adds the component-level `lib` directory to the Python import path
import sys, os
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

# import the shared library, now anything in component/lib/__init__.py can be
# referenced as `lib.something`
import lib
# https://github.com/jkehler/awslambda-psycopg2
import psycopg2


def handler_func(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    conn = psycopg2.connect(
            host="host",
            user="username",
            password="password",
            database="database",
    )

    with conn.cursor() as c:
        # Get total
        c.execute("""SELECT Count(*) FROM people""")
        sum = c.fetchone()[0]  # first row, and column

    conn.commit()
    conn.close()
    return json.dumps(sum)
