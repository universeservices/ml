import argparse
import logging
from servicefoundry import Build, PythonBuild, Service, Resources, Port

logging.basicConfig(level=logging.INFO)

image = Build(
    build_spec=PythonBuild(
        command="uvicorn main:app --port 8000 --host 0.0.0.0",
        requirements_path="requirements.txt",
    )
)

service = Service(
    name="fastapi",
    image=image,
    ports=[Port(port=8000, host="fastapi-intern-pinak-8000.demo1.truefoundry.com")],
    resources=Resources(
        cpu_request=0.1,
        cpu_limit=0.1,
        memory_request=500,
        memory_limit=800,
        ephemeral_storage_limit=1200,
        ephemeral_storage_request=1000,
    ),
    env={
        "UVICORN_WEB_CONCURRENCY": "1",
        "ENVIRONMENT": "dev",
    },
)
service.deploy(workspace_fqn="tfy-gtl-demo-euwe1:intern-pinak")
