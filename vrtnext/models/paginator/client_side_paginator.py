from typing import Any, Dict

from vrtnext.abc.virtual_paginator import PaginationOptions, VirtualPaginator


class ClientSidePaginator(VirtualPaginator):
    """
    Best suited for REST API that does not implemented Pagination. This paginator will fetch all data from find_all method in your VirtualDAO implementation.
    if the REST API already have pagination implementation please map them by yourself instead. this Paginator cannot be used by DatabaseContext. please use Postgresql or MariaDB Paginator instead.
    This Paginator must be used along ClientSideFilters and RestContext.
    """

    def pagination_mapper(self, options: PaginationOptions) -> Dict[str, Any]:
        return {"is_client_side_paginator": True, **options.model_dump()}
