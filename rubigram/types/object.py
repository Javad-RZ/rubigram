import sys
from typing import Union, TypeVar, Type, get_origin, get_args, get_type_hints
from dataclasses import dataclass, fields
from json import dumps

T = TypeVar("T", bound="Object")


@dataclass
class Object:

    def asdict(self):
        data = {}
        for f in fields(self):
            value = getattr(self, f.name)
            if isinstance(value, Object):
                inner = value.asdict()
                data[f.name] = {"_": value.__class__.__name__, **inner}
            elif isinstance(value, list):
                data[f.name] = [
                    {"_": v.__class__.__name__, **v.asdict()} if isinstance(v, Object) else v for v in value
                ]
            else:
                data[f.name] = value
        return data

    def jsonify(self, exclude_none: bool = False) -> str:
        def clear(obj):
            if isinstance(obj, dict):
                return {k: clear(v) for k, v in obj.items() if v is not None}
            elif isinstance(obj, list):
                return [clear(i) for i in obj if i is not None]
            else:
                return obj

        data = self.asdict()
        data.pop("client", None)
        if exclude_none:
            data = clear(data)
        return dumps(
            {"_": self.__class__.__name__, **data},
            ensure_ascii=False,
            indent=4
        )

    @classmethod
    def parse(cls: Type[T], data: dict) -> T:
        data = data or {}
        init_data = {}

        try:
            module = sys.modules[cls.__module__]
            type_hints = get_type_hints(
                cls, globalns=module.__dict__, localns=None)
        except Exception:
            type_hints = {}

        for field in fields(cls):
            raw_value = data.get(field.name)
            if isinstance(raw_value, dict) and "_" in raw_value:
                raw_value = {k: v for k, v in raw_value.items() if k != "_"}

            field_type = type_hints.get(field.name, field.type)
            origin = get_origin(field_type)

            if origin is Union:
                args = get_args(field_type)
                non_none_args = [arg for arg in args if arg is not type(None)]
                if len(non_none_args) == 1:
                    field_type = non_none_args[0]
                    origin = get_origin(field_type)
                else:
                    pass

            if isinstance(raw_value, dict) and isinstance(field_type, type) and issubclass(field_type, Object):
                init_data[field.name] = field_type.parse(raw_value)

            elif origin == list:
                inner_type = get_args(field_type)[0]
                inner_origin = get_origin(inner_type)
                if inner_origin is Union:
                    inner_args = [a for a in get_args(
                        inner_type) if a is not type(None)]
                    inner_type = inner_args[0] if inner_args else inner_type

                if isinstance(raw_value, list):
                    if isinstance(inner_type, type) and issubclass(inner_type, Object):
                        init_data[field.name] = [
                            inner_type.parse(v) if isinstance(v, dict) else v for v in raw_value
                        ]
                    else:
                        init_data[field.name] = raw_value
                else:
                    init_data[field.name] = [
                    ] if raw_value is None else raw_value

            elif origin is Union:
                args = get_args(field_type)
                obj_arg = next((arg for arg in args if isinstance(
                    arg, type) and issubclass(arg, Object)), None)
                if obj_arg and isinstance(raw_value, dict):
                    init_data[field.name] = obj_arg.parse(raw_value)
                else:
                    init_data[field.name] = raw_value

            else:
                init_data[field.name] = raw_value

        return cls(**init_data)

    def __str__(self):
        return self.jsonify(True)