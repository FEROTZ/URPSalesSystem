from ..dto import InternalErrorSchema, ControlledErrorSchema


class Documentation:
    def __init__(self) -> None:
        pass

    def create(success: dict):
        documentation = {}
        try:
            documentation[200] = {"model": success}
            documentation[404] = {"model": ControlledErrorSchema}
            documentation[500] = {"model": InternalErrorSchema}
        except:
            pass
        return documentation