# eensa_aquatic_predictor
Prediction Scripts for eEnSa aquatic organisms

<b> Development Version for Test Users </b>

## Use
### Authentication
Create a <i>configuration.json</i> file in the working directory:

```
{
    "username": "xxxxxx",
    "password": "xxxxxx"
}
```
Enter your credentials accordingly.

### Predict

```
python eEnSa_chiro_predict.py
```

Make sure to have the input_data.csv in the same directory


## Model Infos:

Find an interactive Dashboard,Interface and Documentation for model prediction here:

[Interactive Dashboard](https://apps.prodknime.dywopla.int.bayer.com/d/Chiro%20Prediction%20Interactive%20(vAChT)~data-app:95c43d94-6339-4923-860f-0882f5e80c66/da9c1fff-1105-4463-9b1f-b8d9d7f76950/run)
Basic Model Performance on Hold-Out Set:

R^2: 0.754
MAE: 0.544 
RMSE: 0.703

