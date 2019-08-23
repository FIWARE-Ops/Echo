#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
from argparse import ArgumentParser
import asyncio

routes_provisioning = web.RouteTableDef()
routes_south = web.RouteTableDef()


@routes_south.get('/')
async def handle(request):
    return web.Response(text='South', status=200)


@routes_provisioning.get('/')
async def handle(request):
    return web.Response(text='Provisioning', status=200)


@routes_provisioning.get('/iot/about')
async def handle(request):
    return web.HTTPOk()


@routes_provisioning.post('/iot/services')
async def handle(request):
    return web.HTTPCreated()


@routes_provisioning.get('/iot/services')
async def handle(request):
    return web.HTTPOk()


@routes_provisioning.post('/iot/devices')
async def handle(request):
    return web.HTTPCreated()


@routes_provisioning.get('/iot/devices')
async def handle(request):
    return web.HTTPOk()


async def start(host, port_south, port_provisioning):
    app_south = web.Application()
    app_south.router.add_routes(routes_south)
    runner_south = web.AppRunner(app_south)
    await runner_south.setup()
    site_south = web.TCPSite(runner_south, host, port_south)
    await site_south.start()

    print('Serving south')

    app_provisioning = web.Application()
    app_provisioning.router.add_routes(routes_provisioning)
    runner_provisioning = web.AppRunner(app_provisioning)
    await runner_provisioning.setup()
    site_provisioning = web.TCPSite(runner_provisioning, host, port_provisioning)
    await site_provisioning.start()

    print('Serving provisioning')

    print('Started')
    await asyncio.sleep(100*3600)


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--ip', dest="ip", default='0.0.0.0', help='ip address (default: 0.0.0.0)', action="store")
    parser.add_argument('--south', dest="south", default=7896, help='south port (default: 7896)', action="store")
    parser.add_argument('--provisioning', dest="provisioning", default=4096, help='provisioning port (default: 4096)',
                        action="store")

    args = parser.parse_args()

    try:
        asyncio.run(start(args.ip, args.south, args.provisioning))
    except KeyboardInterrupt:
        pass
