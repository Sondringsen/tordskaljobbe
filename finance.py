import requests
import sys

def get_financials(ticker: str) -> str:
    # url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/%s" %ticker

    # headers = {
    #     "X-RapidAPI-Key": "4c595d1183msh8acc46aeea31ee7p1dc3b0jsn046b73034b60",
    #     "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers).json()[0]
    # relevant_headers = ['shortName', 'marketCap', 'trailingPE', 'priceToBook', 'epsTrailingTwelveMonths']
    # string_headers = ['Company name', 'Market cap', 'PE (trailing)', 'PB', 'EPS (TTM)']
    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/financial-data"

    headers = {
        "X-RapidAPI-Key": "4c595d1183msh8acc46aeea31ee7p1dc3b0jsn046b73034b60",
        "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()['financialData']

    relevant_headers = ['currentPrice', 'recommendationMean', 'recommendationKey', 'numberOfAnalystOpinions', 
                            'totalCash', 'ebitda', 'totalDebt', 'totalRevenue', 'debtToEquity', 'returnOnEquity', 'grossProfits', 
                            'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 'profitMargins'] 
    string_headers = ['Current Price', 'Recommendation Mean', 'Recommendation Key', 'Number of Analyst Opinions', 'Total Cash',
                        'EBITDA', 'Total Debt', 'Total Revenue', 'Debt to Equity', 'Return on Equity', 'Gross Profit', 'Earnings Growth',
                        'Revenue Growth', 'Gross MArgins', 'EBTIDA Margins', 'Operating Margins', 'Profit Margins']
    relevant_data = {}
    for header in relevant_headers:
        # print(response[header])
        if header == 'recommendationKey':
            relevant_data[header] = response[header]
        else:
            relevant_data[header] = response[header]['fmt']
    
    return_string = "Financial summary of " + ticker + ' is: \n'
    data_strings = [(string_headers[i] +  ': ' + str(relevant_data[relevant_headers[i]]) + '\n') for i in range(len(relevant_headers))]
    return_string += ''.join(data_strings)

    return return_string




# ticker = sys.argv[1]

financial_summary = get_financials(ticker="aapl")
print(financial_summary)



