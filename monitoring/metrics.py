from prometheus_client import start_http_server, Counter, Summary

TRANSACTION_COUNT = Counter('transaction_count', 'Number of processed transactions')
TRANSACTION_TIME = Summary('transaction_processing_time', 'Time to process a transaction')

def start_monitoring():
    start_http_server(8000)

@TRANSACTION_TIME.time()
def process_transaction_with_metrics(transaction):
    TRANSACTION_COUNT.inc()
    return transaction.process_transaction("Miner1")
