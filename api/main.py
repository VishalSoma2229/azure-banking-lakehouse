from fastapi import FastAPI, HTTPException
import pandas as pd
import json

app = FastAPI(
    title="Banking Customer and Loan API",
    version="1.0.0"
)

CUSTOMER_FILE = "datasets/source/customer/CUSTOMER_MASTER.csv"
LOAN_FILE = "datasets/source/loan/LOAN_MASTER.csv"


# Load data once when the API starts
customers_df = pd.read_csv(CUSTOMER_FILE, dtype=str)
loans_df = pd.read_csv(LOAN_FILE, dtype=str)


@app.get("/")
def root():
    return {
        "message": "Banking API is running",
        "endpoints": [
            "/customers",
            "/customers/{customer_id}",
            "/loans",
            "/loans/{loan_id}"
        ]
    }


@app.get("/customers")
def get_customers():
    return json.loads(
        customers_df.to_json(orient="records")
    )


@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    customer = customers_df[
        customers_df["customer_id"] == customer_id
    ]

    if customer.empty:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return json.loads(
        customer.iloc[0].to_json()
    )


@app.get("/loans")
def get_loans():
    return json.loads(
        loans_df.to_json(orient="records")
    )


@app.get("/loans/{loan_id}")
def get_loan(loan_id: str):
    loan = loans_df[
        loans_df["loan_id"] == loan_id
    ]

    if loan.empty:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    return json.loads(
        loan.iloc[0].to_json()
    )