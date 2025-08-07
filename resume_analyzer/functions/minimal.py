from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Netlify Functions!'

def handler(event, context):
    try:
        import serverless_wsgi
        return serverless_wsgi.handle_request(app, event, context)
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
