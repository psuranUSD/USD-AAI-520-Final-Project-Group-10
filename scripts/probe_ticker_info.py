"""Probe whether yfinance provides enough metadata to resolve any ticker to news-filter terms.

For each ticker given on the command line, this script checks which identity
fields Yahoo Finance returns (`symbol`, `shortName`, `longName`, `sector`) and
derives the company-specific regex terms the news relevance filter would use.
Tickers that resolve through `info` alone need no curated bank; the script also
shows how an unknown ticker fails so the pipeline can degrade gracefully.

Usage:
    uv run python scripts/probe_ticker_info.py [TICKER ...]

Defaults to a deliberately mixed basket: large caps, a punctuated ticker, a
foreign ADR, an ampersand name, and an invalid symbol.
"""

import re
import sys

import pandas as pd
import yfinance as yf

DEFAULT_TICKERS = ["AAPL", "MSFT", "NVDA", "TSLA", "BRK-B", "SAP", "JNJ", "ZZZZ"]

# Corporate suffixes stripped before taking the leading company name.
SUFFIXES = (
    r"(inc|corp|corporation|ltd|plc|co|company|holdings|group|ag|se|nv|sa)"
    r"\.?$"
)


def derive_filter_terms(info):
    """Derive news-filter terms from a yfinance `info` dict, or None if unusable."""
    symbol = info.get("symbol")
    names = {info.get("shortName"), info.get("longName")} - {None, ""}

    terms = set()
    for name in names:
        base = re.sub(r"[^\w\s]", " ", str(name).lower())
        base = re.sub(SUFFIXES, "", base.strip()).strip()
        if base:
            first_word = base.split()[0]
            if len(first_word) > 1:
                terms.add(first_word)

    if symbol:
        terms.add(re.escape(symbol.lower()))

    return sorted(terms) or None


def probe_ticker(ticker):
    """Return the resolution record for one ticker."""
    record = {"ticker": ticker, "symbol": None, "short_name": None,
              "long_name": None, "sector": None, "terms": None, "verdict": "unresolved"}

    try:
        info = yf.Ticker(ticker).info or {}
    except Exception as error:  # invalid symbols raise or return junk
        record["error"] = f"{type(error).__name__}: {error}"
        return record

    record["symbol"] = info.get("symbol")
    record["short_name"] = info.get("shortName")
    record["long_name"] = info.get("longName")
    record["sector"] = info.get("sector")

    terms = derive_filter_terms(info)
    record["terms"] = ", ".join(terms) if terms else None
    if terms and (record["short_name"] or record["long_name"]):
        record["verdict"] = "resolved"
    elif terms:
        record["verdict"] = "partial"

    return record


def main():
    tickers = sys.argv[1:] or DEFAULT_TICKERS
    records = [probe_ticker(ticker) for ticker in tickers]

    frame = pd.DataFrame.from_records(records)
    with pd.option_context("display.max_colwidth", 60, "display.width", 200):
        print(frame.to_string(index=False))

    resolved = (frame["verdict"] == "resolved").sum()
    print(f"\nResolved through yfinance info alone: {resolved} of {len(frame)}")
    print("Unresolved tickers degrade gracefully in the pipeline:")
    print("the news relevance filter widens and the brief carries a caution note.")


if __name__ == "__main__":
    main()
