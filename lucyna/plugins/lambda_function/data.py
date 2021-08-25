from ...context import ContextObject


def fetch_listing(context: ContextObject, click_params):
    lambda_client = context.lambda_function(click_params["region"])
    paginator = lambda_client.get_paginator("list_functions")

    for page in paginator.paginate():
        yield page["Functions"]
