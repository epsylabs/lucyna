import itertools

from ecs_tool.exceptions import NoResultsException


def _paginate(ecs_client, service, **kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    paginator = ecs_client.get_paginator(service)
    pagination_config = {"MaxItems": 100, "PageSize": 100}

    resp = paginator.paginate(**kwargs, PaginationConfig=pagination_config)
    yield resp

    while "NextToken" in resp:
        yield paginator.paginate(
            {
                **kwargs,
                **{"PaginationConfig": pagination_config},
                **{"StartingToken": resp["NextToken"]},
            }
        )


def fetch_services(ecs_client, cluster, launch_type=None, scheduling_strategy=None):
    pagination = _paginate(
        ecs_client,
        "list_services",
        cluster=cluster,
        launchType=launch_type,
        schedulingStrategy=scheduling_strategy,
    )

    arns = []
    for iterator in pagination:
        for service in iterator:
            arns += service["serviceArns"]

    if not arns:
        raise NoResultsException

    describe_services = ecs_client.describe_services(cluster=cluster, services=arns)

    return describe_services["services"]


def fetch_tasks(
    ecs_client, cluster, status, service_name=None, family=None, launch_type=None
):
    if status == "ANY":
        pagination_running = _paginate(
            ecs_client,
            "list_tasks",
            cluster=cluster,
            desiredStatus="RUNNING",
            serviceName=service_name,
            family=family,
            launchType=launch_type,
        )

        pagination_stopped = _paginate(
            ecs_client,
            "list_tasks",
            cluster=cluster,
            desiredStatus="STOPPED",
            serviceName=service_name,
            family=family,
            launchType=launch_type,
        )

        pagination = itertools.chain(pagination_running, pagination_stopped)
    else:
        pagination = _paginate(
            ecs_client,
            "list_tasks",
            cluster=cluster,
            desiredStatus=status,
            serviceName=service_name,
            family=family,
            launchType=launch_type,
        )

    arns = []
    for iterator in pagination:
        for task in iterator:
            arns += task["taskArns"]

    if not arns:
        raise NoResultsException

    describe_services = ecs_client.describe_tasks(cluster=cluster, tasks=arns)

    return describe_services["tasks"]


def fetch_task_definitions(ecs_client, family, status):
    pagination = _paginate(
        ecs_client, "list_task_definitions", familyPrefix=family, status=status
    )

    arns = []
    for iterator in pagination:
        for task_definition in iterator:
            arns += task_definition["taskDefinitionArns"]

    if not arns:
        raise NoResultsException

    return arns
