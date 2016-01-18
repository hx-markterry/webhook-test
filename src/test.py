#!/usr/bin/env python
from __future__ import print_function
import lambda_function

if __name__ == '__main__':
    event = {
      'A': 1
    }
    context = 1
    lambda_function.lambda_handler(event, context)