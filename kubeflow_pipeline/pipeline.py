import kfp
from kfp import dsl
from kfp.dsl import container_component, Input, Output, Dataset, Model


@container_component
def data_ingestion_op():
    return dsl.ContainerSpec(
        image="ahmadmajde22/colorectal-cancer-prediction-app:latest",
        command=["python", "src/data_ingestion.py"]
    )


@container_component
def data_processing_op():
    return dsl.ContainerSpec(
        image="ahmadmajde22/colorectal-cancer-prediction-app:latest",
        command=["python", "src/data_processing.py"]
    )


@container_component
def model_training_op():
    return dsl.ContainerSpec(
        image="ahmadmajde22/colorectal-cancer-prediction-app:latest",
        command=["python", "src/model_training.py"]
    )


@dsl.pipeline(
    name='Colorectal Cancer Prediction Pipeline',
    description='A pipeline for colorectal cancer prediction using machine learning.'
)
def colorectal_cancer_pipeline():
    ingest = data_ingestion_op()
    process = data_processing_op().after(ingest)
    train = model_training_op().after(process)


if __name__ == '__main__':
    from kfp import compiler
    compiler.Compiler().compile(
        pipeline_func=colorectal_cancer_pipeline,
        package_path='colorectal_cancer_pipeline.yaml'
    )
