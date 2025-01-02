import json
import os
import pickle

import boto3
import numpy as np
import pandas as pd
from ticket_closure_lib.transformers import (  # noqa: F401
    DateColTransformer,
    FeatureRemover,
    OrdinalConverter,
)


class TicketPredictor:
    def __init__(self, model_file="model.pkl"):
        with open(model_file, "rb") as f:
            self.mod = pickle.load(f)
        self.columns = [
            "reassignment_count",
            "reopen_count",
            "sys_mod_count",
            "opened_at",
            "sys_created_at",
            "sys_updated_at",
            "contact_type",
            "location",
            "category",
            "subcategory",
            "u_symptom",
            "cmdb_ci",
            "impact",
            "urgency",
            "priority",
            "assignment_group",
            "u_priority_confirmation",
            "notify",
            "problem_id",
        ]

    def predict_json(self, in_data):
        if isinstance(in_data, dict):
            in_data = [in_data]
        assert isinstance(in_data, list), "Input data should be a list of dictionaries"
        in_df = pd.DataFrame.from_records(in_data)
        # make sure column order is right
        in_df = in_df[self.columns]
        for date_col in ["opened_at", "sys_created_at", "sys_updated_at"]:
            in_df[date_col] = pd.to_datetime(in_df[date_col], format="%d/%m/%Y %H:%M")
        preds = self.mod.predict(in_df)
        return list(np.round(preds, 2))


def lambda_handler(event, context):
    model_file = "/tmp/model.pkl"
    if not os.path.isfile(model_file):
        print("file not found, getting it from S3")
        S3 = boto3.resource("s3")
        S3.meta.client.download_file(
            os.environ["TRAINING_ARTIFACT_BUCKET"], os.environ["MODEL_FILE"], model_file
        )
    predictor = TicketPredictor(model_file=model_file)
    return {"predictions": predictor.predict_json(event["data"])}


if __name__ == "__main__":
    with open("test-preds.json", "r") as f:
        pred_json = {"data": json.loads(f.read())}
    print(lambda_handler(event=pred_json, context=False))
