# score-local

You can create your own model server locally. After running the steps in [TRAIN-LOCAL](./TRAIN-LOCAL.md),
do the following.

## Serve the model locally

```shell
gunicorn \
    --access-logfile=- \
    --error-logfile=- \
    serve:app
```

test making some predictions

```
python scripts/create_random_tickets.py 20 > preds.json

curl -X POST \
    -d @preds.json \
    http://localhost:8000/api/predict
```
