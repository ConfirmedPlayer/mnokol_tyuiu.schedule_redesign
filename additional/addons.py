list_of_addons = ['<link rel="stylesheet" href="/static/shed.css">',
                  '<link rel="stylesheet" href="https://temnomor.ru/static/shed.css">',
                  '<link rel="shortcut icon" href="{{ url_for("static", filename="favicon.ico") }}">',
                  '<script defer src="/static/shed.js"></script>'
                  '<meta http-equiv="refresh" content="120">',
                  '<div class="comm2"><span class="session_example">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>  - сессия</div>',
                  '<div class="comm2"><span class="practice_example">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>  - производственная практика</div>',
                  '<div class="comm2"><span class="GIA_example">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>  - ГИА</div>']


groups_addon = ''.join(list_of_addons)
teachers_and_cabinets_addon = ''.join([x for x in list_of_addons if x not in (list_of_addons[-1], list_of_addons[-2])])


pyppeteer_args = ['--no-sandbox',
                  '--disable-setuid-sandbox',
                  '--autoplay-policy=user-gesture-required',
                  '--disable-background-networking',
                  '--disable-background-timer-throttling',
                  '--disable-backgrounding-occluded-windows',
                  '--disable-breakpad',
                  '--disable-client-side-phishing-detection',
                  '--disable-component-update',
                  '--disable-default-apps',
                  '--disable-dev-shm-usage',
                  '--disable-domain-reliability',
                  '--disable-extensions',
                  '--disable-features=AudioServiceOutOfProcess',
                  '--disable-hang-monitor',
                  '--disable-ipc-flooding-protection',
                  '--disable-notifications',
                  '--disable-offer-store-unmasked-wallet-cards',
                  '--disable-popup-blocking',
                  '--disable-print-preview',
                  '--disable-prompt-on-repost',
                  '--disable-speech-api',
                  '--disable-sync',
                  '--hide-scrollbars',
                  '--ignore-gpu-blacklist',
                  '--metrics-recording-only',
                  '--mute-audio',
                  '--no-default-browser-check',
                  '--no-first-run',
                  '--no-pings',
                  '--no-zygote',
                  '--password-store=basic',
                  '--use-mock-keychain']