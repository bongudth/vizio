from .services import useless

intro_text = """
We have a code snippet below, attach the summary to each line of code based "line_no" key.
Just output a dict "summary" explain complex group of nodes in this function with natural language related to flow chart.
Do not list 1. 2. 3. ... or - in your summary.
Convert variables to natural text. Dont use words 'Assign', 'Set' to describe.
"""

example_code = """

Format of JSON output:
```
{
    "L1": "Define a function quicksort with argument arr"
    ...
}
```
with L1 is line_no of code.
"""


def useless_prompt(prompt, **kwargs):
    gpt_response = useless.Completion.create(prompt=prompt, **kwargs)
    return gpt_response


@staticmethod
def you_summary_code(json_ast, **kwargs):
    snippet_code = f"""
    {json_ast}
    """
    prompt = intro_text + example_code + snippet_code
    response = useless_prompt(prompt=prompt, **kwargs)
    response = post_process_response(response)
    result = response.get("text")
    return result


def post_process_response(response):
    # remove before ``` and after ```
    # response = response.split("```")[1]
    # response = response.split("```")[0]
    # # remove \n
    # response = response.replace("\n", "")
    # # remove \"
    # response = response.replace('\\"', '"')
    # # remove \\
    # response = response.replace("\\\\", "\\")
    # # remove \\n
    # response = response.replace("\\n", "\n")
    return response
