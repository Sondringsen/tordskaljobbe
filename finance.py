import requests
import sys

def get_financials(ticker: str) -> str:
    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/%s" %ticker

    headers = {
        "X-RapidAPI-Key": "4c595d1183msh8acc46aeea31ee7p1dc3b0jsn046b73034b60",
        "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()[0]
    # response = requests.get(url)['quoteResponse']['result'][0]
    relevant_headers = ['shortName', 'marketCap', 'trailingPE', 'priceToBook', 'epsTrailingTwelveMonths']
    relevant_data = {}
    for header in relevant_headers:
        relevant_data[header] = response[header]
    
    return_string = "Financial summary of " + relevant_data['shortName'] + ' is: \n'
    data_strings = [(str(key) +  ': ' + str(relevant_data[key]) + '\n') for key in relevant_data.keys()]
    return_string += ''.join(data_strings)

    return return_string




# ticker = sys.argv[1]

financial_summary = get_financials(ticker='tsla')
print(financial_summary)



