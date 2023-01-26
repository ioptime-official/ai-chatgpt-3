import csv
import json

# open the csv file
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# open the jsonl file
with open('finetuning_data_3.jsonl', 'w') as f:
    # iterate through each question-answer example
    for example in data:
        question = example[0]
        answer = example[1]
        # add the "->" suffix to the question
        question += "->"
        # write the fine-tuning data in jsonl format
        json.dump({"prompt": question, "completion": answer}, f)
        f.write('\n')
