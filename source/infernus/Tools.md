# TOOLS сервер
Основные инструменты сервиса
Не рекомендую менять этот файл

## Server
URL: localhost:5000

## Open Links
METHOD: POST /tools/open_link
BODY: url
REQUEST_MARKERS: открой, сайт, ссылку
PARAM_MARKERS: .com, .org, .ru

## Launch Apps
METHOD: POST /tools/launch_app
BODY: appname
REQUEST_MARKERS: открой, запусти
PARAM_MARKERS: steam, firefox, vs code

## Change Volume
METHOD: POST /tools/change_volume
REQUEST_MARKERS: увеличь, прибавь, уменьши, убавь
PARAM_MARKERS: 