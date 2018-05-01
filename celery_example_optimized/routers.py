def new_router(name, args, kwargs, options, task=None):
    return {
        'exchange': 'smart',
        'routing_key': name,
    }
