import pickle
from fastapi import FastAPI
from pydantic import BaseModel

class Client(BaseModel):
     lead_source: str | None = None
     number_of_courses_viewed: int | None = None
     annual_income: float | None = None


def predict_single(customer, dv, model):
    X = dv.transform(customer)
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

with open('pipeline_v2.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)

app = FastAPI()

@app.post('/api')
def predict_api(customer : Client):
    customer = dict(customer)
    score = predict_single(customer, dv, model)
    return score

def main():
     
    customer = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
    }
    score = predict_single(customer, dv, model)
    print(score)




if __name__ == "__main__":
    main()
