def handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': '<h1>Hello from Netlify Functions!</h1><p>This is a test function.</p>'
    }
