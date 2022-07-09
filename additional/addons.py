list_of_addons = ['<link rel="stylesheet" href="/static/shed.css">',
                  '<link rel="stylesheet" href="https://temnomor.ru/static/shed.css">',
                  '<link rel="shortcut icon" href="{{ url_for("static", filename="favicon.ico") }}">',
                  '<meta http-equiv="refresh" content="120">',
                  '<div class="comm2"><span class="session_example">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>  - сессия</div>',
                  '<div class="comm2"><span class="practice_example">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>  - производственная практика</div>',
                  '<div class="comm2"><span class="GIA_example">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>  - ГИА</div>']


groups_addon = ''.join(list_of_addons)
teachers_and_cabinets_addon = ''.join([x for x in list_of_addons if x not in (list_of_addons[-1], list_of_addons[-2])])