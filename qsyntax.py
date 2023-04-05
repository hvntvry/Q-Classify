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
        {"view_id": "classification", "html": None, "text":None},
        {"view_id": "choice", "html": None, "text":None, "label":None}, 
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
    options1 = "prefaced"
    
    options2 = [
        {"text": "Topic Extension", "id": "extension"}, 
        {"text": "Topical Shift", "id": "shift"},
        {"text": "Reformulation", "id": "reformulation"}, 
        {"text": "Challenge", "id": "challenge"},
        {"text": "Other", "id": "other"}
    ]
    for task in stream:
        task["label"] = options1
        task["options"] = options2
        yield task