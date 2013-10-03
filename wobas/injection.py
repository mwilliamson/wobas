import random

import zuice

from . import templating


def create_bindings():
    bindings = zuice.Bindings()
    
    bindings.bind("random").to_instance(random)
    bindings.bind(templating.Templates).to_instance(templating.templates())
    
    return bindings
    

def get(*args, **kwargs):
    injector = zuice.Injector(create_bindings())
    return injector.get(*args, **kwargs)
