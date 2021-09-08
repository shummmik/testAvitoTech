import httpx
import asyncio
import re

RE = r" *(\d+)+ *"

CONNECTION = "Connection or request error: {}."
STATUS = "Error response {} while requesting {}."


class StructureException(Exception):
    def __init__(self):
        Exception.__init__(self, 'The structure is not quadratic!')


class ConnectionException(Exception):
    def __init__(self, text):
        Exception.__init__(self, text)


class StatusException(Exception):
    def __init__(self, text):
        Exception.__init__(self, text)


def sneil(array):
    lenList = len(array)
    N = int(lenList ** 0.5)
    if (N ** 2 != lenList):
        raise StructureException()
    res = []
    direction = 1
    row = 0
    col = 0
    while (lenList > 0):
        max = int((direction + 1) / 2) * (N - 1)
        while (row * direction - max <= 0):
            if array[row * N + col] in res:
                break
            res.append(array[row * N + col])
            lenList -= 1
            row += direction
        row -= direction
        col += direction

        while (col * direction - max <= 0):
            if array[row * N + col] in res:
                break
            res.append(array[row * N + col])
            lenList -= 1
            col += direction
        row -= direction
        col -= direction
        direction = direction * (-1)
        if (lenList == 0):
            break
    return res


async def get_matrix(url):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
        except httpx.RequestError as ex:
            raise ConnectionException(CONNECTION.format(ex.request.url)) from ex
        except httpx.HTTPStatusError as ex:
            raise StatusException(STATUS.format(ex.response.status_code,
                                          ex.request.url)) from ex
    listNums = re.findall(RE, response.text)
    listNums = list(map(int, listNums))
    lenList = len(listNums)
    if lenList == 0:
        return None
    if lenList == 1:
        return listNums

    return sneil(listNums)


