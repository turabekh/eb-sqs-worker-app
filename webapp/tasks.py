from eb_sqs_worker.decorators import task

def handle_first_task(**kwargs):
    print("I am handling first task")
    print(kwargs)