import requests
def main():

    url = "http://localhost:8000/api"
    # client = {
    # "lead_source": "organic_search",
    # "number_of_courses_viewed": 4,
    # "annual_income": 80304.0
    # }
    client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
    }
    response = requests.post(url, json=client).json()
    print(response)


if __name__ == '__main__':
    main()