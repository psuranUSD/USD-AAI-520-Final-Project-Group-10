# Data & API Sources

All datasets and APIs used in this project's notebooks are documented here.

---

## 1. Financial PhraseBank

- **Location:** <https://huggingface.co/datasets/takala/financial_phrasebank>

- **Summary:** A polar sentiment dataset of sentences from English-language financial news. The dataset consists of 4,840 sentences categorised by sentiment, divided by the agreement rate of 5–8 annotators.

- **Configurations:** `sentences_50agree` (4,846 instances), `sentences_66agree` (4,217), `sentences_75agree` (3,453), `sentences_allagree` (2,264). There is no train/validation/test split. Total size ≈ 699 kB.

- **License:** CC BY-NC-SA 3.0 (Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported).

- **Citation (APA 7):** Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). Good debt or bad debt: Detecting semantic orientations in economic texts. *Journal of the Association for Information Science and Technology, 65*. Dataset: Takala, P. (n.d.). *Financial PhraseBank* [Data set]. Hugging Face. https://huggingface.co/datasets/takala/financial_phrasebank

## 2. NIFTY (News-Informed Financial Trend Yield)

- **Location:** <https://huggingface.co/datasets/raeidsaqur/NIFTY>

- **Summary:** The News-Informed Financial Trend Yield (NIFTY) dataset. Details of the dataset, including data procurement and filtering, are given in the accompanying paper.

- **Contents:** 2,111 examples spanning 2010-01-06 to 2020-09-21. Train: 1,477 (2010-01-06 – 2017-06-27); validation: 317 (2017-06-28 – 2019-02-12); test: 317 (2019-02-13 – 2020-09-21). Total size ≈ 44.4 MB.

- **License:** MIT.

- **Citation (APA 7):** Saqur, R. (2024). *NIFTY-LM: Financial news headlines dataset for LLMs* [Data set]. Hugging Face. https://huggingface.co/datasets/raeidsaqur/NIFTY (paper: arXiv:2405.09747)

## 3. yfinance

- **Location:** <https://github.com/ranaroussi/yfinance> (`pip install yfinance`)

- **Summary:** yfinance offers a Pythonic way to fetch financial and market data from Yahoo! Finance. It is an open-source tool that uses Yahoo's publicly available APIs, intended for research and educational use.

- **License:** Apache-2.0.

- **Citation (APA 7):** Aroussi, R. (n.d.). *yfinance* [Computer software]. GitHub. https://github.com/ranaroussi/yfinance
