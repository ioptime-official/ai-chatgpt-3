# Fine Tuning GPT-3

Fine-tuning GPT-3 involves the following steps:

## Preparing Data

GPT-3 accepts data in JSONL format, which contains a prompt with a separator and a completion. The format looks like:

`{"prompt": "<prompt text>", "completion": "<ideal generated text>"}`

The dataset of COVID-19 FAQs was collected from [Kaggle.](https://www.kaggle.com/datasets/xhlulu/covidqa?select=news.csv "Kaggle.") The csv consisted of multiple columns, out of which Questions and Answers column were extracted into a separate csv file.

In order to convert it to JSONL format which GPT-3 accepts, a [python script](https://github.com/ioptime-official/ai-chatgpt-3-fine-tuning/blob/main/convert.py "python script") was used. A **‘->’** separator was added after every prompt to let the model know where the prompt should end. The data after conversion looks like:

`{"prompt": "When should I get tested? ->", "completion": "Your doctor will tell you if you need to get tested."}
`

## Fine Tuning

To get started, the openai python dependency was installed using the following commands:

`pip install --upgrade openai`

`pip install openai[datalib]`

To prepare and load the data, the following command can be used:

`openai tools fine_tunes.prepare_data -f DATA_PATH
`

In order to link the API, run the following command:

`export OPENAI_API_KEY="PROVIDED API KEY"
`

At the end to start fine tuning, the following command can be executed, which contains the prepared JSONL file and the name of the model you need to fine-tune:

`openai api fine_tunes.create -t OPENAI_PREPARED_DATA_FILE -m MODEL_NAME
`
For COVID-19 based fine tuning, davinci model was used and the total fine-tuning cost was 9.28$.

In order to use the model after training, the following command can be executed with the prompt and the separator or the model can be tested at OpenAI’s playground which can be accessed through this [link](https://beta.openai.com/playground "link"):

`openai api completions.create -m FINETUNED MODEL -p "ADD PROMPT HERE ->" -M 200
`
## Random Questions for Testing

- How dangerous is the coronavirus to asthmatic teenagers?
- Can coronavirus be killed by hot or cold temperatures?
- Is it necessary to cover my face in public?
- And if so, how can I do it?
- When the flu claims far more lives than the coronavirus, why be concerned?
- What can I do if a member of my family believes they have the coronavirus?

## Results 

The model was finetuned on 4 Epochs only. The results with number of steps, elapsed tokens, elapsed examples, training loss, training sququence accuracy and training token accuracy can be seen in results.csv and can be obtained by using the follwing command

`openai api fine_tunes.results -i <YOUR_FINE_TUNE_JOB_ID>`

