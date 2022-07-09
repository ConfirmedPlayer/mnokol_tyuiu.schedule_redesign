from additional.addons import groups_addon, teachers_and_cabinets_addon
from additional.schedule_links import (
    group_schedule_url,
    teachers_schedule_url,
    cabinets_schedule_url
)

from flask import Flask, render_template, redirect, request
import aiofiles
import aiohttp
import asyncio
import datetime


app = Flask(__name__)
app.config.update(
    DEBUG=False,
    TEMPLATES_AUTO_RELOAD=True
)


async def get_schedule_by_group_name(group, sid, gr, year):
    schedule_link = group_schedule_url.format(sid=sid,
                                              gr=gr,
                                              year=year)
    filename = group + '.html'

    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(schedule_link) as response:
            html = await response.text()

    async with aiofiles.open(f'templates/groups/{filename}', 'w', encoding='UTF-8') as temp:
        await temp.write(html + groups_addon + f'<title>{group}</title>')

    return filename


async def get_schedule_by_teacher_name(teacher, teacher_id, year):
    schedule_link = teachers_schedule_url.format(teacher_id=teacher_id,
                                                 year=year)
    filename = teacher + '.html'

    timeout = aiohttp.ClientTimeout(total=100)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(schedule_link) as response:
            html = await response.text()

    async with aiofiles.open(f'templates/teachers/{filename}', 'w', encoding='UTF-8') as temp:
        await temp.write(html + teachers_and_cabinets_addon + f'<title>{teacher}</title>')

    return filename


async def get_schedule_by_cabinet_name(cabinet, cabinet_id, year):
    schedule_link = cabinets_schedule_url.format(cabinet_id=cabinet_id,
                                                 year=year)
    filename = cabinet + '.html'

    timeout = aiohttp.ClientTimeout(total=100)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(schedule_link) as response:
            html = await response.text()

    async with aiofiles.open(f'templates/cabinets/{filename}', 'w', encoding='UTF-8') as temp:
        await temp.write(html + teachers_and_cabinets_addon + f'<title>{cabinet}</title>')

    return filename


@app.route('/')
async def index():
    return render_template('index/index.html')


@app.route('/data/groups')
async def data_groups():
    return render_template('data/groups_data.html')


@app.route('/data/teachers')
async def data_teachers():
    return render_template('data/teachers_data.html')


@app.route('/data/cabinets')
async def data_cabinets():
    return render_template('data/cabinets_data.html')


@app.route('/api/groups')
async def groups_api():
    group = request.args.get('group')
    sid = request.args.get('sid')
    gr = request.args.get('gr')

    year = datetime.datetime.now().year

    if group and len(group) in range(8, 20):
        try:
            filename = await get_schedule_by_group_name(group, sid, gr, year)
            return render_template(f'groups/{filename}')
        except asyncio.TimeoutError:
            return redirect(request.url)
    else:
        return redirect('/')


@app.route('/api/teachers')
async def teachers_api():
    teacher = request.args.get('teacher')
    teacher_id = request.args.get('teacher_id')

    year = datetime.datetime.now().year

    if teacher and teacher_id:
        try:
            filename = await get_schedule_by_teacher_name(teacher, teacher_id, year)
            return render_template(f'teachers/{filename}')
        except asyncio.TimeoutError:
            return redirect(request.url)
    else:
        return redirect('/')


@app.route('/api/cabinets')
async def cabinets_api():
    cabinet = request.args.get('cabinet')
    cabinet_id = request.args.get('cabinet_id')

    year = datetime.datetime.now().year

    if cabinet and cabinet_id:
        try:
            filename = await get_schedule_by_cabinet_name(cabinet, cabinet_id, year)
            return render_template(f'cabinets/{filename}')
        except asyncio.TimeoutError:
            return redirect(request.url)
    else:
        return redirect('/')


@app.errorhandler(404)
async def page_not_found(_):
    return redirect('/')
