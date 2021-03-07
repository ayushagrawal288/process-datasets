from dataset.datasource import LocalStorage, URL
from dataset.output import LocalStorageOutputCSV
from dataset.dataset import CSV, Excel, JSON


def csv_local():
    filename = "character-predictions.csv"
    source = LocalStorage("/Users/shivang/Downloads/archive", filename)
    output = LocalStorageOutputCSV(filename)
    dataset = CSV(source, output)
    dataset.refresh()
    dataset.fetch_all()


def csv_url():
    url = "https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-September-2020-quarter/Download-data/business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv"
    filename = "test.csv"
    source = URL(url, filename)
    output = LocalStorageOutputCSV(filename)
    dataset = CSV(source, output)
    dataset.refresh()
    dataset.fetch_all()


def excel_local():
    filename = "character-deaths.xlsx"
    source = LocalStorage("/Users/shivang/Downloads/archive", filename)
    output = LocalStorageOutputCSV(filename)
    dataset = Excel(source, output)
    dataset.refresh()
    dataset.fetch_all()


def json_local():
    filename = "battles.json"
    source = LocalStorage("/Users/shivang/Downloads/archive", filename)
    output = LocalStorageOutputCSV(filename)
    dataset = JSON(source, output)
    dataset.refresh()
    dataset.fetch_all()


json_local()
