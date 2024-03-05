## load test LLMs with Locust 

Locust, an open source load testing tool, is popular framework for load testing HTTP and other protocols. Its developer friendly approach lets you to define your tests in regular Python code.

Locust tests can be run from command line or using its web-based UI. Throughput, response times and errors can be viewed in real time and/or exported for later analysis.


https://docs.locust.io/en/stable/what-is-locust.html


In this code repository, we provide an example of how to perform load testing on the LLM API to evaluate your production requirements. The code is developed within a SageMaker Notebook and utilizes the command line interface to conduct load testing on both the SageMaker and Bedrock LLM API.

Once the locustfile.py is properly configured, you can initiate the load test by executing a command in the command line. This allows you to test the system with varying levels of throughput, depending on your specific requirements.

locust --headless --users 30 --spawn-rate 30 --run-time 120 --csv ./benchmark_metric/benchmark_u30


| Type     | Name       | # reqs | # fails     | Avg   | Min   | Max   | Med   | req/s | failures/s |
|----------|------------|--------|-------------|-------|-------|-------|-------|-------|------------|
| [Send]   | Prompt     | 390    | 0 (0.00%)   | 9232  | 2037  | 10282 | 9800  | 3.25  | 0.00       |
| Aggregated |             | 390    | 0 (0.00%)   | 9232  | 2037  | 10282 | 9800  | 3.25  | 0.00       |



See our examples of load testing the SageMaker model with `sagemaker_jumpstart_loadtest.ipynb` and the Bedrock model with `bedrock_loadtest.ipynb`. 



## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

