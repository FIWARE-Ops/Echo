#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
from argparse import ArgumentParser
from asyncio import set_event_loop_policy
from uvloop import EventLoopPolicy
from yajl import dumps

routes = web.RouteTableDef()


@routes.get('/version')
async def handle(request):
    reply = {
        "orion": {
            "version": "1.8.0",
            "uptime": "",
            "git_hash": "",
            "compile_time": "",
            "compiled_by": "",
            "compiled_in": "",
            "release_date": "",
            "doc": ""
        }
    }
    return web.Response(text=dumps(reply, indent=4), content_type='application/json')


@routes.get('/v2')
async def handle(request):
    reply = {
        "entities_url": "/v2/entities",
        "types_url": "/v2/types",
        "subscriptions_url": "/v2/subscriptions",
        "registrations_url": "/v2/registrations"
    }
    return web.Response(text=dumps(reply, indent=4), content_type='application/json')


# Entities
@routes.get('/v2/entities')
async def handle(request):
    return web.HTTPOk()


@routes.post('/v2/entities')
async def handle(request):
    return web.HTTPCreated() ## 204 also


@routes.get('/v2/entities/{entityId}')
async def handle(request):
    return web.HTTPOk()


@routes.post('/v2/entities/{entityId}')
async def handle(request):
    return web.HTTPNoContent()


@routes.delete('/v2/entities/{entityId}')
async def handle(request):
    return web.HTTPNoContent()


@routes.get('/v2/entities/{entityId}/attrs')
async def handle(request):
    return web.HTTPOk()


@routes.put('/v2/entities/{entityId}/attrs')
async def handle(request):
    return web.HTTPNoContent()


@routes.post('/v2/entities/{entityId}/attrs')
async def handle(request):
    return web.HTTPNoContent()


@routes.patch('/v2/entities/{entityId}/attrs')
async def handle(request):
    return web.HTTPNoContent()


# Attributes
@routes.get('/v2/entities/{entityId}/attrs/{attrName}')
async def handle(request):
    return web.HTTPOk()


@routes.put('/v2/entities/{entityId}/attrs/{attrName}')
async def handle(request):
    return web.HTTPOk()


@routes.delete('/v2/entities/{entityId}/attrs/{attrName}')
async def handle(request):
    return web.HTTPNoContent()

# Attribute Value
@routes.get('/v2/entities/{entityId}/attrs/{attrName}/value')
async def handle(request):
    return web.HTTPOk()


@routes.put('/v2/entities/{entityId}/attrs/{attrName}/value')
async def handle(request):
    return web.HTTPOk()

# Subscriptions
@routes.get('/v2/subscriptions')
async def handle(request):
    return web.HTTPOk()


@routes.post('/v2/subscriptions')
async def handle(request):
    return web.HTTPCreated()


@routes.get('/v2/subscriptions/{subscriptionId}')
async def handle(request):
    return web.HTTPOk()


@routes.delete('/v2/subscriptions/{subscriptionId}')
async def handle(request):
    return web.HTTPNoContent()


@routes.patch('/v2/subscriptions/{subscriptionId}')
async def handle(request):
    return web.HTTPNoContent()

# Registrations
@routes.get('/v2/registrations')
async def handle(request):
    return web.HTTPOk()


@routes.post('/v2/registrations')
async def handle(request):
    return web.HTTPCreated()


@routes.get('/v2/registrations/{registrationId}')
async def handle(request):
    return web.HTTPOk()


@routes.delete('/v2/registrations/{registrationId}')
async def handle(request):
    return web.HTTPNoContent()


@routes.patch('/v2/registrations/{registrationId}')
async def handle(request):
    return web.HTTPNoContent()

# Batch Operations
@routes.post('/v2/op/update')
async def handle(request):
    return web.HTTPNoContent()


@routes.post('/v2/op/query')
async def handle(request):
    return web.HTTPOk()


@routes.post('/v2/op/notify')
async def handle(request):
    return web.HTTPOk()

# Legacy v1
@routes.post('/v1/updateContext')
async def handle(request):
    return web.HTTPOk()


@routes.get('/{tail:.*}')
async def handle(request):
    print(request.raw_path)
    return web.Response(text=request.method + ' ' + request.raw_path + '\n', status=404)


@routes.post('/{tail:.*}')
async def handle(request):
    print(request.raw_path)
    return web.Response(text=request.method + ' ' + request.raw_path + '\n', status=404)


@routes.put('/{tail:.*}')
async def handle(request):
    print(request.raw_path)
    return web.Response(text=request.method + ' ' + request.raw_path + '\n', status=404)


@routes.patch('/{tail:.*}')
async def handle(request):
    print(request.raw_path)
    return web.Response(text=request.method + ' ' + request.raw_path + '\n', status=404)


@routes.delete('/{tail:.*}')
async def handle(request):
    print(request.raw_path)
    return web.Response(text=request.raw_path + '\n', status=404)


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--path', dest="path", action="store")

    args = parser.parse_args()

    set_event_loop_policy(EventLoopPolicy())

    app = web.Application()
    app.add_routes(routes)

    web.run_app(app, path=args.path)
