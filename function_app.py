import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        url = 'https://burntlettuce.azurewebsites.net/api/http_trigger1?code=nB4JIZZcCKVj6gfNqF1gh5iaDe88iZ34NMBTvPEIEY7pAzFu_2zGrg%3D%3D'
        # url = 'https://api.github.com/users'
        response = requests.get(url)

        if response:
            return func.HttpResponse(f"Hello, {response.json()}. This HTTP triggered function executed successfully.")
        else:
            return func.HttpResponse(
                "This HTTP triggered function executed successfully. Pass a response in the query string or in the request body for a personalized response.",
                status_code=200
            )
    except Exception as e:
        logging.error(f"Error processing response: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
