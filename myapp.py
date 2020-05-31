#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
from sanic import Sanic
import psycopg2
import time
from sanic_jinja2 import SanicJinja2
from python_paginate.css.semantic import Semantic
from python_paginate.web.sanic_paginate import Pagination

app = Sanic(__name__)

# update pagination settings
settings = dict(PREV_LABEL='<i class="left chevron icon"></i>',
                NEXT_LABEL='<i class="right chevron icon"></i>',
                PER_PAGE=10,  # default is 10
                DB_PATH="postgresql://root@localhost/dataset",
                )
app.config.update(settings)

jinja = SanicJinja2(app, autoescape=True)

# customize default pagination
if 'PREV_LABEL' in app.config:
    Semantic._prev_label = app.config.PREV_LABEL

if 'NEXT_LABEL' in app.config:
    Semantic._next_label = app.config.NEXT_LABEL

Pagination._css = Semantic()  # for cache
# or
# Pagination._css_framework = 'semantic'
# like above line, but little different
# if you want to get same result, need do below:
# pass css_prev_label, css_next_label to Pagination for initialize

Pagination._per_page = app.config.PER_PAGE


@app.route('/')
async def index(request):
    conn = psycopg2.connect(app.config.DB_PATH)
    #conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('select count(*) from data')
    total = cur.fetchone()[0]
    page, per_page, offset = Pagination.get_page_args(request)
    sql = 'select date, season, home, visitor, ft, hgoal, vgoal, division, tier, totgoal, goaldif, result from data offset {} limit {}'\
        .format(offset, per_page)
    starttime = time.time()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    exec_time = round((time.time() - starttime), 4)
    pagination = Pagination(request, total=total, record_name='data')
    return jinja.render('index.html', request, data=data, exec_time=exec_time, pagination=pagination)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
