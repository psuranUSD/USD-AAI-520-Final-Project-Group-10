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

- **Citation (APA 7):** Saqur, R., Kato, K., Vinden, N., & Rudzicz, F. (2024). *NIFTY-LM: Financial news headlines dataset for LLMs* [Data set]. Hugging Face. https://huggingface.co/datasets/raeidsaqur/NIFTY (paper: arXiv:2405.09747)

## 3. yfinance

- **Location:** <https://github.com/ranaroussi/yfinance> (`pip install yfinance`)

- **Summary:** yfinance offers a Pythonic way to fetch financial and market data from Yahoo! Finance. It is an open-source tool that uses Yahoo's publicly available APIs, intended for research and educational use.

- **License:** Apache-2.0.

- **Citation (APA 7):** Aroussi, R. (n.d.). *yfinance* [Computer software]. GitHub. https://github.com/ranaroussi/yfinance

## 4. FRED (Federal Reserve Economic Data)

- **Location:** <https://fred.stlouisfed.org> (public CSV endpoint `fredgraph.csv`, no API key)

- **Summary:** The Federal Reserve Bank of St. Louis's economic database of more than 800,000 US and international series. This project reads one series, `DGS10` (10-Year Treasury Constant Maturity Rate, daily), as a macro-context feature.

- **License:** Public domain (US federal government data); FRED terms of use apply.

- **Citation (APA 7):** Board of Governors of the Federal Reserve System. (n.d.). *10-Year Treasury Constant Maturity Rate* [Data set]. Federal Reserve Bank of St. Louis. https://fred.stlouisfed.org/series/DGS10

## 5. Google Gemini API

- **Location:** <https://ai.google.dev/gemini-api>

- **Summary:** Google's generative-model API, used at temperature 0 throughout. In the ticker-agent notebook `gemini-3.5-flash-lite` serves the eight agent roles (concept proposal, planning and routing, term-quality investigation, transmission-channel judgment, pre-decision advocacy, the final decision, decision auditing, and outcome reflection). The proposal notebook uses `gemini-3.1-flash-lite` for its zero-shot sentiment comparison and its monthly portfolio backtest, and the EDA notebook uses `gemini-3.5-flash-lite` for its zero-shot comparison. Replies are cached on disk keyed by prompt hash, so reruns make no calls.

- **License:** Google Generative AI API Terms of Service.

- **Citation (APA 7):** Google. (n.d.). *Gemini API* [Computer software]. https://ai.google.dev/gemini-api

## 6. spaCy English models (en_core_web_sm, en_core_web_md)

- **Location:** <https://github.com/explosion/spacy-models/releases> (installed as packages `en-core-web-sm`, `en-core-web-md`, version 3.8.0)

- **Summary:** Pretrained spaCy pipelines for English. The ticker pipeline uses `en_core_web_sm` for part-of-speech tagging, lemmatization, and named-entity recognition on news headlines, and `en_core_web_md` for its 300-dimensional static word vectors, which score candidate terms against concept and market-process seed sets before theme clustering.

- **License:** MIT.

- **Citation (APA 7):** Honnibal, J., Montani, I., Van Landeghem, S., & Boyd, A. (2020). *en_core_web_sm / en_core_web_md (3.8.0)* [Computer software]. Explosion / GitHub. https://github.com/explosion/spacy-models/releases. Word vectors from: Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global vectors for word representation. *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 1532–1543. https://doi.org/10.3115/v1/D14-1162

## 7. SEC EDGAR

- **Location:** <https://www.sec.gov/edgar> (submissions API: `https://data.sec.gov/submissions/CIK##########.json`)

- **Summary:** The U.S. Securities and Exchange Commission's Electronic Data Gathering, Analysis, and Retrieval system. This project reads one endpoint per ticker — the company submissions JSON, which lists each filing's type (10-K, 10-Q, 8-K) and filing date — as business-context input for the earnings analysis agent. Requests identify themselves with a `User-Agent` header, and responses are cached on disk, so reruns make no calls.

- **License:** Public domain (US federal government data); SEC fair-access terms apply.

- **Citation (APA 7):** U.S. Securities and Exchange Commission. (n.d.). *EDGAR: Electronic Data Gathering, Analysis, and Retrieval system* [Data set]. https://www.sec.gov/edgar

## 8. Alpha Vantage

- **Location:** <https://www.alphavantage.co> (free-tier REST API; the public `demo` key serves sample series)

- **Summary:** A market-data API offering daily equity series, technical indicators, and real-time sentiment and news feeds under a free API key. The EDA probes it once with the public demo key: its daily price series duplicates the yfinance feed already in use and its sentiment endpoints are live-window only, so it adds no archival data for the 2010-2020 corpus window and is not used downstream.

- **License:** Alpha Vantage Terms of Use (free tier).

- **Citation (APA 7):** Alpha Vantage. (n.d.). *Alpha Vantage APIs* [Computer software]. https://www.alphavantage.co

## 9. NewsAPI.org

- **Location:** <https://newsapi.org> (v2 REST API)

- **Summary:** A news aggregation API. The free developer tier requires an API key and serves a rolling window of roughly 30 days of article history, so it cannot backfill the project's 2010-2020 evaluation window. The EDA documents the access gate and the source is recorded as a live-only extension.

- **License:** NewsAPI Terms of Service.

- **Citation (APA 7):** NewsAPI. (n.d.). *NewsAPI.org* [Computer software]. https://newsapi.org
