def default_router(name, args, kwargs, options, task=None, **kw):
    return {
        'exchange': 'smart',
        'routing_key': name,
    }
