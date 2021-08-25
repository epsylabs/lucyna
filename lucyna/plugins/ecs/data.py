from ...utils import _paginate, grouper


def fetch_listing(
    ecs,
    paginator_type,
    arn_index,
    describe_function,
    describe_filter,
    result_key,
    grouper_limit=10,
    paginator_params=None,
):
    if not paginator_params:
        paginator_params = {}

    pagination = _paginate(
        ecs,
        paginator_type,
        **paginator_params,
    )

    arns = []
    for iterator in pagination:
        for task in iterator:
            arns.extend(task[arn_index])

    result = []
    for chunk in grouper(arns, grouper_limit):
        params = {**{describe_filter: list(filter(None, chunk)), **paginator_params}}
        result.extend(describe_function(**params)[result_key])

    return result
