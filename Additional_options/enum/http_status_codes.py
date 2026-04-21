from enum import Enum

class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        code_dict = {
            HTTPStatusCodes.CONTINUE: "информация",
            HTTPStatusCodes.OK: "успех",
            HTTPStatusCodes.USE_PROXY: "перенаправление",
            HTTPStatusCodes.NOT_FOUND: "ошибка клиента",
            HTTPStatusCodes.BAD_GATEWAY: "ошибка сервера"
        }

        return code_dict.get(self)


# Входные данные1
print(HTTPStatusCodes.OK.info())
print(HTTPStatusCodes.OK.code_class())

# Выходные данные1
# ('OK', 200)
# успех

