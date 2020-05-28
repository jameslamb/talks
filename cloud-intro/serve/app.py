import importlib
import json
import falcon
import os

from lambdas.predict import TicketPredictor


class PredictionEndpoint(object):
    def __init__(self):
        self.model = TicketPredictor(
            "model.pkl"
        )

    def on_post(self, req, resp):
        """
        Given a POST request, grab the JSON
        data attached to it, call the model on it,
        and return predictions.
        """
        if req.content_length:
            in_data = json.load(req.stream)
        else:
            resp.status = falcon.HTTP_400
            return
        resp.body = json.dumps(self.model.predict_json(in_data))

# for each function, create an endpoint with the function name
app = falcon.API()
app.add_route(f"/api/predict", PredictionEndpoint())
