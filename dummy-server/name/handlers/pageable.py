from .data_pool import DataListSerializer

def init_pageable_info(data : list, page : int, page_size : int) -> dict:
    return {
        "sort" : {
            "sorted": False,
            "unsorted": True,
            "empty": True
        },
        "pageNumber" : page,
        "pageSize" : page_size,
        "offset" : page * page_size,
        "paged" : True,
        "unpaged" : False
    }

def init_content_metainfo(data : list, size : int) -> dict:
    return {
        "last" : False,
        "number": 0,
        "totalElements": len(data),
        "totalPages": len(data) // size,
        "size": size,
        "first": True,
        "numberOfElements": size,
        "empty": False if len(data) == 0 else True
    }

class Pageable():
    def __init__(self, list : list, page : int, page_size : int, sort_standard : str = "views") -> None:
        self.list : list = list
        self.pageable_info : dict = init_pageable_info(self.list, page, page_size)
        self.content_metainfo : dict = init_content_metainfo(self.list, page_size)
        self.sort_by(sort_standard)

    def sort_by(self, key, direction = "ASC"):
        isReversed = False if direction == "ASC" else True if direction == "DESC" else False
        
        def checkFlagSorted(self):
            self.pageable_info["sort"] = {
                "sorted": True,
                "unsorted": False,
                "empty": False
            }

        if len(self.list) == 0:
            self.pageable_info["sort"] = {
                "sorted": False,
                "unsorted": True,
                "empty": True
            }
            return

        if key == "views":
            self.list.sort(key=lambda x: x.views, reverse=isReversed)
            checkFlagSorted(self)
        elif key == "recomment":
            self.list.sort(key=lambda x: x.recomment, reverse=isReversed)
            checkFlagSorted(self)
        elif key == "lastest":
            self.list.sort(key=lambda x: x.created_at, reverse=isReversed)
            checkFlagSorted(self)
        else:
            pass

    def to_dict(self):
        return {
            "content": DataListSerializer.convert(self.list),
            "Pageable": self.pageable_info,
            "totalPages": self.content_metainfo["totalPages"],
            "totalElements": self.content_metainfo["totalElements"],
            "last": self.content_metainfo["last"],
            "number": self.content_metainfo["number"],
            "sort": self.pageable_info["sort"],
            "size": self.content_metainfo["size"],
            "numberOfElements": self.content_metainfo["numberOfElements"],
            "first": self.content_metainfo["first"],
            "empty": self.content_metainfo["empty"]
        }