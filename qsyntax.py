import prodigy
from prodigy.components.loaders import JSONL

@prodigy.recipe(
    "qsyntax",
    dataset=("Dataset to save answers to", "positional", None, str),
    file_path=("Path to texts", "positional", None, str),
)
def qsyntax(dataset, file_path):
    
    #VIEW 
    blocks = [
        {"view_id": "html"},         
        {"view_id": "choice", "html": None, "text":None}, 
        {"view_id": "text_input", "field_rows": 2, "field_label": 'Write any comments you might have'}]

    #STREAM
    stream = JSONL(file_path)
    stream = add_options(stream)
    
    return {
        "dataset": dataset,
        "view_id": "blocks",
        "stream": stream,
        "config": {
            #"options": ["options1"],
            #"options": ["options2"],
            "blocks": blocks,
        }
    }

def add_options(stream):
    options2 = [
        {"text": "Prefaced", "id": "prefaced"}, 
        {"text": "Non-Prefaced", "id": "nonprefaced"},
        {"text": "Other", "id": "other"}
    ]
    for task in stream:
        task["options"] = options2
        yield task
