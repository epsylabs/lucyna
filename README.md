# Lucyna
[![PyPI](https://img.shields.io/pypi/v/lucyna.svg)](https://pypi.org/project/lucyna/) ![](https://img.shields.io/pypi/pyversions/lucyna.svg) ![](https://img.shields.io/pypi/l/lucyna.svg)

Lucyna is a library that tries to help you with your daily tasks with AWS ECS and AWS Lambda (more might come in future).

## Screenshots
<a href="https://user-images.githubusercontent.com/164009/127609861-145265c3-5b1a-4ed2-a55b-2d400f7b0975.png" title="Dashboard"><img width="150" alt="Dashboard" src="https://user-images.githubusercontent.com/164009/127609795-ac1a5684-a334-418b-932f-15880bfe7066.png"></a>
<a href="https://user-images.githubusercontent.com/164009/127610177-ca44d337-a2a3-469b-b413-8221e9c4598e.png" title="Cluster listing"><img width="150" alt="Cluster listing" src="https://user-images.githubusercontent.com/164009/127610175-c3ebd211-dc65-4770-8f69-360c1fb5bf89.png"></a>
<a href="https://user-images.githubusercontent.com/164009/127610437-3d2f153e-7554-4284-9454-cfed8e2a3ac8.png" title="Serices list"><img width="150" alt="Services list" src="https://user-images.githubusercontent.com/164009/127610439-e8d0b543-3062-47c8-918f-4edd30bdf6eb.png"></a>

## Summary of functionalities
### ECS
#### Cluster
* <a href="https://user-images.githubusercontent.com/164009/127610177-ca44d337-a2a3-469b-b413-8221e9c4598e.png">Listing of all clusters</a>
#### Service
* <a href="https://user-images.githubusercontent.com/164009/127610437-3d2f153e-7554-4284-9454-cfed8e2a3ac8.png">Listing of all services</a>
* <a href="https://user-images.githubusercontent.com/164009/127609861-145265c3-5b1a-4ed2-a55b-2d400f7b0975.png">Dashboard</a>, which includes `CPUUtilization` and `MemoryUtilization` plots for service (refreshed automatically)
#### Task
* Run task, returns information about ran task, e.g. logs output from it (refreshed automatically)
* Listing of all running tasks
* Show single task, displays information about running task (refreshed automatically)
* Show task's logs (refreshed automatically)
### Lambda
* Listing of all lambdas

More detailed information about available commands below.

## Installation & usage

### As python package
```shell
pip install lucyna

lucyna

# with aws-vault
aws-vault exec my-aws-profile -- lucyna 
```

### With docker
```shell
# build image
docker build -t lucyna

docker run -it --rm --name lucyna lucyna ecs

# with aws-vault
docker run -it --rm --env-file <(aws-vault exec my-aws-profile -- env | grep "^AWS_") --name lucyna lucyna ecs
```

## What `lucyna` can do?
### ECS
#### Cluster
#### List of available clusters
```shell
lucyna ecs cluster list
```

#### Service
#### List of available services
```shell
lucyna ecs service list [OPTIONS]

Options:
  -c, --cluster TEXT
```

#### Dashboard for service
```shell
lucyna ecs service dashboard [OPTIONS] SERVICE

Options:
  -c, --cluster TEXT
```

#### Task
#### Run task
```shell
lucyna ecs task run [OPTIONS] TASK_DEFINITION [COMMAND]...

Options:
  -c, --cluster TEXT
  --network-configuration TEXT
  --capacity-provider-strategy TEXT
```

`TASK_DEFINITION` - you can either provide full definition e.g. `my-definition:123` or just name, `my-definition`. If no number is provided, latest version is assumed.

`[COMMAND]` - any command that should be executed on ECS task

Examples:

**Running with Fargate**
```shell
lucyna ecs task run epsy-dynks --capacity-provider-strategy '{"capacityProvider": "FARGATE"}' --network-configuration '{"awsvpcConfiguration":{"subnets":["subnet-1234567890"],"securityGroups":["sg-123456789"],"assignPublicIp":"DISABLED"}}' --  my_command subcommand --one-option --another-option="test"
```

#### List of running tasks
```shell
lucyna ecs task list [OPTIONS]

Options:
  -c, --cluster TEXT
```

#### Display information about ran task
```shell
lucyna ecs task show [OPTIONS] TASK_ID

Options:
  -c, --cluster TEXT
```

#### Display task logs
```shell
lucyna ecs task logs [OPTIONS] TASK_ID

Options:
  -c, --cluster TEXT
```

### Lambda
#### List of available lambdas
```shell
lucyna lambda list [OPTIONS]

Options:
  --region TEXT  Region e.g. us-east-2
```


## Can I use grep?
Yes! All commands results (but dashboards) can be filtered with `grep`
