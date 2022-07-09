from schedule_links import schedule_menu_url as schedule_url

from bs4 import BeautifulSoup
from loguru import logger
from pyppeteer import launch
import aiofiles
import asyncio


@logger.catch
async def parse_groups(page_loading_delay: int | float):
    """
    Находит все HTML-тэги с группами МПК ТИУ


    Возвращает (записывает в .html) <a> тэги с атрибутами sid, gr, id, где:

    sid — сид группы (число в районе 244 - 247 и т.д.) \n
    gr — уникальный идентификатор группы. Нужен для получения расписания по api \n
    id — id = название группы


    page_loading_delay нужен для того чтобы дать полностью загрузиться JS и самой странице.
    Группы, как правило, загружаются намного быстрее, чем преподаватели и кабинеты
    """
    while True:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(schedule_url)
        await asyncio.sleep(page_loading_delay)
        html = await page.content()

        while '(9)' not in rf'{html}' or '(11)' not in rf'{html}':
            logger.info('Groups not found in HTML. Trying again')

            await page.goto(schedule_url)
            await asyncio.sleep(page_loading_delay)
            html = await page.content()

            await asyncio.sleep(300)
        else:
            logger.info('Groups found in HTML')

        soup = BeautifulSoup(html, 'lxml')
        zero_group = soup.find('option').find_next()
        all_groups = zero_group.find_next_siblings()

        async with aiofiles.open('../templates/data/groups_data.html',
                                 'w',
                                 encoding='UTF-8') as temp:
            data = ''
            for group_tag in all_groups:
                group_tag_attributes = soup.find('option', string=group_tag.text).attrs
                sid = group_tag_attributes.get('sid')
                gr = group_tag_attributes.get('value')

                data += f'<a id="{group_tag.text}" sid="{sid}" gr="{gr}" \
                    onclick="updateName(this)">{group_tag.text}</a>'

            await temp.write(data)

        await browser.close()

        logger.info('Groups was parsed successfully')

        await asyncio.sleep(200_000)


@logger.catch
async def parse_teachers(page_loading_delay: int | float):
    """
    Находит все HTML-тэги с преподавателями МПК ТИУ \n
    Игнорирует расписание сразу нескольких преподавателей по типу: \n
    Иванов И.И. / Петрова Б.А, Королев О.А. и т.д.


    Возвращает (записывает в .html) <a> тэги с атрибутами value, id, где:

    value — уникальный идентификатор преподавателя. Нужен для получения расписания по api \n
    id — id = инициалы преподавателя


    page_loading_delay нужен для того чтобы дать полностью загрузиться JS и самой странице.
    """
    while True:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(schedule_url)
        await asyncio.sleep(page_loading_delay)
        html = await page.content()

        while 'Преподаватели' not in rf'{html}':
            logger.info('Teachers not found in HTML. Trying again')

            await page.goto(schedule_url)
            await asyncio.sleep(page_loading_delay)
            html = await page.content()

            await asyncio.sleep(300)
        else:
            logger.info('Teachers found in HTML')

        soup = BeautifulSoup(html, 'lxml')
        zero_teacher = soup.find('option', {'id': 'prep0', 'value': '0'}).find_next()
        all_teachers = zero_teacher.find_next_siblings()

        async with aiofiles.open('../templates/data/teachers_data.html',
                                 'w',
                                 encoding='UTF-8') as temp:
            data = ''
            for teacher_tag in all_teachers:
                if ',' in teacher_tag.text or '/' in teacher_tag.text:
                    continue
                else:
                    teacher_name = teacher_tag.text

                teacher_tag_attributes = soup.find('option', string=teacher_tag.text).attrs
                value = teacher_tag_attributes.get('value')

                data += f'<a id="{teacher_name}" value="{value}" \
                    onclick="updateName2(this)">{teacher_name}</a>'

            await temp.write(data)

        await browser.close()

        logger.info('Teachers was parsed successfully')

        await asyncio.sleep(200_000)


@logger.catch
async def parse_cabinets(page_loading_delay: int | float):
    """
    Находит все HTML-тэги с кабинетами отделений МПК ТИУ


    Возвращает (записывает в .html) <a> тэги с атрибутами value, id, где:

    value — уникальный идентификатор кабинета. Нужен для получения расписания по api \n
    id — id = название кабинета


    page_loading_delay нужен для того чтобы дать полностью загрузиться JS и самой странице.
    """
    while True:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(schedule_url)
        await asyncio.sleep(page_loading_delay)
        html = await page.content()

        while 'Все кабинеты' not in rf'{html}':
            logger.info('Cabinets not found in HTML. Trying again')

            await page.goto(schedule_url)
            await asyncio.sleep(page_loading_delay)
            html = await page.content(page_loading_delay)

            await asyncio.sleep(300)
        else:
            logger.info('Cabinets found in HTML')

        soup = BeautifulSoup(html, 'lxml')
        zero_cabinet = soup.find('option', {'id': 'cab0', 'value': '0'}).find_next()
        all_cabinets = zero_cabinet.find_next_siblings()

        async with aiofiles.open('../templates/data/cabinets_data.html',
                                 'w',
                                 encoding='UTF-8') as temp:
            data = ''
            for cabinet_tag in all_cabinets:
                cabinet_tag_attributes = soup.find('option', string=cabinet_tag.text).attrs
                value = cabinet_tag_attributes.get('value')

                data += f'<a id="{cabinet_tag.text}" value="{value}" \
                    onclick="updateName3(this)">{cabinet_tag.text}</a>'

            await temp.write(data)

        await browser.close()

        logger.info('Cabinets was parsed successfully')

        await asyncio.sleep(200_000)


async def main():
    tasks = []

    tasks.append(asyncio.create_task(parse_groups(10)))
    tasks.append(asyncio.create_task(parse_teachers(30)))
    tasks.append(asyncio.create_task(parse_cabinets(30)))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
