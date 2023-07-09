from .data_pool import DataListSerializer

# sort - sorted : 정렬 여부
# sort - unsorted : 정렬 안된 여부
# sort - empty : 정렬할 데이터가 없는지 여부 == (content.size == 0)
# pageNumber : 현재 페이지 번호
# pageSize : 페이지 크기
# offset : 페이지 시작 위치 (pageNumber * pageSize)
# paged : 페이지 여부
# unpaged : 페이지가 아닌지 여부
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

# sort - sorted : 전체 데이터의 정렬 여부
# sort - unsorted : 전체 데이터의 정렬 안된 여부
# sort - empty : 전체 데이터 중 정렬할 데이터가 없는지 여부 == (content.size == 0)
# last : 마지막 페이지 여부
# first : 첫번째 페이지 여부
# number : 현재 페이지 번호
# numberOfElements : 현재 페이지에서 요청이 들어왔을 때 조회된 데이터의 개수 (content.size)
# size : 페이지 크기
# totalElements : 전체 데이터 개수
# totalPages : 전체 페이지 개수
# empty : 조회된 데이터가 없는지 여부 (content.size == 0)
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