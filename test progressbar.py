from mpfd import make_parallel
import time
import random


@make_parallel
def my_function(param):
    time.sleep(random.randint(1, 5))


my_function(
    [
        "Hello, parallel world!1",
        "Hello, parallel world!2",
        "Hello, parallel world!3",
        "Hello, parallel world!4",
        "Hello, parallel world!5",
        "Hello, parallel world!6",
        "Hello, parallel world!7",
        "Hello, parallel world!8",
        "Hello, parallel world!9",
        "Hello, parallel world!10",
    ]
)
