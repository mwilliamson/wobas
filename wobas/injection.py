import random

import zuice


def get(*args, **kwargs):
    bindings = zuice.Bindings()
    
    bindings.bind("random").to_instance(random)
    
    injector = zuice.Injector(bindings)
    return injector.get(*args, **kwargs)
